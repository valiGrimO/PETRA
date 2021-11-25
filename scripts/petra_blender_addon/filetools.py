"""
Tools to read and save files.
"""

from .lib import yaml


def read(filepath):
    with open(filepath) as file:
        return file.read()


def read_yaml(filepath):
    with open(filepath) as file:
        return yaml.safe_load(file)


def save(text, filepath):
    with open(filepath, "w") as file:
        return file.write(text)


def save_yaml(data, filepath, allow_unicode=True):
    with open(filepath, "w") as file:
        return yaml.dump(data, file, allow_unicode=allow_unicode, sort_keys=False)
