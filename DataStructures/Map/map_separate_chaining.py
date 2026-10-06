import random
 
from DataStructures.List import single_linked_list as sll
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def new_map(num_elements, load_factor, prime=109345121):
    
    capacity = mf.next_prime( num_elements / load_factor )
    
    tabla = lt.new_list()
    
    for _ in range(capacity):
        lt.add_last(tabla, sll.new_list())
    
    table = {
        'prime': prime,
        'capacity': capacity,
        'scale': random.randint(1, prime - 1),
        'shift': random.randint(0, prime - 1),
        'table': tabla,
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0
    }
    
    return table

def put(my_map, key, value):
    hash_v = mf.hash_value(my_map, key)
    
    bucket = lt.get_element(my_map['table'], hash_v)
    
    nodo = bucket['first']
    while nodo is not None:
        if default_compare(key, nodo['info']) == 0:
            me.set_value(nodo['info'], value)
            return my_map
        nodo = nodo['next']
    
    sll.add_last(bucket, me.new_map_entry(key, value))
    my_map['size'] += 1
    my_map['current_factor'] = my_map['size'] / my_map['capacity']
    
    if my_map['current_factor'] > my_map['limit_factor']:
        rehash(my_map)
    
    return my_map

def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1

def contains(my_map, key):
    hash_v = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map['table'], hash_v)
    
    nodo = bucket['first']
    while nodo is not None:
        if default_compare(key, nodo['info']) == 0:
            return True
        nodo = nodo['next']
            
    return False

def remove(my_map, key):
    hash_v = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map['table'], hash_v)
    
    anterior = None
    nodo = bucket['first']
    
    while nodo is not None:
        if default_compare(key, nodo['info']) == 0:
            if anterior is None:
                bucket['first'] = nodo['next']
            else:
                anterior['next'] = nodo['next']
            if bucket['last'] is nodo:
                bucket['last'] = anterior
            bucket['size'] -= 1
            my_map['size'] -= 1
            my_map['current_factor'] = my_map['size'] / my_map['capacity']
            break
        anterior = nodo
        nodo = nodo['next']
        
    return my_map

def get(my_map, key):
    hash_v = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map['table'], hash_v)
    
    nodo = bucket['first']
    
    while nodo is not None:
        if default_compare(key, nodo['info']) == 0:
            return me.get_value(nodo['info'])
        nodo = nodo['next']
    
    return None

def size(my_map):
    return my_map['size']

def is_empty(my_map):
    return size(my_map) == 0

def key_set(my_map):
    
    lista = lt.new_list()
    
    for pos in range(my_map['capacity']):
        bucket = lt.get_element(my_map['table'], pos)
        nodo = bucket['first']
        while nodo is not None:
            lt.add_last(lista, me.get_key(nodo['info']))
            nodo = nodo['next']
    
    return lista

def value_set(my_map):
    
    lista = lt.new_list()
    
    for pos in range(my_map['capacity']):
        bucket = lt.get_element(my_map['table'], pos)
        nodo = bucket['first']
        while nodo is not None:
            lt.add_last(lista, me.get_value(nodo['info']))
            nodo = nodo['next']
    
    return lista

def rehash(my_map):
    new_table = new_map(2 * my_map['capacity'] * my_map['limit_factor'],
                        my_map['limit_factor'],
                        my_map['prime'])

    for pos in range(my_map['capacity']):
        bucket = lt.get_element(my_map['table'], pos)
        node = bucket['first']
        while node is not None:
            put(new_table, me.get_key(node['info']), me.get_value(node['info']))
            node = node['next']

    my_map['capacity'] = new_table['capacity']
    my_map['scale'] = new_table['scale']
    my_map['shift'] = new_table['shift']
    my_map['table'] = new_table['table']
    my_map['size'] = new_table['size']
    my_map['current_factor'] = new_table['current_factor']
    return my_map