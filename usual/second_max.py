while True:
    try:
        nums = input('Numbers: ').split()
        nums = [int(i) for i in nums]
        def second(array):
            nums.remove(max(nums))
            return max(nums)
        print(f'Second of max: {second(nums)}')
    except:
        print('Irregular numbers!')