from ..base.entity import IEntity


class Model(IEntity):
    """The representation of a data model."""

    _name: str

    @property
    def name(self) -> str:
        """Name of the model."""
        return self._name

    _description: str

    @property
    def description(self) -> str:
        """Decription of the model."""
        return self._description

    _tables: str

    @property
    def tables(self):
        """A list of the model tables."""
        return self._tables

    _relationships: str

    @property
    def relationships(self):
        """A list of the model relationships."""
        return self._relationships
