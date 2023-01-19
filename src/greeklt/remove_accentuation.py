def remove_accentuation(string: str, modifier=0):
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
    dieresis_reverse = {"ϊ": "ι", "ϋ": "υ"}
    new_string = ""
    prev_char = 0
    for c in string:
        char = c
        if c in accents.keys():
            char = accents[c]
        if modifier == 0:
            if c in dieresis.keys() and prev_char in ("ά", "ό", "έ"):
                char = dieresis[c]
        if modifier == 1:  # Remove dieresis
            if c in dieresis_reverse.keys():
                char = dieresis_reverse[c]
        prev_char = c
        new_string += char
    return new_string
