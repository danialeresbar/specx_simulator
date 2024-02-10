import importlib

from typing import Any


def import_class_from_module(module_name: str, class_name: str) -> type[Any]:
    """
    Import a class from a module.

    :param module_name: Name of the module.
    :param class_name: Name of the class.
    :return: The desired class.
    """
    try:
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
    except AttributeError:
        raise ImportError(f'Class {class_name} not found in module {module_name}')
    except ModuleNotFoundError:
        raise ImportError(f'Module {module_name} not found')
    else:
        return class_
