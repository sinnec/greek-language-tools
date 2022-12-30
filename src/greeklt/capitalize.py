from .remove_accentuation import remove_accentuation


def capitalize(string):
    return remove_accentuation(string).upper()
