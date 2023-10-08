from dataclasses import dataclass
from typing import Optional, List
from datetime import date




@dataclass
class AddDevice:
    name:str
    status:bool

@dataclass
class UpdateDevice:
    device_id:int
    name: str
    status:bool

@dataclass
class AddDevice:
    device_id:int
    name: str
    status:bool


# @dataclass
# class UpdateProduct:
#     name: str
#     price: int
