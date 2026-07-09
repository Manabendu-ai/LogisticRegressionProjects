from pydantic import BaseModel

class Titan(BaseModel):
    features : list[float]

    class Config:
        form_attributes = True