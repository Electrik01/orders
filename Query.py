from constant import *
import math
from datetime import *

class DateValueLineQuery():
    @staticmethod
    def invoke(iter,time_parameters,first_date,num):
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

class TimeParametersQuery():
    @staticmethod
    def invoke(prn,num):
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

class TagsList():
    @staticmethod
    def invoke(prn):
        tags = []
        for iter in range(TAGS_COUNT):
            num = prn//DIVIDER_TAG*pow(10,iter)
            if num % (iter+3) == 0:
                tags.append(TAG[iter])
        return tags
        

class PxFillValueDependencyStatusQuery():
    @staticmethod
    def invoke(status_num,prn):
        px_init_num = prn//DIVIDER_PX_INIT % COUNT_INSTRUMENT
        px_init_value = PxInitValueQuery.invoke(prn)
        px_fill_change = prn//DIVIDER_PX_FILL%50 * PX_INIT[px_init_num][1]
        px_fill_value = [
            px_init_value,
            round(px_init_value - px_fill_change,5),
            0
        ]
        return px_fill_value[status_num]

class PxInitValueQuery():
    @staticmethod
    def invoke(prn):
        px_init_num = prn//DIVIDER_PX_INIT % COUNT_INSTRUMENT
        px_init_change = prn//DIVIDER_PX_INIT_CHANGE % 100 * PX_INIT[px_init_num][1] 
        px_init_value = round(PX_INIT[px_init_num][0]+px_init_change,5)
        return px_init_value
        
class CopyElementQuery():
    @staticmethod
    def invoke(iter,value):
        if iter<ORDER_CREATED_BEFORE_START+ORDER_DONE_AFTER_FINISH:
            return [value]*MIN_COUNT_RECORDS
        else:
            return [value]*MAX_COUNT_RECORDS

class VolumeFillValueDependencyStatus():
    @staticmethod
    def invoke(status_num,volume_init_value,prn):
        volume_fill_value = [
            int(volume_init_value),
            int(volume_init_value - prn%100*1000),
            0
        ]
        return volume_fill_value[status_num]