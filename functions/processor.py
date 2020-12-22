def process_numbers(numargs):

    numbers = []

    if isinstance(numargs, list) != False:
        for item in numargs:
          
            if isinstance(item, str) != False:
                letters = item.isalpha()
                if letters == True:
                    continue           
            elif isinstance(item, int) == False:
                continue
            item = int(item)
            numbers.append(item)

    numbers.sort()
    return numbers

def process_names(nameargs):
    
    names = []

    if isinstance(nameargs, list) != False:
        for name in nameargs:

            if isinstance(name, str) != False:
                letters = name.isalpha()
                if letters == False:
                    continue
            else:
                continue
            names.append(name)

    names.sort()
    return names