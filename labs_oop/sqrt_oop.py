class sqrtHeron:
    def __init__(self):
        self.num=0
        self.res=0
        self.bound=0

        print('-----------------------------')
        print("Square root (Heron's formula)")
        print('-----------------------------')

    def set(self, res, num):
        self.res=res
        self.num=num

    def calc_sqrt(self, res, num):
        self.set(res, num)
        self.res = self.num
        while self.res != self.bound:
            self.bound = self.res
            self.res = 1 / 2 * (self.res + self.num / self.res)
        return self.res
class Input:
    def __init__(self):
        self.number=0
    def checkInputNumber(self):
        while True:
            try:
                self.number = float(input('Enter value:'))
            except ValueError:
                print("Invalid value! Please enter a number.")
                continue
            if self.number < 0:
                print("The number is negative! Please enter a positive one.")
            elif self.number == 0:
                print("The sqrt of '0' is '0'!!!")
                exit()
            else:
                break
        return self.number
def main():
    num=Input()
    sqrt=sqrtHeron()
    number=num.checkInputNumber()
    x=number
    print('Result: ' + str(sqrt.calc_sqrt(x, number)))
if __name__ == '__main__':
    main()
