class NotANumberError(ValueError):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


numbers = []
number = ''

while True:
    try:
        number = input('Enter number or ''stop'' to exit: ')
        if number.isdigit():
            numbers.append(float(number))
        elif number.upper() != 'STOP':
            raise NotANumberError('Not a number!')
        else:
            break
    except NotANumberError as nane:
        print(nane)

print(f'Numbers list: {numbers}')
