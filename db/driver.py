from . import Villager
from typing import Dict, List, Union
from sqlalchemy.orm import Session


def retrieve_filter(s: Session,
                    **filters: Dict[str, Union[str, int]]) -> List[Villager]:
    """Provided a list of filters, return the query from the provided session

    Args:
        s (Session): [The SQLAlchemy session we are pulling from]

    Returns:
        List[Villager]: [The villagers who fit the expected criteria]
    """
    q = s.query(Villager)
    if len(filters) != 0:
        q = q.filter_by(**filters)
    return q.all()
