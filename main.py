import math
from datetime import *
from config import *
from Interfaces import IRecordBuilder,IRecordListFactory
from Gererators import *
from DTO import RecordDTO


class RecordBuilder(IRecordBuilder):
    def __init__(self):
        self.list_values = {}

    def set_id(self):
        id_generator = IdGenerator()
        list_values["Id"] = id_generator.generate()
    def set_instrument(self):
        insturment_generator = InstrumentGenerator()
        list_values["Instrument"] = insturments_generator.generate()
    def set_px_init(self):
        px_init_generator = PxInitGenerator()
        list_values["PxInit"] = px_init_generator.generate()
    def set_px_fill(self):
        px_fill_generator = PxFillGenerator()
        list_values["PxFill"] = px_fill_generator.generate()
    def set_side(self):
        side_generator = SideGenerator()
        list_values["Side"] = side_generator.generate()
    def set_volume_init(self):
        volume_init_generator = VolumeInitGenerator()
        list_values["VolumeInit"] = volume_init_generator.generate()
    def set_volume_fill(self):
        volume_fill_generator = VolumeFillGenerator()
        list_values["VolumeFill"] = volume_fill_generator.generate()
    def set_date(self):
        date_generator = DateGenerator()
        list_values["Date"] = date_generator.generate()
    def set_note(self):
        note_generator = NoteGenerator()
        list_values["Note"] = note_generator.generate()
    def set_status(self):
        status_generator = StatusGenerator()
        list_values["Status"] = status_generator.generate()
    
    
    def get(self):
        records_list = []
        for iter in range(COUNT_RECORDS):
            item = RecordDTO()
            item.id = list_values["Id"][iter]
	        item.instrument = list_values["Instrument"][iter]
            item.px_init = list_values["PxInit"][iter]
            item.volume_init = list_values["VolumeInit"][iter]
            item.side: = list_values["Side"][iter]
            item.px_fill = list_values["PxFill"][iter] 
            item.volume_fill = list_values["VolumeFill"][iter] 
            item.status = list_values["Status"][iter]
            item.date = list_values["Date"][iter]
            item.note = list_values["Note"][iter]
            records_list.append(item)
        return records_list


class RecordListFactory(IRecordListFactory):
    def create():
        builder = RecordBuilder()
        builder.set_id()
        builder.set_instrument()
        builder.set_px_init()
        builder.set_volume_init()
        builder.set_side()
        builder.set_volume_init()
        builder.set_volume_fill()
        builder.set_status()
        builder.set_note()
        builder.set_date()
        builder.get()



def main():
    factory = RecordListFactory()
    records_list = factory.create()

if __name__ == "__main__":
    main()