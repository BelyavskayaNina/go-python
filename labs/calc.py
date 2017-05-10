def choice():
    print('Enter № of function:\n0)Exit\n1)+\n2)-\n3)*\n4)/\n5)^\n6)sqrt')
    function = int(input())
    return function
def sum(x,y):
    result = x + y
    print('Result: ' + str(x) + ' + ' + str(y) + ' = ' + str(result))
    return result
def sub(x,y):
    result = x - y
    print('Result: ' + str(x) + ' - ' + str(y) + ' = ' + str(result))
    return result
def multi(x,y):
    result = x * y
    print('Result: ' + str(x) + ' * ' + str(y) + ' = ' + str(result))
    return result
def div(x,y):
    result = x / y
    print('Result: ' + str(x) + ' / ' + str(y) + ' = ' + str(result))
    return result
def expo(x,y):
    result = x ** y
    print('Result: ' + str(x) + ' ^ ' + str(y) + ' = ' + str(result))
    return result
def root(x,y):
    result = abs(x ** (1 / y))
    print('Result: ' + 'sqrt(' + str(x) + ') ^ ' + str(y) + ' = ' + str(result))
    return result

def main():
    res=0
    check=1
    repeat=True
    print ('Calculator\n----------')
    while repeat:
        if check == 1:
            a = float(input('a='))
        func=choice()
        if func == 0:
            print ('Goodbye!')
            break
        if func < 7:
            b=float(input('b='))
            if func == 1:
                res=sum(a,b)
            elif func == 2:
                res=sub(a,b)
            elif func == 3:
                res=multi(a,b)
            elif func == 4:
                try:
                    div(a,b)
                except ZeroDivisionError:
                    print('Division by zero!')
                    continue
            elif func == 5:
                res=expo(a,b)
            elif func == 6:
                if b>=2:
                    res=root(a,b)
                else:
                    print('Enter an integer value >= 2!')
                    continue
        else:
            print('Invalid value, try again!')
            print ('------------------------')
        if int(input('Continue? 0-NO; 1-YES '))== 1:
            a=res
            check = 0
            print('----------------------')
            print('a = ',a)
        else: repeat=False
    else: print ('Goodbye!')
if __name__==('__main__'):
    main()


