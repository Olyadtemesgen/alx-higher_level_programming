def safe_print_division(a, b):
    try:
        resu = a / b
        return resu
    except:
        resu = None
    finally:
        print("Inside result: {}".format(resu),end = '\n')
