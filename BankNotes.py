from pydantic import BaseModel

# this is a POJO defines in which way your input should come and what are the expected params
class BankNote(BaseModel) :
    variance : float
    skewness : float
    curtosis : float
    entropy : float

    