from typing import Any, Dict
from .entity import IEntity


class ICategory(IEntity):

    _name: str

    @property
    def name(self) -> str:
        """Name of the category."""
        return self._name

    _description: str

    @property
    def description(self) -> str:
        """Decription of the category."""
        return self._description

    def to_dict(self) -> Dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self._name or self.__class__.__name__[: -len("Category")],
        }
