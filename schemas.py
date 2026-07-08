from typing import Optional

from pydantic import BaseModel

class passenger(BaseModel):

    Pclass:int
    sex:str

    age:optional[float]=None
    fare:optional[float]=None
