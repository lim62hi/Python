def numbers(num):
    nums = tuple([i for i in num if i != ' '])
    return f'Text is {nums}'
while True:
    number = input('Text: ')
    print(numbers(number))