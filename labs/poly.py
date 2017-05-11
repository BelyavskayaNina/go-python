import sys
def main():
    if sys.argv[1]=='--poly' and len(sys.argv)>2:
        print ('The sequence: ',sum(map(lambda x: 1/2/float(x), sys.argv[2:])))
    else:
        print('Invalid argument or enter values!!!')
if __name__ == '__main__':
  main()


