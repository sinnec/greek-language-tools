def greek_transliteration(string: str):
    eng = "abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ"
    el = "αβψδεφγηιξκλμνοπρστθωςχυζΑΒΨΔΕΦΓΗΙΞΚΛΜΝΟΠΡΣΤΘΩςΧΥΖ"
    new_string = ""
    for i in string:
        if i in eng:
            new_string += el[eng.index(i)]
        else:
            new_string += i
    return new_string
