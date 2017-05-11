def calc_sqrt(a,num):
    b=0
    a = num
    while a != b:
        b = a
        a = 1 / 2 * (a + num / a)
    return a
def main():
    print ('-----------------------------')
    print ("Square root (Heron's formula)")
    print ('-----------------------------')
    while True:
        try:
            number = float(input('Enter value:'))
        except ValueError:
            print("Invalid value! Please enter a number.")
            continue
        if number < 0:
            print("The number is negative! Please enter a positive one.")
        elif number == 0:
            print("The sqrt of '0' is '0'!!!")
            exit()
        else:
            break
    x=number
    print('Result: ' + str(calc_sqrt(x,number)))
if __name__ == '__main__':
    main()
