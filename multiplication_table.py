def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(x * y, end=' ')
        print('\n')

multiplication_table(1, 3)
