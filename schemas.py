from typing import Optional

from pydantic import BaseModel

class Passenger(BaseModel):

    Pclass:int
    sex:str

    age:optional[float]=None
    fare:optional[float]=None
