first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = first_value.lower()
first_value = first_value.title()

print(first_value.rstrip().rjust(22))

# Second challenge
second_value = second_value.strip('-')
second_value = second_value.strip()

print(second_value.capitalize())

# Third challenge 
third_value = third_value.swapcase()
third_value = third_value.replace(' ','')
third_value = third_value.replace('-',' ')

print(third_value.rjust(31))

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')


### CHALLENGE OUTPUT ###
#       First Challenge        
#Second challenge
#               Third challenge
#fourth#fifth#sixth!
#        fourth
#        fifth
#        sixth