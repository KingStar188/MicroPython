
#热点模式允许用户将自己的ESP32配置为热点，
#这让多个 ESP32 芯片之间的无线连接在不借助外部路由器网络的情况下成为可能。
import network

ap = network.WLAN(network.AP_IF) # 创建一个热点
ap.active(True)         # 激活热点
# 为热点配置热点名称，通道，加密方式，密码
ap.config(essid='LCKFB', channel=5, authmode=3, password="12345678") 



#将 ESP32 连接到 WiFi 网络
"""
import time
import network


# 设置路由器 WiFi 账号与密码
ssid = 'qwer'
password = '12345678'

# 创建 WIFI 连接对象
wlan = network.WLAN(network.STA_IF)
# 激活 wlan 接口
wlan.active(True)
# 扫描允许访问的 WiFi
print('扫描周围信号源：', wlan.scan())

print("正在连接 WiFi 中", end="")
# 
wlan.connect(ssid, password)

# 如果一直没有连接成功，则每隔 0.1s 在命令号中打印一个 .
while not wlan.isconnected():
  print(".", end="")
  time.sleep(0.1)

# 连接成功之后，打印出 IP、子网掩码(netmask)、网关(gw)、DNS 地址
print(f"\n{wlan.ifconfig()}")
"""
