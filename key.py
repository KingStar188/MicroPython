from machine import Pin					#机器硬件的接口类
import time

#初始化 GPIO48 引脚为输出模式
LED = Pin (48, Pin.OUT )

#初始化 GPIO 引脚为输入模式, 使能上拉电阻
KEY = Pin (0, Pin.IN, Pin.PULL_UP)

#LED状态变量
state = 0

while True:
    #如果按键按下
    if KEY.value() == 0:
    #消抖
        time.sleep_ms (10)
        #重新确定是否按下按键
        if KEY.value() == 0:
            #LED状态变量 取反
            state = not state
            #切换LED状态
            LED.value (state)
            #等待按键松开 (如果一直为0则一直延时)
            while not KEY.value():
                time.sleep_ms(50)
