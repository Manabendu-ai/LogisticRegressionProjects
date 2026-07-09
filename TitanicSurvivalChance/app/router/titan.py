from fastapi import APIRouter
from ..schemas import Titan
from ..service import make_prediction

router = APIRouter(
    prefix="/titan",
    tags=['prediction']
)

@router.post("/predict")
def predict(titan_data : Titan):
    op = make_prediction(titan_data.features)
    if op[0] == 1:
        result = "Survived"
    else:
        result = "Not Survived"

    return {
        "Prediction" : {
            "Passenger: " : result
        }
    }
