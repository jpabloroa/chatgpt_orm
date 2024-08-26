import json
import inspect
from typing import Any, Dict, Union


class IEntity:
    """The base entity class."""

    @classmethod
    def get_class_properties(cls) -> Dict[str, Any]:
        """Get all the properties of the class (with @property decorator)."""
        members = inspect.getmembers(cls, predicate=inspect.isfunction)
        property_methods = {}

        for name, method in members:
            if isinstance(getattr(cls, name), property):
                property_methods[name] = method

        return property_methods

    @classmethod
    def get_class_docs(cls) -> Dict[str, str]:
        """Get docstrings of all properties and their setters in the given class."""
        property_methods = cls._get_property_methods()
        property_docs = {}

        for name, method in property_methods.items():
            prop = getattr(cls, name)
            """ For a 2nd version to insert feature
            getter_doc = prop.fget.__doc__ if prop.fget else None
            setter_doc = prop.fset.__doc__ if prop.fset else None
            property_docs[name] = {
                'getter': getter_doc,
                'setter': setter_doc
            }
            """
            doc = prop.fget.__doc__ if prop.fget else None
            property_docs[name] = doc

        return property_docs

    def __init__(self) -> None:
        pass

    def set(self, property_name: Union[str, Dict[str, str]], value: Any) -> None:
        """The main class setter."""
        if type(property_name) == str:
            setattr(self, f"_{property_name}", value)
        elif type(property_name) == Dict[str, str]:
            for key, value in property_name.items():
                setattr(self, f"_{key}", value)

    def to_dict(self) -> Dict[str, Any]:
        """Get the class values as dictionary."""
        property_methods = self.__class__.get_class_properties()
        property_values = {}

        for name, method in property_methods.items():
            prop = getattr(self.__class__, name)
            current_value = prop.fget(self) if prop.fget else None
            property_values[name] = current_value

        return property_values

    def to_json(self) -> str:
        """Retrieve a json representation of the class."""
        return json.dumps(self.to_dict())
