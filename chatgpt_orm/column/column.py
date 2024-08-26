from typing import Union, List
from .column_alias import IColumnAlias
from ..base.entity import IEntity
from ..base.data_type import IDataType
from .column_category import IColumnCategory


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

    _aliases: List[IColumnAlias]

    @property
    def aliases(self) -> List[IColumnAlias]:
        """A list of aliases for the column."""
        return self.aliases

    _description: str

    @property
    def description(self) -> str:
        """Decription of the column content."""
        return self._description

    _categories: List[IColumnCategory]

    @property
    def categories(self) -> List[IColumnCategory]:
        """A list of the categories of the column."""
        return self._categories
