# Embeded MicroPyton code for Pico W

## WOKWI → FYYSINEN MUUNNOS

## WOKWI ANALYYSI

✅ GP2 → relay1:IN (Keittiö)  
✅ GP3 → relay3:IN (Olohuone)
✅ GP4 → relay4:IN (Lämpö)
✅ GP5 → relay2:IN (Vesi)
✅ VBUS → rele VCC (5V)
✅ GND → yhteinen maa
✅ 3V3 → rele COM (LEDit)
✅ NO → Kontaktori → 60W testilamput (sulake demo)
✅ GP6 → r8 → sininen LED (WiFi!)

## OSTOSLISTA

| Komponentti            | Määrä | Hinta | Liike   |
| ---------------------- | ----- | ----- | ------- |
| Raspberry Pi Pico WH   | 1     | 14€   | Partco  |
| 4-kan relemoduuli 5V   | 1     | 8€    | Motonet |
| Finder 40.61.9         | 1     | 15€   | RS      |
| USB-C kaapeli          | 1     | 3€    | Motonet |
| DIN-kotelon 6M         | 1     | 12€   | RS      |
| DIN-kisko 25cm         | 1     | 4€    | Motonet |
| DIN-kiskoliitin 3nap   | 6kpl  | 9€    | Motonet |
| Sininen LED 5mm        | 1     | 1€    | Partco  |
| 330Ω vastus            | 1     | 0.5€  | Partco  |
| Schuko pistokejohto    | 1     | 5€    | Motonet |
| Sulakeautomaatti 2A    | 1     | 3€    | Motonet |
| DuPont F-F johdot      | 20kpl | 3€    | Partco  |
| 4x E27 60W testilamppu | 4     | 12€   | Motonet |
| KOKONAISHINTA          |       | 71€   |         |

## YKSINKERTAINEN KYTKENTÄ

Matalajännite (DuPont F-F):

Pico.VBUS   → pun  → Rele.VCC
Pico.GND3   → must → Rele.GND  

Pico.GP2 → vihreä1 → Rele.IN1 (Keittiö)
GP3      → vihreä2 → Rele.IN2 (Olohuone)
GP4      → vihreä3 → Rele.IN3 (Lämpö)
GP5      → vihreä4 → Rele.IN4 (Vesi)
GP6      → sininen → SinLED+330R→GND (WiFi)

230V (DIN-liittimet, SUORA):

**Rele → Kontaktori:**
Rele1.NO → DIN-liitin → Kontaktori.A1
USB5V    → DIN-liitin → Kontaktori.A2

**Kontaktori → ламput:**
Kont.1 → DIN3 → 230V.L → 4x60W → 230V.N → DIN4 → Kont.3

**Syöttö:**
Schuko.L → Sulake2A → DIN1 → Kont.A1  
Schuko.N → DIN2 → Kont.A2

### DIN-KISKO

[Pico WH]  [Relemoduuli]  [Kontaktori]  [DIN-liittimet]
 USB-C↑      DuPont↑          liitin↑       Schuko↑

## VISUAALINEN TILANNE

🔵 Sininen LED = WiFi status (GP6)
💡 4x60W lamput = Releiden TILA (syttyy/sammuu)

## KOODI SÄILYY SAMANA

### Punaiset LEDit korvattu lampuilla, mutta logiikka sama

set_relay(relays, 0, price <= 0.10)  # Keittiö → lamppu syttyy

## Simulaattori

### <https://wokwi.com/projects/455510202460972033>
