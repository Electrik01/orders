from Interfaces import IGenerator
import math
from config import *
from datetime import *
from Query import *

class IdGenerator(IGenerator):
    def __init__(self):
        self.pseudo_randomized_numbers = PseudoGenerator.invoke()

    def generate(self):
        id_values = []
        for i in range(COUNT_ORDERS):
            id_value = hex(self.pseudo_randomized_numbers[i])[2:].rjust(10,'0')
            id_values.extend(CopyElementQuery.invoke(i,id_value))
        return id_values

class InstrumentGenerator(IGenerator):
    def __init__(self):
        self.pseudo_randomized_numbers = PseudoGenerator.invoke()
    def generate(self):
        insturments_values = []
        for i in range(COUNT_ORDERS):
            instrument_num = self.pseudo_randomized_numbers[i]//DIVISIOR % COUNT_INSTRUMENT
            insturments_values.extend(CopyElementQuery.invoke(i,INSTRUMENTS[instrument_num]))
        return insturments_values

class PxInitGenerator(IGenerator):
    def __init__(self):
        self.pseudo_randomized_numbers = PseudoGenerator.invoke()
    def generate(self):
        px_init_values = []
        for i in range(COUNT_ORDERS):
            px_init_value = PxInitValueQuery.invoke(self.pseudo_randomized_numbers[i])
            px_init_values.extend(CopyElementQuery.invoke(i,px_init_value))
        return px_init_values

class SideGenerator(IGenerator):
    def __init__(self):
        self.pseudo_randomized_numbers = PseudoGenerator.invoke()
    def generate(self):
        side_values = []
        for i in range(COUNT_ORDERS):
            if self.pseudo_randomized_numbers[i]//DIVISIOR_SIDE % 2 == 0:
                side_values.extend(CopyElementQuery.invoke(i,SIDE[0]))
            else:
                side_values.extend(CopyElementQuery.invoke(i,SIDE[1]))
        return side_values

class PxFillGenerator(IGenerator):
    def __init__(self):
        self.pseudo_randomized_numbers = PseudoGenerator.invoke()
    def generate(self):
        px_fill_values = []
        for i in range(COUNT_ORDERS):
            status_num = self.pseudo_randomized_numbers[i]//DIVISIOR_STATUS%3
            px_fill_value = PxFillValueDependencyStatusQuery.invoke(status_num,self.pseudo_randomized_numbers[i])
            if i < ORDER_CREATED_BEFORE_START:
                px_fill_values.extend([0,px_fill_value,px_fill_value])
            elif i < ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
                px_fill_values.extend([0,0,px_fill_value])
            else:
                px_fill_values.extend([0,0,px_fill_value,px_fill_value])
        return px_fill_values

class VolumeInitGenerator(IGenerator):
    def __init__(self):
        self.pseudo_randomized_numbers = PseudoGenerator.invoke()
    def generate(self):
        volume_init_values = []
        for i in range(COUNT_ORDERS):
            volume_init_multiplier = math.pow(10,self.pseudo_randomized_numbers[i]%3+3)
            volume_init_value = int(self.pseudo_randomized_numbers[i]//DIVISIOR_VOLUME_INIT * volume_init_multiplier)
            volume_init_values.extend(CopyElementQuery.invoke(i,volume_init_value))
        return volume_init_values

class NoteGenerator(IGenerator):
    def __init__(self):
        self.pseudo_randomized_numbers = PseudoGenerator.invoke()
    def generate(self):
        note_values = []
        for i in range(COUNT_ORDERS):
            note_num = self.pseudo_randomized_numbers[i]//DIVISIOR % COUNT_NOTE
            note_values.extend(CopyElementQuery.invoke(i,NOTE[note_num]))
        return note_values

class VolumeFillGenerator(IGenerator):
    def __init__(self):
        self.pseudo_randomized_numbers = PseudoGenerator.invoke()
    def generate(self):
        volume_fill_values = []
        for i in range(COUNT_ORDERS):
            volume_init_multiplier = math.pow(10,self.pseudo_randomized_numbers[i]%3+3)
            volume_init_value = int(self.pseudo_randomized_numbers[i]//DIVISIOR_VOLUME_INIT) * volume_init_multiplier
            status_num = self.pseudo_randomized_numbers[i]//DIVISIOR_STATUS%3
            volume_fill_value = VolumeFillValueDependencyStatus.invoke(
                status_num,volume_init_value,self.pseudo_randomized_numbers[i]
                )
            if i < ORDER_CREATED_BEFORE_START:
                volume_fill_values.extend([0,volume_fill_value,volume_fill_value])
            elif i < ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
                volume_fill_values.extend([0,0,volume_fill_value])
            else:
                volume_fill_values.extend([0,0,volume_fill_value,volume_fill_value])
        return volume_fill_values

class DateGenerator(IGenerator):
    def __init__(self):
        self.pseudo_randomized_numbers = PseudoGenerator.invoke()
    def generate(self):
        date_values = []
        for i in range(COUNT_ORDERS):
            num = self.pseudo_randomized_numbers[i]//DIVISIOR
            time_parameters = TimeParametersQuery.invoke(self.pseudo_randomized_numbers[i],num)
            first_date = datetime(YEAR,MONTH,DAY,time_parameters['hour'],
                                                time_parameters['minute'],
                                                time_parameters['second'],
                                                time_parameters['msec'][0]*1000)
            date_values.extend(DateValueLineQuery.invoke(i,time_parameters,first_date,num))
        return date_values

class StatusGenerator(IGenerator):
    def __init__(self):
        self.pseudo_randomized_numbers = PseudoGenerator.invoke()
    def generate(self):
        status_values = []
        for i in range(COUNT_ORDERS):
            status_num = self.pseudo_randomized_numbers[i]//DIVISIOR_STATUS%3
            if i < ORDER_CREATED_BEFORE_START:
                status_values.extend([STATUS[1],STATUS[2][status_num],STATUS[3]])
            elif i < ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
                status_values.extend([STATUS[0],STATUS[1],STATUS[2][status_num]])
            else:
                status_values.extend([STATUS[0],STATUS[1],STATUS[2][status_num],STATUS[3]])
        return status_values





class PseudoGenerator():
    @staticmethod
    def invoke():
        pseudo_randomized_numbers = []
        seed = SEED
        for i in range(COUNT_ORDERS):
            seed = (seed*MULTIPLIER+INCREMENT)%MODULE
            pseudo_randomized_numbers.append(seed)
        return pseudo_randomized_numbers

