while True:
    try:
        def days(num = None):
            if num != None and num > 0:
                num %= 7
                if num == 1:
                    return 'понедельник'
                elif num == 2:
                    return 'вторник'
                elif num == 3:
                    return 'среда'
                elif num == 4:
                    return 'четверг'
                elif num == 5:
                    return 'пятница'
                elif num == 6:
                    return 'суббота'
                elif num == 7:
                    return 'воскресенье'
            else:
                return None
        nums = [int(i) for i in input('Номера дней недели: ').split()]
        for i in nums:
            print(f'{i} день недели это {days(i)}!')
    except ValueError:
        print('Irregular day of the week!')
    except:
        print('Error')