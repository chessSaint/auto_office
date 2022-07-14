import time  ##导入时间模块
fahrenheit=int(input("输入华氏温度："))
celsius=(fahrenheit-32)/1.8
print("%.1f华氏温度转化为摄氏温度为%.1f" %(fahrenheit,celsius))
time.sleep(20) ##输出结果后等待20s退出程序