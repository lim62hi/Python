while True:
    try:
        nums = input('Numbers: ').split()
        nums = [int(num) for num in nums]
        def filter(array = None):
            if array != None:
                array.sort()
                array = [i for i in array if i > 0]
                array = [i for i in array if i % 5 == 3]
                return array
        print(filter(nums))
    except ValueError:
        print('Irregular numbers!')