from typing import List, Literal
from ..tables.table import Table
from ..base.entity import IEntity


class Relation(IEntity):
    """The representation of a table relationship."""

    _letf_table: str

    @property
    def letf_table(self) -> str:
        """The left table name on source."""
        return self._letf_table

    _rigth_table: str

    @property
    def rigth_table(self) -> str:
        """The rigth table name on source."""
        return self._rigth_table

    _direction: Literal["Many_to_one", "One_to_many", "One_to_one", "Many_to_many"]

    @property
    def direction(self) -> str:
        """The direction of the relation."""
        return self._direction
