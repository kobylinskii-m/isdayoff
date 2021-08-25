from enum import IntEnum
from typing_extensions import TypedDict


class ServiceNotRespond(Exception):
    pass

class DataError(Exception):
    pass

class ParamsApi(TypedDict):
    locale: str
    pre: bool
    sd: bool
    covid: bool

class DateType(IntEnum):
    WORKING = 0
    NOT_WORKING = 1
    SHORTENED = 2
    WORKING_DAY = 4
