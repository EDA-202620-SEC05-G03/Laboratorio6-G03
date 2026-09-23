import random
 
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def new_map(num_elements, load_factor, prime=109345121):

    capacity = mf.next_prime(num_elements/load_factor)

    table = lt.new_list()
    
    for _ in range(capacity):
        lt.add_last(table, me.new_map_entry(None, None))

    tabla ={
        'prime': prime,
        'capacity': capacity,
        'scale': random.randint(1, prime - 1),
        'shift': random.randint(0, prime - 1),
        'table': table,
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0
    }
    
    return tabla

