if __name__ == '__main__':
    import sys
    a = len(sys.argv)
    sum = 0
    for x in range(1 , a):
        sum += int(sys.argv[x])
    print('{:d}'.format(sum))
