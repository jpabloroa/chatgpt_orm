from typing import Dict
from .entity import IEntity


class IDataType(IEntity):
    """Describes the data type."""

    _name: str

    @property
    def name(self) -> str:
        """The name of the datatype."""
        return self._name

    _names_in_sources: Dict[str, str]

    @property
    def names_in_sources(self) -> str:
        """A key value object, the key is the engine and the value is the name of the data type."""
        return self._names_in_sources
