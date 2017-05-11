from random import uniform
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import numpy as np

size=int(input('Enter size of data: '))
data=[uniform(56,58)for i in range(size)]
print(data)
window=int(input('Enter size of window: '))
mean=[]
sum=0
for i in range(size-window+1):
    k=i
    for element in range(window):
        sum+=data[k]
        k+=1
    mean.append(sum/window)
    sum=0
print(mean)
grid = plt.grid(True)
x=np.arange(size)
pl.plot(x,data)
pl.plot(mean, color='tomato')
pl.title('Simple Moving Average')
pl.ylabel('$ rate')
pl.xlabel('Window')
pl.legend ( ('All values', 'SMA'),title='Legend')
pl.show()





