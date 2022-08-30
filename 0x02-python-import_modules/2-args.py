if __name__ == '__main__':
    import sys
    le = len(sys.argv)
    if le <= 1:
        print('{:d} arguments.'.format(le - 1))
    else:
        if le == 2:
            print('{:d} argument:'.format(le - 1))
        else:
            print('{:d} arguments:'.format(le - 1))
        for x in range(1 , le):
            print('{:d}: {}'.format(x, sys.argv[x]))
            

    