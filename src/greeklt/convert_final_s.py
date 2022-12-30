def convert_final_s(string):
    new_string = ""
    for i, letter in enumerate(string):
        if letter == "σ" and (
            i == len(string) - 1 or string[i + 1] == " " or string[i + 1] == "-"
        ):
            new_string += "ς"
        else:
            new_string += letter
    return new_string
