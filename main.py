import math
from datetime import *
from config import *
from Interfaces import IRecordBuilder,IRecordListFactory
from Generators import *
from DTO import RecordDTO


class RecordBuilder(IRecordBuilder):
    def __init__(self):
        self.list_values = {}

    def set_id(self):
        id_generator = IdGenerator()
        self.list_values["Id"] = id_generator.generate()
    def set_instrument(self):
        insturment_generator = InstrumentGenerator()
        self.list_values["Instrument"] = insturment_generator.generate()
    def set_px_init(self):
        px_init_generator = PxInitGenerator()
        self.list_values["PxInit"] = px_init_generator.generate()
    def set_px_fill(self):
        px_fill_generator = PxFillGenerator()
        self.list_values["PxFill"] = px_fill_generator.generate()
    def set_side(self):
        side_generator = SideGenerator()
        self.list_values["Side"] = side_generator.generate()
    def set_volume_init(self):
        volume_init_generator = VolumeInitGenerator()
        self.list_values["VolumeInit"] = volume_init_generator.generate()
    def set_volume_fill(self):
        volume_fill_generator = VolumeFillGenerator()
        self.list_values["VolumeFill"] = volume_fill_generator.generate()
    def set_date(self):
        date_generator = DateGenerator()
        self.list_values["Date"] = date_generator.generate()
    def set_note(self):
        note_generator = NoteGenerator()
        self.list_values["Note"] = note_generator.generate()
    def set_status(self):
        status_generator = StatusGenerator()
        self.list_values["Status"] = status_generator.generate()
    
    
    def get(self):
        records_list = []
        for iter in range(COUNT_RECORDS):
            item = RecordDTO()
            item.id = self.list_values["Id"][iter]
            item.instrument = self.list_values["Instrument"][iter]
            item.px_init = self.list_values["PxInit"][iter]
            item.volume_init = self.list_values["VolumeInit"][iter]
            item.side = self.list_values["Side"][iter]
            item.px_fill = self.list_values["PxFill"][iter] 
            item.volume_fill = self.list_values["VolumeFill"][iter] 
            item.status = self.list_values["Status"][iter]
            item.date = self.list_values["Date"][iter]
            item.note = self.list_values["Note"][iter]
            records_list.append(item)
        return records_list


class RecordListFactory(IRecordListFactory):
    def __init__(self):
        self.builder = RecordBuilder()
    def create(self):
        self.builder.set_id()
        self.builder.set_instrument()
        self.builder.set_px_init()
        self.builder.set_px_fill()
        self.builder.set_volume_init()
        self.builder.set_side()
        self.builder.set_volume_init()
        self.builder.set_volume_fill()
        self.builder.set_status()
        self.builder.set_note()
        self.builder.set_date()
        return self.builder.get()




def main():
    factory = RecordListFactory()
    records_list = factory.create()
    

if __name__ == "__main__":
    main()