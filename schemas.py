from typing import Optional

from pydantic import BaseModel

class passenger(BaseModel):

    Pclass:int
    sex:str

    age:optional[float]=none
    fare:optional[float]=none
