import random
 
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def new_map(num_elements, load_factor, prime=109345121):

    capacity = mf.next_prime(num_elements/load_factor)

    table = lt.new_list()
    
    for _ in range(capacity):
        lt.add_last()
        

    tabla ={
        'prime': prime,
        'capacity': capacity,
        'scale': 1,
        'shift': 0,
        'table': {
            'size': 11,
            'elements': [
                {'key': None},
                {'key': None},
                ]
        },
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0
    }
    
    return tabla

