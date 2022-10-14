import inspect
from typing import Any, get_type_hints

from pydantic import BaseModel, create_model
from starlite import PluginProtocol


class TypedDictPlugin(PluginProtocol[dict]):
    """The class for which we create a plugin.

    For example, could be a base ORM class such as "Model" or "Document"
    etc.
    """

    def __init__(self) -> None:
        """_"""
        self._to_pydantic_class_counter = 0

    def to_pydantic_model_class(self, model_class: type[dict], **kwargs: Any) -> type[BaseModel]:
        """Given a model_class, convert it to a subclass of the pydantic
        BaseModel."""
        pydantic_class = create_model(  # type:ignore[call-overload]
            f"{model_class.__name__}_{self._to_pydantic_class_counter}",
            **{k: (v, ...) for k, v in get_type_hints(model_class).items()},
        )
        self._to_pydantic_class_counter += 1
        return pydantic_class  # type:ignore[no-any-return]

    @staticmethod
    def is_plugin_supported_type(value: Any) -> bool:  # type:ignore[override]
        """Given a value of indeterminate type, determine if this value is
        supported by the plugin by returning a bool."""
        return bool(inspect.isclass(value) and issubclass(value, dict) and get_type_hints(value)) or isinstance(
            value, dict
        )

    def from_pydantic_model_instance(self, model_class: type[dict], pydantic_model_instance: BaseModel) -> dict:
        """Given an instance of a pydantic model created using a plugin's
        'to_pydantic_model_class', return an instance of the class from which
        that pydantic model has been created.

        This class is passed in as the 'model_class' kwarg.
        """
        return pydantic_model_instance.dict()

    def to_dict(self, model_instance: dict) -> dict[str, Any]:
        """Given an instance of a model supported by the plugin, return a
        dictionary of serializable values."""
        return model_instance

    def from_dict(self, model_class: type[dict], **kwargs: Any) -> dict:
        """Given a class supported by this plugin and a dict of values, create
        an instance of the class."""
        return kwargs
