from machine import Pin, Timer
import time

# 定义 Pin 控制引脚
led = Pin(48, Pin.OUT)

# 定义定时器中断的回调函数
def timer_irq(timer_pin):
    led.value(not led.value())

# 定义定时器
timer = Timer(0)
# 初始化定时器
timer.init(period = 500, mode = Timer.PERIODIC, callback = timer_irq)

while True:
    time.sleep(1)