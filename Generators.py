from Interfaces import IGenerator
import math
from datetime import *

class IdGenerator(IGenerator):
    def generate(self):
        id_values = []
        for i in range(COUNT_ORDERS):
            id_value = hex(pseudo_randomized_numbers[i])[2:].rjust(10,'0')
            id_values.extend(copy_element(i,id_value))
        return id_values

class InstrumentGenerator(IGenerator):
    def generate(self):
    insturments_values = []
        for i in range(COUNT_ORDERS):
            instrument_num = pseudo_randomized_numbers[i]//DIVISIOR % COUNT_INSTRUMENT
            insturments_values.extend(copy_element(i,INSTRUMENTS[instrument_num]))
        return insturments_values

class PxInitGenerator(IGenerator):
    def generate(self):
        px_init_values = []
        for i in range(COUNT_ORDERS):
            px_init_value = get_px_init_value(pseudo_randomized_numbers[i])
            px_init_values.extend(copy_element(i,px_init_value))
        return px_init_values

class SideGenerator(IGenerator):
    def generate(self):
        side_values = []
        for i in range(COUNT_ORDERS):
            if pseudo_randomized_numbers[i]//DIVISIOR_SIDE % 2 == 0:
                side_values.extend(copy_element(i,SIDE[0]))
            else:
                side_values.extend(copy_element(i,SIDE[1]))
        return side_values

class PxFillGenerator(IGenerator):
    def generate(self):
        px_fill_values = []
        for i in range(COUNT_ORDERS):
            status_num = pseudo_randomized_numbers[i]//DIVISIOR_STATUS%3
            px_fill_value = get_px_fill_value_dependency_status(status_num,pseudo_randomized_numbers[i])
            if i < ORDER_CREATED_BEFORE_START:
                px_fill_values.extend([0,px_fill_value,px_fill_value])
            elif i < ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
                px_fill_values.extend([0,0,px_fill_value])
            else:
                px_fill_values.extend([0,0,px_fill_value,px_fill_value])
        return px_fill_values

class VolumeInitGenerator(IGenerator):
    def generate(self):
        volume_init_values = []
        for i in range(COUNT_ORDERS):
            volume_init_multiplier = math.pow(10,pseudo_randomized_numbers[i]%3+3)
            volume_init_value = int(pseudo_randomized_numbers[i]//DIVISIOR_VOLUME_INIT * volume_init_multiplier)
            volume_init_values.extend(copy_element(i,volume_init_value))
        return volume_init_values

class NoteGenerator(IGenerator):
    def generate(self):
        note_values = []
        for i in range(COUNT_ORDERS):
            note_num = pseudo_randomized_numbers[i]//DIVISIOR % COUNT_NOTE
            note_values.extend(copy_element(i,NOTE[note_num]))
        return note_values

class VolumeFillGenerator(IGenerator):
    def generate(self):
        volume_fill_values = []
        for i in range(COUNT_ORDERS):
            volume_init_multiplier = math.pow(10,pseudo_randomized_numbers[i]%3+3)
            volume_init_value = int(pseudo_randomized_numbers[i]//DIVISIOR_VOLUME_INIT) * volume_init_multiplier
            status_num = pseudo_randomized_numbers[i]//DIVISIOR_STATUS%3
            volume_fill_value = get_volume_fill_value_dependency_status(
                status_num,volume_init_value,pseudo_randomized_numbers[i]
                )
            if i < ORDER_CREATED_BEFORE_START:
                volume_fill_values.extend([0,volume_fill_value,volume_fill_value])
            elif i < ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
                volume_fill_values.extend([0,0,volume_fill_value])
            else:
                volume_fill_values.extend([0,0,volume_fill_value,volume_fill_value])
        return volume_fill_values

class DateGenerator(IGenerator):
    def generate(self):
        date_values = []
        for i in range(COUNT_ORDERS):
            num = pseudo_randomized_numbers[i]//DIVISIOR
            time_parameters = get_time_parameters(pseudo_randomized_numbers[i],num)
            first_date = datetime(YEAR,MONTH,DAY,time_parameters['hour'],
                                                time_parameters['minute'],
                                                time_parameters['second'],
                                                time_parameters['msec'][0]*1000)
            date_values.extend(get_date_value_line(i,time_parameters,first_date,num))
        return date_values

class StatusGenerator(IGenerator):
    def generate(self):
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






def get_volume_fill_value_dependency_status(status_num,volume_init_value,prn):
    volume_fill_value = [
        int(volume_init_value),
        int(volume_init_value - prn%100*1000),
        0
    ]
    return volume_fill_value[status_num]

def pseudo_generator():
    pseudo_randomized_numbers = []
    seed = SEED
    for i in range(COUNT_ORDERS):
        seed = (seed*MULTIPLIER+INCREMENT)%MODULE
        pseudo_randomized_numbers.append(seed)
    return pseudo_randomized_numbers

def copy_element(iter, value):
    if iter<ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
        return [value]*MIN_COUNT_RECORDS
    else:
        return [value]*MAX_COUNT_RECORDS

def get_px_init_value(prn):
    px_init_num = prn//DIVISIOR_PX_INIT % COUNT_INSTRUMENT
    px_init_change = prn//DIVISIOR_PX_INIT_CHANGE % 100 * PX_INIT[px_init_num][1] #or 100
    px_init_value = round(PX_INIT[px_init_num][0]+px_init_change,5)
    return px_init_value

def get_px_fill_value_dependency_status(status_num,prn):
    px_init_num = prn//DIVISIOR_PX_INIT % COUNT_INSTRUMENT
    px_init_value = get_px_init_value(prn)
    px_fill_change = prn//DIVISIOR_PX_FILL%50 * PX_INIT[px_init_num][1]
    px_fill_value = [
        px_init_value,
        round(px_init_value - px_fill_change,5),
        0
    ]
    return px_fill_value[status_num]

def get_volume_fill_value_dependency_status(status_num,volume_init_value,prn):
    volume_fill_value = [
        int(volume_init_value),
        int(volume_init_value - prn%100*1000),
        0
    ]
    return volume_fill_value[status_num]

def get_time_parameters(prn,num):
    first_time = {
        'hour': num%23,
        'minute': num%60,
        'second': num//10%60,
        'msec': [
            num%1000,
            math.ceil(num*1.1)%1000,
            math.ceil(num*1.2)%1000,
            math.ceil(num*1.3)%1000
        ]    
    } 
    return first_time 

def get_date_value_line(iter,time_parameters,first_date,num):
    date_value = [
        first_date.strftime(DATE_FORMAT)[:-3],
        (first_date + timedelta(milliseconds = int(num % 10)*1000 + time_parameters['msec'][1])).strftime(DATE_FORMAT)[:-3],
        (first_date + timedelta(milliseconds = math.ceil(num % 10 + 1)*1000 + time_parameters['msec'][2])).strftime(DATE_FORMAT)[:-3],                
        (first_date + timedelta(milliseconds = int(num % 10 + 2)*1000 + time_parameters['msec'][3])).strftime(DATE_FORMAT)[:-3]
    ]
    if iter<ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
        return date_value[:-1]
    else:
        return date_value
