# Servo control using Raspberry Pi Pico
# 🦾 2-DOF Robotic Arm with Raspberry Pi Pico

This MicroPython project allows you to control **two servo motors** using a **Raspberry Pi Pico** via **serial input** through the Thonny IDE. It's a foundation for a robotic arm or similar servo-based mechanisms.

---

## 📦 Components Used

- Raspberry Pi Pico
- SG90 servo motors (x2)
- External 5V power supply (recommended)
- Breadboard and jumper wires
- Thonny IDE (for code upload and serial input)

---

## 🔌 Wiring

| Servo | GPIO Pin | VCC | GND |
|-------|----------|-----|-----|
| Servo 1 | GPIO 16 | 5V (external) | GND |
| Servo 2 | GPIO 17 | 5V (external) | GND |

> ⚠️ **Important:** Connect **Pico GND**, **servo GND**, and **power supply GND** together.

---

## 🚀 Usage Instructions

1. Upload the `main.py` script to your Raspberry Pi Pico using Thonny.
2. Open the **Thonny Shell** (bottom panel).
3. Input two angles (0–180) separated by a comma, like: 90,45
- This will move:
  - Servo 1 to 90°
  - Servo 2 to 45°

4. The script will keep prompting for new inputs.

---

## 🧠 Code Highlights

- Uses `PWM` on GPIO16 and GPIO17 at 50 Hz for standard servo control.
- Converts angle (0–180) to pulse width using:
```python
duty = int(1000 + (angle / 180) * 8000)
