class Calculator:
    def __init__(self):
        self.res = 0
        self.x = 0
        self.y = 0
        print('Welcome to calculator!\n**********************')
    def choice(self):
        print('Enter № of function:\n0)Exit\n1)+\n2)-\n3)*\n4)/\n5)^\n6)sqrt')
        function = int(input())
        return function
    def set(self, x, y):
        self.x = x
        self.y = y
    def getResult(self):
        return self.res;
    def printResult(self, res, function):
        print('Result : ' + str(self.x) + ' ' + function + ' ' + str(self.y) + ' = ' + str(res))
    def sum(self, x, y):
        self.set(x, y)
        self.res = x + y
        self.printResult(self.res, '+')
    def sub(self, x, y):
        self.set(x, y)
        self.res = x - y
        self.printResult(self.res, '-')
    def multi(self, x, y):
        self.set(x, y)
        self.res = x * y
        self.printResult(self.res, '*')
    def expo(self, x, y):
        self.set(x, y)
        self.res = x ** y
        self.printResult(self.res, '^')
    def div(self, x, y):
        self.set(x, y)
        self.res = x / y
        self.printResult(self.res, '/')
    def root(self,x, y):
        self.set(x,y)
        self.res = abs(x ** (1 / y))
        print('Result: ' + 'sqrt(' + str(x) + ') ^ ' + str(y) + ' = ' + str(self.res))


def main():
    calc = Calculator()
    res = 0
    check = 1
    repeat = True
    while repeat:
        if check == 1:
            a = float(input('a='))
        func = calc.choice()
        if func == 0:
            print ('Goodbye!')
            break
        if func < 7:
            b = float(input('b='))
            if func == 1:
                calc.sum(a,b)
            elif func == 2:
                calc.sub(a,b)
            elif func == 3:
                calc.multi(a,b)
            elif func == 4:
                try:
                    calc.div(a,b)
                except ZeroDivisionError:
                    print('Division by zero!')
                    continue
            elif func == 5:
                calc.expo(a,b)
            elif func == 6:
                if b >= 2:
                    calc.root(a,b)
                else:
                    print('Enter an integer value >= 2!')
                    continue
        else:
            print('Invalid value, try again!')
            print('------------------------')
        if int(input('Continue? 0-NO; 1-YES ')) == 1:
           a = calc.getResult()
           check = 0
           print('----------------------')
           print('a = ', a)
        else: repeat = False
    else:
        print('Goodbye!')
if __name__ == '__main__':
    main()