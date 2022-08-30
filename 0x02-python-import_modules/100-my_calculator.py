#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    l = len(sys.argv)
    if l != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        if sys.argv[2]  not in '+-*/':
            print("Unknown operator. Available operators: +, -, * and /")
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if sys.argv[2] == '+':
                print(' {:d} {} {:d} = {:d}'.format(a, sys.argv[2], b, add(a, b) ))
            elif sys.argv[2] == '-':
                print(' {:d} {} {:d} = {:d}'.format(a, sys.argv[2], b, sub(a, b) ))
            elif sys.argv[2] == '*':
                print(' {:d} {} {:d} = {:d}'.format(a, sys.argv[2], b, mul(a, b) ))
            elif sys.argv[2] == '/':
                print(' {:d} {} {:d} = {:d}'.format(a, sys.argv[2], b, div(a, b) ))
            
    
        

