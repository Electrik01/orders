from Interfaces import IGenerator
import math
from config import *
from datetime import *
from Query import *

class IdGenerator(IGenerator):
    def __init__(self):
        self.random_value = PseudoGenerator.get_random_value(SEED)

    def generate(self):
        id_value = hex(self.random_value)[2:].rjust(10,'0')
        #id_value.extend(CopyElementQuery.invoke(i,id_value))
        self.random_value = PseudoGenerator.get_random_value(self.random_value)
        return id_value

class InstrumentGenerator(IGenerator):
    def __init__(self):
        self.random_value = PseudoGenerator.get_random_value(SEED)
    def generate(self):
        instrument_num = self.random_value//DIVISIOR % COUNT_INSTRUMENT
        self.random_value = PseudoGenerator.get_random_value(self.random_value)
        #insturments_values.extend(CopyElementQuery.invoke(i,INSTRUMENTS[instrument_num]))
        return INSTRUMENTS[instrument_num]

class PxInitGenerator(IGenerator):
    def __init__(self):
        self.random_value = PseudoGenerator.get_random_value(SEED)
    def generate(self):
        px_init_value = PxInitValueQuery.invoke(self.random_value)
        #px_init_values.extend(CopyElementQuery.invoke(i,px_init_value))
        self.random_value = PseudoGenerator.get_random_value(self.random_value)
        return px_init_value

class SideGenerator(IGenerator):
    def __init__(self):
        self.random_value = PseudoGenerator.get_random_value(SEED)
    def generate(self):
        flag = self.random_value//DIVISIOR_SIDE % 2 
        self.random_value = PseudoGenerator.get_random_value(self.random_value)
        if flag == 0:
            return SIDE[0]
        else:
            return SIDE[1]

class PxFillGenerator(IGenerator):
    def __init__(self):
        self.random_value = PseudoGenerator.get_random_value(SEED)
        self.iter = 0
    def generate(self):
        status_num = self.random_value//DIVISIOR_STATUS%3
        px_fill_value = PxFillValueDependencyStatusQuery.invoke(status_num,self.random_value)
        if self.iter < ORDER_CREATED_BEFORE_START:
            px_fill_values = [0,px_fill_value,px_fill_value]
        elif self.iter < ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
            px_fill_values = [0,0,px_fill_value]
        else:
            px_fill_values = [0,0,px_fill_value,px_fill_value]
        self.random_value = PseudoGenerator.get_random_value(self.random_value)
        self.iter+=1
        return px_fill_values

class VolumeInitGenerator(IGenerator):
    def __init__(self):
        self.random_value = PseudoGenerator.get_random_value(SEED)
    def generate(self):
        volume_init_multiplier = math.pow(10,self.random_value%3+3)
        volume_init_value = int(self.random_value//DIVISIOR_VOLUME_INIT * volume_init_multiplier)
        self.random_value = PseudoGenerator.get_random_value(self.random_value)
        return volume_init_value

class NoteGenerator(IGenerator):
    def __init__(self):
        self.random_value = PseudoGenerator.get_random_value(SEED)
    def generate(self):
        note_num = self.random_value//DIVISIOR % COUNT_NOTE
        self.random_value = PseudoGenerator.get_random_value(self.random_value)
        return NOTE[note_num]

class VolumeFillGenerator(IGenerator):
    def __init__(self):
        self.random_value = PseudoGenerator.get_random_value(SEED)
        self.iter = 0
    def generate(self):
        volume_init_multiplier = math.pow(10,self.random_value%3+3)
        volume_init_value = int(self.random_value//DIVISIOR_VOLUME_INIT) * volume_init_multiplier
        status_num = self.random_value//DIVISIOR_STATUS%3
        volume_fill_value = VolumeFillValueDependencyStatus.invoke(
            status_num,volume_init_value,self.random_value
            )
        if self.iter < ORDER_CREATED_BEFORE_START:
            volume_fill_values = [0,volume_fill_value,volume_fill_value]
        elif self.iter < ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
            volume_fill_values = [0,0,volume_fill_value]
        else:
            volume_fill_values = [0,0,volume_fill_value,volume_fill_value]
        self.random_value = PseudoGenerator.get_random_value(self.random_value)
        self.iter+=1
        return volume_fill_values

class DateGenerator(IGenerator):
    def __init__(self):
        self.random_value = PseudoGenerator.get_random_value(SEED)
        self.iter = 0
    def generate(self):
        date_values = []
        num = self.random_value//DIVISIOR
        time_parameters = TimeParametersQuery.invoke(self.random_value,num)
        first_date = datetime(YEAR,MONTH,DAY,time_parameters['hour'],
                                                time_parameters['minute'],
                                                time_parameters['second'],
                                                time_parameters['msec'][0]*1000)
        date_values = DateValueLineQuery.invoke(self.iter,time_parameters,first_date,num)
        self.random_value = PseudoGenerator.get_random_value(SEED)
        self.iter+=1
        return date_values

class StatusGenerator(IGenerator):
    def __init__(self):
        self.random_value = PseudoGenerator.get_random_value(SEED)
        self.iter=0
    def generate(self):
        status_num = self.random_value//DIVISIOR_STATUS%3
        if self.iter < ORDER_CREATED_BEFORE_START:
            status_values = [STATUS[1],STATUS[2][status_num],STATUS[3]]
        elif self.iter < ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
            status_values = [STATUS[0],STATUS[1],STATUS[2][status_num]]
        else:
            status_values = [STATUS[0],STATUS[1],STATUS[2][status_num],STATUS[3]]        
        self.random_value = PseudoGenerator.get_random_value(SEED)
        self.iter+=1        
        return status_values





class PseudoGenerator():
    A = MULTIPLIER
    C = INCREMENT
    M = MODULE
    @staticmethod
    def invoke():
        pseudo_randomized_numbers = []
        seed = SEED
        for i in range(COUNT_ORDERS):
            seed = (seed*MULTIPLIER+INCREMENT)%MODULE
            pseudo_randomized_numbers.append(seed)
        return pseudo_randomized_numbers

    @staticmethod
    def get_random_value(seed):
        return (seed*MULTIPLIER+INCREMENT)%MODULE
