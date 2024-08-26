from typing import Any, Dict
from .entity import IEntity


class IAlias(IEntity):

    _name: str

    @property
    def name(self) -> str:
        """Name of the alias."""
        return self._name

    _order: int

    @property
    def order(self) -> int:
        """The order of priority of the alias in search."""
        return self._order

    def to_dict(self) -> Dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self._name or self.__class__.__name__[: -len("Alias")],
        }
