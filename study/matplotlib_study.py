import matplotlib.pyplot as plt
import random
from matplotlib import font_manager
# my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\C:\Windows\Fonts\SIMLI.TTF",size=20)
# x=range(2,26,2)
# y=[random.randint(15,30) for i in x]
# plt.figure(figsize=(20,8),dpi=80)
# x_lab=["{}:00".format(i) for i in x]
# plt.xticks(x,x_lab,rotation=45)
# y_lab=["{}摄氏度".format(i) for i in range(min(y),max(y)+1)]
# plt.xlabel("时间",fontproperties=my_font)
# plt.ylabel("温度",fontproperties=my_font)
# plt.yticks(range(min(y),max(y)+1),y_lab,fontproperties=my_font)
# plt.plot(x,y,color='red',alpha=0.8,marker='o',linestyle='-',linewidth=1)
# plt.title("温度表",fontproperties=my_font,color='red')
# plt.savefig('2.png')
# plt.show()


# my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\C:\Windows\Fonts\SIMLI.TTF",size=20)
# x=range(0,121)
# plt.figure(figsize=(10,8),dpi=80)
# y=[random.randint(10,30) for i in x]
# plt.xlabel("时间",fontproperties=my_font,rotation=45)
# plt.ylabel("次数",fontproperties=my_font)
# plt.plot(x,y,color='blue',linewidth=2,alpha=0.7)
# plt.title("每分钟心脏跳动数",color='red',fontproperties=my_font)
# plt.show()
# import matplotlib
# import numpy as np
# x=np.arange(5)
# x1=[59,82,75,65,72]
# x2 = [68, 82, 77, 89, 61]
# x3 = [90, 71, 86, 53, 62]
# total_width,n=0.83,3
# width=total_width/n
# x=x-(total_width-width)/2
# plt.bar(x,x1,width=width,label='language',fc='b')
# plt.bar(x+width,x2,width=width,label='math',fc='r')
# plt.bar(x+2*width,x3,width=width,label='english',fc='y')
# plt.xticks(np.arange(5),['tom','jack','bob','jone','lucy'])
# plt.legend()
# plt.show()
my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\SIMLI.TTF",size=20)

plt.style.use('fivethirtyeight')
def set_chinese_font():
    plt.rcParams['font.family'] = my_font.get_name()
# 设置中文字体
set_chinese_font()
price = [2.50, 1.23, 4.02, 3.25, 5.00, 4.40]
sales_per_day = [34, 62, 49, 22, 13, 19]
plt.scatter(price,sales_per_day)
plt.title('价格的')
plt.xlabel('价格')
plt.ylabel('hh')
plt.tight_layout()
plt.show()






