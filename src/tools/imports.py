from importlib import util
from pathlib import Path
from typing import Any

from constants.paths import SOURCE_PATH


def import_class_from_module(module_name: str, package_name: str, class_name: str) -> type[Any]:
    """
    Import a class from a module.

    :param module_name: Name of the module.
    :param package_name: Name of the package.
    :param class_name: Name of the class.
    :return: The desired class.
    """
    module_path = Path(f'{SOURCE_PATH}/{package_name}/{module_name}.py').resolve()
    spec = util.spec_from_file_location(module_name, str(module_path))
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    try:
        class_ = getattr(module, class_name)
    except AttributeError:
        raise ImportError(f'Class {class_name} not found in module {module_name}')

    return class_
