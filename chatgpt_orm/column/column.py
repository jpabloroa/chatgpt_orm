from typing import Union, List
from .column_alias import ColumnAlias
from ..base.entity import IEntity
from ..base.data_type import IDataType
from .column_category import ColumnCategory


class Column(IEntity):
    """Representation of a column."""

    _display_name: str

    @property
    def display_name(self) -> str:
        """Display name of the column."""
        return self._display_name

    _source_name: str

    @property
    def source_name(self) -> str:
        """Name of the column in source, only used for queries."""
        return self._source_name

    _data_type: List[IDataType]

    @property
    def data_type(self) -> List[IDataType]:
        """Data type of the column."""
        return self._data_type

    _aliases: List[ColumnAlias]

    @property
    def aliases(self) -> List[ColumnAlias]:
        """A list of aliases for the column."""
        return self.aliases

    _description: str

    @property
    def description(self) -> str:
        """Decription of the column content."""
        return self._description

    _categories: List[ColumnCategory]

    @property
    def categories(self) -> List[ColumnCategory]:
        """A list of the categories of the column."""
        return self._categories
