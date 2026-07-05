from typing import List

from pydantic import BaseModel

class Sonar(BaseModel):
    features : List[float]

    class Config:
        form_attributes = True
