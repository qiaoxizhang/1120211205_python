#日期和时间的输出
from datetime import datetime #引用datatime库
now=datetime.now()
print(now)
print(now.strftime("%x")) #输出其中的日期
print(now.strftime("%X")) #输出其中的时间

