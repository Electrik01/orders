from abc import ABC,abstractmethod

def IRepository(ABC):
    @abstractmethod
    def Add(self, items):
        pass
    @abstractmethod
    def Get(self):
        pass

def IGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

def IRecordListFactory(ABC):
    @abstractmethod
    def create(self):
        pass

def IRecordBuilder(ABC):
    @abstractmethod
    def set_id(self):
        pass
    @abstractmethod
    def set_instrument(self):
        pass
    @abstractmethod
    def set_px_init(self):
        pass
    @abstractmethod
    def set_px_fill(self):
        pass
    @abstractmethod
    def set_side(self):
        pass
    @abstractmethod
    def set_volume_init(self):
        pass
    @abstractmethod
    def set_volume_fill(self):
        pass
    @abstractmethod
    def set_date(self):
        pass
    @abstractmethod
    def set_note(self):
        pass
    @abstractmethod
    def set_tags(self):
        pass
    @abstractmethod
    def get(self):
        pass