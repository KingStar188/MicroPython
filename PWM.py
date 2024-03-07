from machine import Pin, PWM
import time

led = PWM(Pin(48), freq = 1000)

while True:
    #渐亮
    for i in range(0, 1024):
        led.duty(i)
        time.sleep_ms(1)
        
    #渐暗
    for i in range(1023, 0, -1):
        led.duty(i)
        time.sleep_ms(1)