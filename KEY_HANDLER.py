from machine import Pin
import time

# 初始化 GPIO48 引脚为输出模式 
LED=Pin(48, Pin.OUT)
# 初始化 GPIO0 引脚为输入模式，使能上拉电阻
KEY=Pin(0,Pin.IN, Pin.PULL_UP) 

#定义外部中断服务函数
def key_handler(key):
    #消抖
    time.sleep_ms(10)
    #如果按钮按下
    if KEY.value() == 0:
        #LED状态取反
        LED.value(not LED.value())
        
#绑定中断服务函数, 下降沿触发，中断服务函数为key_handler
KEY.irq(key_handler, Pin.IRQ_FALLING)

while True:
    time.sleep_ms(10)

