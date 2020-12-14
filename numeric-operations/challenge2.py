print('Simple calculator!\n')
first_num = input('First number? ')
operationInput = input('Operation? ')
second_num = input('Second number? ')

if first_num.isnumeric() == False or second_num.isnumeric() == False:
    print('Please input a number.')
else:
    if operationInput == '+':
        addition = int(first_num) + int(second_num)
        print(f'sum of {first_num} {operationInput} {second_num} equals {addition}')
    elif operationInput == '-':
        difference = int(first_num) - int(second_num)
        print(f'difference of {first_num} {operationInput} {second_num} equals {difference}')
    elif operationInput == '*':
        product = int(first_num) * int(second_num)
        print(f'product of {first_num} {operationInput} {second_num} equals {product}')
    elif operationInput == '/':
        quotient = int(first_num) / int(second_num)
        print(f'quotient of {first_num} {operationInput} {second_num} equals {quotient}')        
    elif operationInput == '%':
        modulus = int(first_num) % int(second_num)
        print(f'modulus of {first_num} {operationInput} {second_num} equals {modulus}')
    elif operationInput == '**':
        exponent = int(first_num) ** int(second_num)
        print(f'exponent of {first_num} {operationInput} {second_num} equals {exponent}')
    else:
        print('Operation not recognised.')   