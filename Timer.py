from machine import Pin, Timer
import time


led = Pin(48, Pin.OUT)


def timer_irq(timer_pin):
    led.value(not led.value())


timer = Timer(0)

timer.init(period = 500, mode = Timer.PERIODIC, callback = timer_irq)

while True:
    time.sleep(1)