def process_numbers(numargs):

    numbers = []

    if isinstance(numargs, list) != False:
        for item in numargs:

            if isinstance(item, str) != False:
                letters = item.isalpha()
                if letters == True:
                    continue           
            elif isinstance(item, int) == False:
                #item = int(item)
                #numbers.append(item)
                continue
            item = int(item)
            numbers.append(item)

    numbers.sort()
    return numbers