import random
 
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def is_available(table, pos):

   entry = lt.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def rehash(my_map):
    new_capacity_target = 2 * my_map["capacity"]
    new_table = new_map(new_capacity_target * my_map["limit_factor"],
                        my_map["limit_factor"],
                        my_map["prime"])
 
    for i in range(my_map["capacity"]):
        entry = lt.get_element(my_map["table"], i)
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            put(new_table, key, me.get_value(entry))
 
    my_map["capacity"] = new_table["capacity"]
    my_map["scale"] = new_table["scale"]
    my_map["shift"] = new_table["shift"]
    my_map["table"] = new_table["table"]
    my_map["size"] = new_table["size"]
    my_map["current_factor"] = new_table["current_factor"]
 
    return my_map

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

def put(my_map, key, value):
    hash_v = mf.hash_value(my_map, key)
    
    found, pos = find_slot(my_map, key, hash_v)
    
    if found:
        entry = lt.get_element(my_map['table'], pos)
        me.set_value(entry, value)
    else:
        lt.change_info(my_map['table'], pos, me.new_map_entry(key, value))
        my_map['size'] += 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity']
        
    if my_map['current_factor'] > my_map['limit_fator']:
        my_map = rehash(my_map)
        
def contains(my_map, key):
    hash_v = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_v)
    
    return found

def get(my_map, key):
    hash_v = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_v)
    
    if found:
        entry = lt.get_element(my_map['table'], pos)
        return me.get_value(entry)
    
    return None

def remove(my_map, key):
    hash_v = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_v)
    
    if found:
        lt.change_info(my_map['table'], pos, me.new_map_entry('__EMPTY__', '__EMPTY__'))
        my_map['size'] -= 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity']
        
    return my_map

def size(my_map):
    return my_map['size']