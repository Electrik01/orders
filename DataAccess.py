from config import *
from DTO import *
import time
class OrderRepository():
    def __init__(self, connectionString):
        self.connectionString = connectionString

    def Add(self,_list):
        f = open(self.connectionString, 'w')
        for i in range(len(_list)):
            f.write(Map.RecordToSql(_list[i])+'\n')

class Map():
    @staticmethod
    def RecordToSql(item):
        return DATE_FORMAT_FOR_MYSQL.format(   
                id=item.id,
                instrument=item.instrument,
                px_init=item.px_init,
                px_fill=item.px_fill,
                side=item.side,
                volume_init=item.volume_init,
                volume_fill=item.volume_fill,
                status=item.status,
                date=item.date,
                note=item.note
                )
    @staticmethod
    def OrderToRecord(item:OrderDTO):
        records = []
        for iter in range(len(item.status)):
            record = RecordDTO()
            record.id = item.id
            record.instrument = item.instrument
            record.px_init = item.px_init
            record.px_fill = item.px_fill[iter]
            record.side = item.side
            record.volume_init = item.volume_init
            record.volume_fill = item.volume_fill[iter]
            record.note = item.note
            record.status = item.status[iter]
            record.date = item.date[iter]
            records.append(record)
        return records