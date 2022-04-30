try:
    with open("task_1.txt", "w") as file:
        line = ' '
        while line:
            line = input('Enter line to write to file (or empty line to quit): ')
            file.write(f'{line}\n')
except IOError as ioe:
    print(f'I/O error: {ioe}')
