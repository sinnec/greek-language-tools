def greek_transliteration(string: str):
    eng = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    el = "αβψδεφγηιξκλμνοπ;ρστθωςχυζΑΒΨΔΕΦΓΗΙΞΚΛΜΝΟΠ:ΡΣΤΘΩςΧΥΖ"
    diaresis = {"i": "ΐ", "y": "ΰ"}
    accent = {"a": "ά", "e": "έ", "h": "ή", "i": "ί", "y": "ύ", "v": "ώ"}
    diaresis_accent = {"i": "ΐ", "y": "ΰ"}

    new_string = ""
    for i, letter in enumerate(string):
        if letter in eng:
            if i != len(string) - 1 and letter == "W":
                if string[i + 1] in diaresis_accent.keys():
                    new_string += diaresis_accent[string[i + 1]]
                else:
                    new_string += el[eng.index(letter)]
            elif (string[i - 1] == "W" and letter in diaresis.keys()) or (
                string[i - 1] in (";", ":") and letter in accent.keys()
            ):
                continue
            else:
                new_string += el[eng.index(letter)]
        elif letter in (";", ":"):
            if letter == ";":
                new_string += accent[string[i + 1]]
            else:
                new_string += diaresis[string[i + 1]]
        else:
            new_string += letter
    return new_string
