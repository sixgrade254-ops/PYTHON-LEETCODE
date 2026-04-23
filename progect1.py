def convent_unit(value,from_unit,to_unit):
    unit_dictionary = {
        'm':1
        'cm':0.01
        'mm':0.001
        'km':1000
    }
    
    in_meters = value * unit_dictionary[from_unit]
    if to_unit = 'm':
        return in_meters
    
    elif to_unit = 'cm':
        return in_meters * 100
    
    elif to_unit = 'mm':
        return in_meters * 1000
    
    if to_unit = 'km':
        return in_meters * 0.001
    else:
        return None

value = float(input('enter the number:')) 
from_unit = (input('enter from unit:')) 
to_unit = input('enter to unit;')
print(convent_unit(value,from_unit,to_unit))

    