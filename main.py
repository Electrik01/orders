import math
from config import *

def pseudo_generator():
    pseudo_randomized_numbers = []
    seed = SEED
    for i in range(COUNT_ORDERS):
        pseudo_randomized_numbers.append(seed)
        seed = (seed*MULTIPLIER+INCREMENT)%MODULE
    return pseudo_randomized_numbers

def copy_element(iter, value):
    if(iter<ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH):
        return [value]*MIN_COUNT_RECORDS
    else:
        return [value]*MAX_COUNT_RECORDS

def id_generator(pseudo_randomized_numbers):
    id_values = []
    for i in range(COUNT_ORDERS):
        id_value = hex(pseudo_randomized_numbers[i])[2:].rjust(10,'0')
        id_values.extend(copy_element(i,id_value))
    return id_values

def insturments_generator(pseudo_randomized_numbers):
    insturments_values = []
    for i in range(COUNT_ORDERS):
        instrument_num = pseudo_randomized_numbers[i]//DIVISIOR % COUNT_INSTRUMENT
        insturments_values.extend(copy_element(i,INSTRUMENTS[instrument_num]))
    return insturments_values

def px_init_generator(pseudo_randomized_numbers):
    px_init_values = []
    for i in range(COUNT_ORDERS):
        px_init_num = pseudo_randomized_numbers[i]//DIVISIOR_PX_INIT % COUNT_INSTRUMENT
        px_init_change = pseudo_randomized_numbers[i]//DIVISIOR_PX_INIT % 50 * PX_INIT[px_init_num][1] #or 100
        px_init_value = round(PX_INIT[px_init_num][0]+px_init_change,5)
        px_init_values.extend(copy_element(i,px_init_value))
    return px_init_values

def volume_init_generator(pseudo_randomized_numbers):
    volume_init_values = []
    for i in range(COUNT_ORDERS):
        volume_init_multiplier = math.pow(10,pseudo_randomized_numbers[i]%3+2)
        volume_init_value = int(pseudo_randomized_numbers[i]//DIVISIOR_VOLUME_INIT * volume_init_multiplier)
        volume_init_values.extend(copy_element(i,volume_init_value))
    return volume_init_values

def side_generator(pseudo_randomized_numbers):
    side_values = []
    for i in range(COUNT_ORDERS):
        if pseudo_randomized_numbers[i]//DIVISIOR_SIDE % 2 == 0:
            side_values.extend(copy_element(i,SIDE[0]))
        else:
            side_values.extend(copy_element(i,SIDE[1]))
    return side_values

def status_generator(pseudo_randomized_numbers):
    status_values = []
    for i in range(COUNT_ORDERS):
        status_num = pseudo_randomized_numbers[i]//DIVISIOR_STATUS%3
        if i < ORDER_CREATED_BEFORE_START:
            status_values.extend([STATUS[1],STATUS[2][status_num],STATUS[3]])
        elif i < ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
            status_values.extend([STATUS[0],STATUS[1],STATUS[2][status_num]])
        else:
            status_values.extend([STATUS[0],STATUS[1],STATUS[2][status_num],STATUS[3]])
    return status_values

def px_fill_generator(pseudo_randomized_numbers):
    px_fill_values = []
    for i in range(COUNT_ORDERS):
        px_init_num = pseudo_randomized_numbers[i]//DIVISIOR_PX_INIT % COUNT_INSTRUMENT
        px_init_change = pseudo_randomized_numbers[i]//DIVISIOR_PX_INIT % 50 * PX_INIT[px_init_num][1] 
        status_num = pseudo_randomized_numbers[i]//DIVISIOR_STATUS%3
        if status_num == 2:
            px_fill_value=0
        elif status_num == 1:
            px_fill_change = pseudo_randomized_numbers[i]//DIVISIOR_PX_FILL%50 * PX_INIT[px_init_num][1]
            px_fill_value=round(PX_INIT[px_init_num][0]+px_init_change - px_fill_change,5)
        else:
            px_fill_value=round(PX_INIT[px_init_num][0]+px_init_change,5)
        if i < ORDER_CREATED_BEFORE_START:
            px_fill_values.extend([0,px_fill_value,px_fill_value])
        elif i < ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
            px_fill_values.extend([0,0,px_fill_value])
        else:
            px_fill_values.extend([0,0,px_fill_value,px_fill_value])
    return px_fill_values

def note_generator(pseudo_randomized_numbers):
    note_values = []
    for i in range(COUNT_ORDERS):
        note_num = pseudo_randomized_numbers[i]//DIVISIOR % COUNT_NOTE
        note_values.extend(copy_element(i,NOTE[note_num]))
    return note_values

def order_generator(pseudo_randomized_numbers):
    id = id_generator(pseudo_randomized_numbers)
    instrument = insturments_generator(pseudo_randomized_numbers)
    px_init = px_init_generator(pseudo_randomized_numbers)
    px_fill = px_fill_generator(pseudo_randomized_numbers)
    side = side_generator(pseudo_randomized_numbers)
    volume_init = volume_init_generator(pseudo_randomized_numbers)
    #volume_fill =
    status = status_generator(pseudo_randomized_numbers)
    #date = 
    note = note_generator(pseudo_randomized_numbers)
    #tag
    orders_list = []
    for i in range(COUNT_RECORDS):
        orders_list.append( [id[i],
                            instrument[i],
                            px_init[i],
                            px_fill[i],
                            side[i],
                            volume_init[i],
                            #volume_fill[i],
                            status[i],
                            #date[i],
                            note[i]
                            #tag[i]
                        ])
    return orders_list

def print_list(list_):
    for i in range(COUNT_RECORDS):
        print(str(list_[i])+'\n')

def main():
    prn = pseudo_generator()
    print_list(order_generator(prn))

main()
