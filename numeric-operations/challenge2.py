print('Simple calculator!\n')
first_num = input('First number? ')
operationInput = input('Operation? ')
second_num = input('Second number? ')

operation = ['+','-','*','/','**','%']

#print(type(first_num))
#print(first_num)
#print(type(operation))
#print(operation)
#print(type(second_num))
#print(second_num)

if first_num.isnumeric() == False or second_num.isnumeric() == False:
    print('Please input a number.')
else:
    if operationInput in operation:
        print(str(operationInput + ' is valid')) 
    else:
        print('Operation not recognised.')