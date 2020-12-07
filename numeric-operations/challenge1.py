fahrenheit = input('What is the temperature in fahrenheiht? ')

if fahrenheit.isnumeric() == False:             # checks if variable is number, otherwise exit
    print('Input is not a number')
    exit()
else:
    celsius = (int(fahrenheit) - 32) * 5/9      # calcuation 
    celsius = round(celsius)                    # round up result value
    print('Temperature in celsius is ' + str(celsius))