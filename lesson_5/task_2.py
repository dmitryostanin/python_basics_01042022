try:
    with open("task_2.txt", "r") as file:
        count = 0
        for line in file:
            count += 1
            print(f'Line #{count}: {len(line.split())} word(s)')
        print(f'Total lines: {count}')
except IOError as ioe:
    print(f'I/O error: {ioe}')