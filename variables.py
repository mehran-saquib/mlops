from pydantic import BaseModel

class columns(BaseModel):
    property_type:str
    room_type:str
    accommodates:int
    bathrooms:int
    bed_type:str
    cancellation_policy:str
    cleaning_fee:str
    city:str
    instant_bookable:str 
    bedrooms:int
    beds:int