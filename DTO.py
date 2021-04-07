

class RecordDTO():
    id: str 
    instrument: str 
    px_init: float
    volume_init: int
    side: str  
    px_fill: float 
    volume_fill: int 
    status: str 
    date: str 
    note: str 
    tags: str 

class OrderDTO:
    id: str
    instrument: str 
    px_init: float
    volume_init: int
    side: str  
    px_fill: list 
    volume_fill: list 
    status: list 
    date: list 
    note: str 
    tags: str 