def process_numbers(numargs):
    numbers = []

    for item in numargs: #items():
        #if item.isnumeric():
        numbers.append(item)
        print(type(item))
        #else:
         #   continue

    #numbers.sort()
    return numbers