from random import uniform
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import numpy as np
class SMA:
    def __init__(self):
        self.data=[]
        self.mean=[]
        self.sum=0
        self.window=0
        self.size=0
        print('Simple Moving Average')
    def set(self, size, window):
        self.size = size
        self.window = window
    def getData(self, size):
        return self.data
    def countAverage(self, size, window):
        self.set(size, window)
        self.data=[uniform(56, 58) for i in range(self.size)]
        for i in range(self.size - self.window + 1):
            k = i
            for element in range(self.window):
                self.sum += self.data[k]
                k += 1
            self.mean.append(self.sum / self.window)
            self.sum = 0
        return self.mean

def main():
    s=SMA()
    size=int(input('Enter size of data: '))
    window=int(input('Enter size of window: '))
    print(s.countAverage(size, window))
    x = np.arange(size)
    pl.plot(x, s.data)
    pl.plot(s.mean, color='tomato')
    pl.title('Simple Moving Average')
    pl.ylabel('$ rate')
    pl.xlabel('Window')
    pl.legend(('All values', 'SMA'), title='Legend')
    pl.show()
if __name__ == '__main__':
    main()


