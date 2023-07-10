while True:
    try:
        array = tuple([i for i in input('Text: ').split()])
        print(array)
        array = tuple([i for i in array[::int(input('Step: '))]])
        print(array)
    except ValueError:
        print('Irregular numbers!')
    except:
        print('error')