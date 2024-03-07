import machine					#导入机器硬件的接口类
import time						#导入时间类

led_gpio = 48					#定义一个变量【LED控制引脚】为48

#初始化 led_gpio 引脚为输出模式，开启上拉电阻，默认输出低电平（0）
led_pin =machine.Pin(led_gpio, machine.Pin.OUT, machine.Pin.PULL_UP)

while True:
    
    #将引脚设置为“1”输出电平
    led_pin.on()
    
    #延时500ms
    time.sleep(0.5)					#utime.sleep(seconds)
    
    #将引脚设置为“0”输出电平
    led_pin.off()
    
    #延时500ms
    time.sleep(0.5)
    
#这个是单行注释
    
'''
这个是多行注释
'''
"""
这个也是多行注释
"""