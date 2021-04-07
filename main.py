import math
from datetime import *
from constant import *
from Interfaces import *
from Generators import *
from DTO import OrderDTO
from DataAccess import *
from config import Config
class OrderBuilder(IOrderBuilder):
    def __init__(self):
        self.id_generator = IdGenerator()
        self.instrument_generator = InstrumentGenerator()
        self.px_init_generator = PxInitGenerator()
        self.px_fill_generator = PxFillGenerator()
        self.side_generator = SideGenerator()
        self.volume_init_generator = VolumeInitGenerator()
        self.volume_fill_generator = VolumeFillGenerator()
        self.date_generator = DateGenerator()
        self.note_generator = NoteGenerator()
        self.tag_generator = TagGenerator()
        self.status_generator = StatusGenerator()
        self.orderDTO = OrderDTO()

    def set_id(self):
        self.orderDTO.id = self.id_generator.generate()
    def set_instrument(self):
        self.orderDTO.instrument = self.instrument_generator.generate()
    def set_px_init(self):
        self.orderDTO.px_init = self.px_init_generator.generate()
    def set_px_fill(self):
        self.orderDTO.px_fill = self.px_fill_generator.generate()
    def set_side(self):
        self.orderDTO.side = self.side_generator.generate()
    def set_volume_init(self):
        self.orderDTO.volume_init = self.volume_init_generator.generate()
    def set_volume_fill(self):
        self.orderDTO.volume_fill = self.volume_fill_generator.generate()
    def set_date(self):
        self.orderDTO.date = self.date_generator.generate()
    def set_tags(self):
        self.orderDTO.tags = self.tag_generator.generate()
    def set_note(self):
        self.orderDTO.note = self.note_generator.generate()
    def set_status(self):
        self.orderDTO.status = self.status_generator.generate()
    
    
    def get(self):
        return self.orderDTO


class OrderFactory(IOrderFactory):
    def __init__(self):
        self.builder = OrderBuilder()
        
    def create(self):
        self.builder.set_id()
        self.builder.set_instrument()
        self.builder.set_px_init()
        self.builder.set_px_fill()
        self.builder.set_volume_init()
        self.builder.set_side()
        self.builder.set_volume_fill()
        self.builder.set_status()
        self.builder.set_note()
        self.builder.set_date()
        self.builder.set_tags()
        return self.builder.get()




def main():
    config = Config.get()
    records = []
    factory = OrderFactory()
    for iter in range(config["GENERATOR"]["count_orders"]):
        records.extend(Map.OrderToRecord(factory.create()))
    rep = OrderRepository(config["MySQL"])
    rep.AddToFile(records,config["PATH"]["path_to_file"])
    

if __name__ == "__main__":
    main()