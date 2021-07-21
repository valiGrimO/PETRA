import importlib


modules = ["initial", "materials", "compositing"]


def build():
    """Build the initial PETRA Setup."""
    globals_dict = globals()
    is_first_import = "initial" not in globals_dict

    for module in modules:
        if is_first_import:
            importlib.import_module("." + module, __name__)
        else:
            importlib.reload(globals_dict[module])
