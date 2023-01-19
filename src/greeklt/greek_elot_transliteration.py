def greek_elot_transliteration(string):
    from remove_accentuation import remove_accentuation
#    reference_string = string
    string = remove_accentuation(string, 1)
    lowercase = {
        'α': 'a',
        'β': 'v',
        'γ': 'g',
        'δ': 'd',
        'ε': 'e',
        'ζ': 'z',
        'η': 'i',
        'θ': 'th',
        'ι': 'i',
        'κ': 'k',
        'λ': 'l',
        'μ': 'm',
        'ν': 'n',
        'ξ': 'x',
        'ο': 'o',
        'π': 'p',
        'ρ': 'r',
        'σ': 's',
        'τ': 't',
        'υ': 'y',
        'φ': 'f',
        'χ': 'ch',
        'ψ': 'ps',
        'ω': 'o'
    }
    caps = {
        'Α': 'A',
        'Β': 'V',
        'Γ': 'G',
        'Δ': 'D',
        'Ε': 'E',
        'Ζ': 'Z',
        'Η': 'I',
        'Θ': 'TH',
        'Ι': 'I',
        'Κ': 'K',
        'Λ': 'L',
        'Μ': 'M',
        'Ν': 'N',
        'Ξ': 'X',
        'Ο': 'O',
        'Π': 'P',
        'Ρ': 'R',
        'Σ': 'S',
        'Τ': 'T',
        'Υ': 'Y',
        'Φ': 'F',
        'Χ': 'CH',
        'Ψ': 'PS',
        'Ω': 'O'
    }
    # Simple digraphs with no extra rules or edge cases
    # No need for mixed casing "Γγ" or "Γξ" against Greek phonology
    el_simple_digraphs = [
        'γγ',
        'γξ',
        'γχ',
        'ου'
    ]
    eng_simple_digraphs = [
        'ng',
        'nx',
        'nch',
        'ou'
    ]
    el_simple_cap_digraphs = [
        "ΓΓ",
        "ΓΞ",
        "ΓΧ",
        "ΟΥ"
    ]
    eng_simple_cap_digraphs = [
        "NG",
        "NX",
        "NCH",
        "OU"
    ]

    el_mono_digraph_sub = [
        "TH",
        "CH",
        "PS"
    ]
#   Accent based digraphs
#    el_low_acc_digraphs = [
#        "άυ",
#        "αϋ",
#
#        "έυ",
#        "εϋ",
#
#        "ήυ",
#        "ηϋ"
#
#    ]
#    el_mix_acc_digraphs = [
#        "Άυ",
#        "Αϋ",
#
#        "Έυ",
#        "Εϋ",
#
#        "Ήυ",
#        "Ηϋ"
#    ]
#    el_cap_acc_digraphs = [
#        "ΆΥ",
#        "ΑΫ",
#
#        "ΈΥ",
#        "ΕΫ",
#
#        "ΉΥ",
#        "ΗΫ"
#    ]
    el_mp_digraph = [
        "ΜΠ",
        "Μπ",
        "μπ"
    ]
    eng_mp_digraph_0 = [
        "B",
        "B",
        "b"
    ]
    eng_mp_digraph_1 = [
        "MP",
        "Mp",
        "mp"
    ]
    el_xu_digraphs = [
        "αυ",
        "ευ",
        "ηυ"
    ]
    eng_xu_digraphs_v = [
        "av",
        "ev",
        "iv"
    ]
    eng_xu_digraphs_f = [
        "af",
        "ef",
        "if"
    ]
    xu_sound_modifiers_v = [

        "β",
        "γ",
        "δ",
        "ζ",
        "λ",
        "μ",
        "ν",
        "ρ",
        
        "α",
        "ε",
        "η",
        "ι",
        "ο",
        "υ",
        "ω"
    ]
#   +empty space (accounted for in code)
    xu_sound_modifiers_f = [

        "θ",
        "κ",
        "ξ",
        "π",
        "σ",
        "τ",
        "φ",
        "χ",
        "ψ"
    ]
#   Replace ς with σ
    prep_string = string.replace("ς", "σ")
#   if el_low_acc_digraphs or el_mix_acc_digraphs or el_cap_acc_digraphs in string:
#   Do nothing, we don't care with current implementation
#   Prepare the Unicode tables for use with translate()
    lowercase = string.maketrans(lowercase)
    caps = string.maketrans(caps)
#    reference_string_list = reference_string.split(" ")
    new_string_list = prep_string.split(" ")
    output = ""
    for new_string in new_string_list:
        #   Replace all digraphs, so they're ignored by the simple transcription
        for i in el_simple_digraphs:
            if i in string:
                new_string = new_string.replace(i, eng_simple_digraphs[el_simple_digraphs.index(i)])
        for i in el_simple_cap_digraphs:
            if i in string:
                new_string = new_string.replace(i, eng_simple_cap_digraphs[el_simple_cap_digraphs.index(i)])
#       Check which "mp" sound to use depending on if it's at word start
        for i in el_mp_digraph:
            if i in string:
                if string.startswith(i):
                    new_string = new_string.replace(i, eng_mp_digraph_0[el_mp_digraph.index(i)], 1)
                    new_string = new_string.replace(i, eng_mp_digraph_1[el_mp_digraph.index(i)])
#       Check what VOWEL+"υ" should transliterate to depending on the following letter.
        for i in el_xu_digraphs:
            if i in new_string:
                if len(new_string) > 2:  # Make sure we're not calling an out of range index
                    for loop in xu_sound_modifiers_f:
                        if new_string[new_string.find(i)+2] in loop:
                            new_string = new_string.replace(i, eng_xu_digraphs_f[el_xu_digraphs.index(i)])

                    for loop in xu_sound_modifiers_v:
                        if new_string[new_string.find(i)+2] in loop:
                            new_string = new_string.replace(i, eng_xu_digraphs_v[el_xu_digraphs.index(i)])
                if len(new_string) == 2:  # Account for VOWEL+"υ" at end of sentence
                    new_string = new_string.replace(i, eng_xu_digraphs_f[el_xu_digraphs.index(i)])

#   Simple transcription
        new_string = new_string.translate(caps)
        new_string = new_string.translate(lowercase)
#   Normalize capital letters if needed
        for i in el_mono_digraph_sub:
            if new_string.startswith(i):
                if new_string[3].islower() is True:
                    new_string = new_string.replace(new_string[1], new_string[1].lower())
        new_string += " "
        output += new_string
    return output
