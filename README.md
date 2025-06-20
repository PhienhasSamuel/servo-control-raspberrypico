# Servo control using Raspberry Pi Pico

This project controls a 4-DOF robotic arm using 4 servo motors and a Raspberry Pi Pico with MicroPython.

## 💡 Features
- Control up to 4 servo motors via serial input
- Scalable: easily expand from 2 to 4 servos
- Input format: `angle1,angle2,angle3,angle4`

## 📦 Components Used
- Raspberry Pi Pico
- SG90 Servo motors (x4)
- External 5V Power Supply
- Jumper wires and breadboard

## 🔌 Wiring
| Servo | Signal Pin | VCC | GND |
|-------|-------------|-----|-----|
| Servo 1 | GPIO 16 | 5V | GND |
| Servo 2 | GPIO 17 | 5V | GND |
| Servo 3 | GPIO 18 | 5V | GND |
| Servo 4 | GPIO 19 | 5V | GND |

> Make sure all GNDs are connected together (Pico GND + Servo power GND)

## 🧪 Usage
1. Upload `main.py` to your Raspberry Pi Pico using Thonny
2. Open the Thonny shell
3. Input angles like:
