from machine import Pin, PWM
from time import sleep

# Initialize two servos on GPIO 16 and GPIO 17
servo1 = PWM(Pin(16))
servo2 = PWM(Pin(17))
servo1.freq(50)
servo2.freq(50)

def angle_to_duty(angle):
    # Convert 0–180° to 1000–9000 (duty cycle for 0.0–2.0ms pulse)
    return int(1000 + (angle / 180) * 8000)

def set_servo_angles(angle1, angle2):
    servo1.duty_u16(angle_to_duty(angle1))
    servo2.duty_u16(angle_to_duty(angle2))

print("Enter two angles (0–180) separated by comma. Example: 90,45")

while True:
    user_input = input(">> ")  # Get input from Thonny Shell
    try:
        parts = user_input.strip().split(",")
        if len(parts) != 2:
            print("Enter exactly two angles like 90,45")
            continue
        angle1 = int(parts[0])
        angle2 = int(parts[1])
        if not (0 <= angle1 <= 180 and 0 <= angle2 <= 180):
            print("Angles must be between 0 and 180")
            continue
        set_servo_angles(angle1, angle2)
    except:
        print("Invalid input. Please enter like 90,45")

