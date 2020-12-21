def process_numbers(numargs):
    numbers = []

    if isinstance(numargs, list) != False:
        for item in numargs:
            if isinstance(item, int) == False:
                #numbers.remove(item)
                continue
            numbers.append(item)
            #numbers.remove(item)

            print(type(item))

    numbers.sort()
    return numbers