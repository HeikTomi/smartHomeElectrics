from time import sleep
import network
from machine import Pin
import uasyncio as asyncio
import ujson as json

# WiFi settings
SSID = "Wokwi-GUEST"
PASSWORD = ""
WLAN = network.WLAN(network.STA_IF)

# WiFi status LED pin (set to your wiring)
WIFI_LED_PIN = 6

# Relay pins (from wiring diagram: GP2-GP5)
# Relays are controlled by MCU GPIO pins below.
RELAY_PINS = (2, 3, 4, 5)

# Mock data settings
MOCK_POLL_INTERVAL = 5
RELAY_LIMITS = [0.10, 0.12, 0.14, 0.16]
LIMIT_BAND = 0.02

def init_wifi_led() -> Pin:
    led = Pin(WIFI_LED_PIN, Pin.OUT)
    led.value(0)
    return led


# WLAN connection
async def connectWifi(wifi_led: Pin) -> None:
    WLAN.active(True)
    WLAN.connect(SSID, PASSWORD)
    while not WLAN.isconnected():
        print(".", end="")
        await asyncio.sleep(0.1)
    print("OK")
    print(WLAN.ifconfig())
    wifi_led.value(1)


def init_outputs() -> tuple[list[Pin], Pin]:
    # Initialize relays (OFF on startup)
    relays = [Pin(pin_num, Pin.OUT) for pin_num in RELAY_PINS]
    for relay in relays:
        relay.off()

    wifi_led = init_wifi_led()
    return relays, wifi_led


def set_relay(relays: list[Pin], index: int, on: bool) -> None:
    if 0 <= index < len(relays):
        # Most 1-channel relay modules are active-LOW
        relays[index].value(0 if on else 1)


def set_all_relays(relays: list[Pin], on: bool) -> None:
    # Most 1-channel relay modules are active-LOW
    value = 0 if on else 1
    for relay in relays:
        relay.value(value)


async def mock_query_loop(relays: list[Pin]) -> None:
    price = 0.08
    direction = 0.01
    while True:
        for relay_no in range(1, 5):
            limit = RELAY_LIMITS[relay_no - 1]
            limit_low = max(0.0, limit - LIMIT_BAND)
            limit_high = limit + LIMIT_BAND
            payload = {
                "relay_no": relay_no,
                "stock_limit": limit,
                "stock_limit_low": round(limit_low, 3),
                "stock_limit_high": round(limit_high, 3),
                "stock_price": round(price, 3),
            }
            print(json.dumps(payload))

            # Relay ON -> NO contact active (price above limit)
            relay_on = price > limit
            set_relay(relays, relay_no - 1, relay_on)
            await asyncio.sleep(0)

        price += direction
        if price >= 0.20 or price <= 0.05:
            direction *= -1

        await asyncio.sleep(MOCK_POLL_INTERVAL)


async def main() -> None:
    relays, wifi_led = init_outputs()
    await connectWifi(wifi_led)

    asyncio.create_task(mock_query_loop(relays))

    while True:
        await asyncio.sleep(1)


asyncio.run(main())
