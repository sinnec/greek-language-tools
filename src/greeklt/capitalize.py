from .remove_accentuation import remove_accentuation


def capitalize(string: str):
    return remove_accentuation(string).upper()
