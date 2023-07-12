while True:
    try:
        num = int(input('До какого числа? '))
        numnech = [i for i in range(1, num + 1) if i % 2 == 1]
        numch = [i for i in range(1, num + 1) if i % 2 == 0]
        f = 0
        s = 1
        chet = list()
        nechet = list()
        try:
            while True:
                res = (numch[f], numch[s])
                chet.append(res)
                res = (numnech[f], numnech[s])
                nechet.append(res)
                f += 2
                s += 2
        except:
            print(f'{chet}\n\n{nechet}')
    except ValueError:
        print('Irregular numbers!')
    #except:
     #   print('error')