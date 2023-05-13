from pydantic import BaseModel


class Iris (BaseModel):
    Id: int
    SepalLengthCm: int
    SepalWidthCm: int
    PetalLengthCm: int
    PetalWidthCm: int
    Species: str