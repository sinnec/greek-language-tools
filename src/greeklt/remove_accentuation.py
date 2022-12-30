def remove_accentuation(string):
    accents = {
        "ά": "α",
        "έ": "ε",
        "ή": "η",
        "ί": "ι",
        "ΐ": "ϊ",
        "ό": "ο",
        "ύ": "υ",
        "ώ": "ω",
        "Ά": "Α",
        "Έ": "Ε",
        "Ή": "Η",
        "Ί": "Ι",
        "Ό": "Ο",
        "Ύ": "Υ",
        "Ώ": "Ω",
    }
    dieresis = {"ι": "ϊ", "υ": "ϋ"}
    new_string = ""
    prev_char = 0
    for c in string:
        char = c
        if c in accents.keys():
            char = accents[c]
        if c in dieresis.keys() and prev_char in ("ά", "ό", "έ"):
            char = dieresis[c]
        prev_char = c
        new_string += char
    return new_string
