first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = first_value.lower()
first_value = first_value.title()

print(first_value.strip())

# Second challenge
second_value = second_value.strip('-')
second_value = second_value.strip()

print(second_value.capitalize())

# Third challenge

print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print('#' + fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
#print(f'')

#First Challenge        
#Second challenge
#               Third challenge
#fourth#fifth#sixth!
#        fourth
#        fifth
#        sixth