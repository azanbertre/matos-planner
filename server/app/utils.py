import string
import random

from datetime import datetime
from bson import ObjectId
from pymongo.database import Database


def get_timestamp() -> float:
    """ Return utc now timestamp

        @return : timestamp
    """

    return datetime.utcnow().timestamp()

def parse_timestamp(ts: float) -> datetime:
    """ Return timestamp parsed to datetime

        @param ts : timestamp \n
        @return : datetime
    """

    return datetime.utcfromtimestamp(ts)

