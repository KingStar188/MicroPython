from bluetooth import BLE
import bluetooth

bt = BLE()        #创建蓝牙对象
bt.active(1)#打开蓝牙

SERVER_1_UUID = bluetooth.UUID(0x9011)
CHAR_A_UUID = bluetooth.UUID(0x9012)
CHAR_B_UUID = bluetooth.UUID(0x9013)

#设置特性的读写权限
CHAR_A = ( CHAR_A_UUID, bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY,)
CHAR_B = ( CHAR_B_UUID, bluetooth.FLAG_READ | bluetooth.FLAG_WRITE,)

#把特性A和特性B放入服务1
SERVER_1 = (SERVER_1_UUID, (CHAR_A, CHAR_B),)
#把服务1放入 服务集合 中
SERVICES = (SERVER_1,)
#注册服务到gatts
((char_a, char_b),) = bt.gatts_register_services(SERVICES)

#开启广播
bt.gap_advertise(100, adv_data=b'\x02\x01\x05\x05\x09\x42\x69\x62\x69')
 
#蓝牙中断复位函数
def ble_irq(event, data):
    if event == 1:#蓝牙已经连接
        pass
    elif event == 2:#蓝牙断开连接
        bt.gap_advertise(100, adv_data=b'\x02\x01\x05\x04\x09\x42\x69\x62\x69')
    elif event == 3:#写入事件
        conn_handle, chan_handle = data
        buffer = ble.gatts_read(char_handle)
        #输出接收到的数据
        print(buffer)
        if buffer == b'A': #如果数据为单个字符A
            #向手机发送数据 单个字符B
            ble.gatts_notify(0, char_handle, b'B')        
bt.irq(ble_irq)
 