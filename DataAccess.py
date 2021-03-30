from config import *


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