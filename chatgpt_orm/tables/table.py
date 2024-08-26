from typing import List, Optional
from ..column.column import Column
from .table_alias import TableAlias
from ..base.entity import IEntity
from .table_category import TableCategory


class Table(IEntity):
    """Representation of a table."""

    _display_name: str

    @property
    def display_name(self) -> str:
        """Display name of the table."""
        return self._display_name

    _source_name: str

    @property
    def source_name(self) -> str:
        """Name of the table in source, only used for queries."""
        return self._source_name

    _columns: List[Column]

    @property
    def column(self) -> List[Column]:
        """A list of the table columns."""
        return self._columns

    def get_columns(self) -> List[Column]:
        """Get the table columns."""
        return self._columns

    def get_column(self, column_name) -> Optional[Column]:
        """Get a specific column by the name."""
        return next(
            (column for column in self.get_columns() if column.name == column_name),
            None,
        )

    _aliases: List[TableAlias]

    @property
    def aliases(self) -> List[TableAlias]:
        """A list of aliases for the column."""
        return self.aliases

    _description: str

    @property
    def description(self) -> str:
        """Decription of the column content."""
        return self._description

    _categories: List[TableCategory]

    @property
    def categories(self) -> List[TableCategory]:
        """A list of the categories of the column."""
        return self._categories
