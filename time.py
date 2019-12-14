'''from datetime import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'
t1='Sun 10 May 2015 13:54:36 -0700'
t2='Sun 10 May 2015 13:54:36 -0000'
time1 = dt.strptime(t1, fmt)
time2 = dt.strptime(t2, fmt)
print(int(abs((time1-time2).total_seconds())))
'''
'''
for _ in range(int(input())):
    time1 = dt.strptime(t1, fmt)
    #time1 = dt.strptime(input(), fmt)
    time2 = dt.strptime(t2, fmt)
    #time2 = dt.strptime(input(), fmt)
   print(int(abs((time1 - time2).total_seconds())))
'''
'''
from datetime import datetime

def time_delta(t1, t2):
    t1=datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return (int(abs((t1-t2).total_seconds())))

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
    print(delta)
'''

str1='07:05:45PM'
time=str1.split(':')
print(time)



