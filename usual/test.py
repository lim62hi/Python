while True:
    try:
        f = float(input('First: '))
        s = float(input('Second: '))
        r = max(f, s)
        r = 'First is bigger, than second' if r == f else 'Second is bigger, than first'
        print(r)
        break
    except:
        print('Something isn\'t right!')