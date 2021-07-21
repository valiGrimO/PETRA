import importlib
from pathlib import Path
import sys


print("[PETRA] Setup: Materials")

material_filepaths = Path(__file__).parent.glob("[!_]*.py")
material_names = list(map(lambda x: x.stem, material_filepaths))
system_modules = sys.modules

for name in material_names:
    print(f"[PETRA] Setup: Materials: {name}")
    module_name = f"{__name__}.{name}"
    if module_name not in system_modules:
        importlib.import_module("." + name, __name__)
    else:
        importlib.reload(system_modules[module_name])
