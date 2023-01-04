def greek_iso_transliteration(string: str):
    el_low = [
        "α"
        "β"
        "γ"
        "δ"
        "ε"
        "ζ"
        "η"
        "θ"
        "ι"
        "κ"
        "λ"
        "μ"
        "ν"
        "ξ"
        "ο"
        "π"
        "ρ"
        "σς"
        "τ"
        "υ"
        "φ"
        "χ"
        "ψ"
        "ω"
    ]
    el_cap = [
        "Α"
        "Β"
        "Γ"
        "Δ"
        "Ε"
        "Ζ"
        "Η"
        "Θ"
        "Ι"
        "Κ"
        "Λ"
        "Μ"
        "Ν"
        "Ξ"
        "Ο"
        "Π"
        "Ρ"
        "Σ"
        "Τ"
        "Υ"
        "Φ"
        "Χ"
        "Ψ"
        "Ω"
    ]
    # TODO FIX Psari, not PSari
    eng_low = [
        "a"
        "v"
        "g"
        "d"
        "e"
        "z"
        "i"
        "th"
        "i"
        "k"
        "l"
        "m"
        "n"
        "x"
        "o"
        "p"
        "r"
        "s"
        "t"
        "y"
        "f"
        
        "ch"
        "ps"
        "o"
    ]
    eng_cap = [
        "A"
        "V"
        "G"
        "D"
        "E"
        "Z"
        "I"
        "TH"
        "I"
        "K"
        "L"
        "M"
        "N"
        "X"
        "O"
        "P"
        "R"
        "S"
        "T"
        "Y"
        "F"
        "CH"
        "PS"
        "O"
    ]
    # Simple digraphs with no extra rules or edge cases
    # No need for mixed casing "Γγ" or "Γξ" against Greek phonology
    el_simple_digraphs = [
        "γγ"
        "γξ"
        "γχ"
    ]
    el_simple_cap_digraphs = [
        "ΓΓ"
        "ΓΞ"
        "ΓΧ"
    ]
    eng_simple_digraphs = [
        "ng"
        "nx"
        "nch"
    ]
    eng_simple_cap_digraphs = [
        "NG"
        "NX"
        "NCH"
    ]
#   Accent based digraphs
    el_low_acc_digraphs = [
        "άυ"
        "αϋ"
        
        "έυ"
        "εϋ"
        
        "ήυ"
        "ηϋ"

    ]
    el_mix_acc_digraphs = [
        "Άυ"
        "Αϋ"
        
        "Έυ"
        "Εϋ"
        
        "Ήυ"
        "Ηϋ"
    ]
    el_cap_acc_digraphs = [
        "ΆΥ"
        "ΑΫ"
        
        "ΈΥ"
        "ΕΫ"
        
        "ΉΥ"
        "ΗΫ"
    ]
    el_mp_digraph = [
        "ΜΠ"
        "Μπ"
        "μπ"
    ]
    eng_mp_digraph_0 = [
        "B"
        "B"
        "b"
    ]
    eng_mp_digraph_1 = [
        "MP"
        "Mp"
        "mp"
    ]
    el_xu_digraphs = [
        "αυ"
        "ευ"
        "ηυ"
    ]
    eng_xu_digraphs = [
        "av"
        "af"
        "ev"
        "ef"
        "iv"
        "if"
    ]
#   List related to xu lists
    xu_sound_modifiers_v = [
#    β, γ, δ, ζ, λ, μ, ν, ρ, α, ε, η, ι, ο, υ, ω
        "β"
        "γ"
        "δ"
        "ζ"
        "λ"
        "μ"
        "ν"
        "ρ"
        
        "α"
        "ε"
        "η"
        "ι"
        "ο"
        "υ"
        "ω"
    ]
    xu_sound_modifiers_f = [
#        θ, κ, ξ, π, σ, τ, φ, χ, ψ, empty space
        "θ"
        "κ"
        "ξ"
        "π"
        "σ"
        "τ"
        "φ"
        "χ"
        "ψ"
    ]
    print(string)
    new_string = string
#   if el_low_acc_digraphs or el_mix_acc_digraphs or el_cap_acc_digraphs in string:
#   Do nothing, we don't care
#   Replace all digraphs so they're ignored by the simple transcription
    for i in el_simple_digraphs:
        if i in string:
            new_string.replace(i, eng_simple_digraphs[el_simple_digraphs.index(i)])
    for i in el_simple_cap_digraphs:
        if i in string:
            new_string.replace(i, eng_simple_cap_digraphs[el_simple_digraphs.index(i)])
#   At the moment we don't care, but in future we need to account for accents too
#   for i in el_low_acc_digraphs
#       if i in string:
#            new_string.replace(i, )
    for i in el_mp_digraph:
        if i in string:
            if string.startswith(i):
                new_string.replace(i, eng_mp_digraph_0[el_mp_digraph.index(i)], 1)
            new_string.replace(i, eng_mp_digraph_1[el_mp_digraph.index(i)])
    for i in el_xu_digraphs:
        if i in string:
            for loop in xu_sound_modifiers_f:
                if string[string.find(i)+1] in loop:
                    new_string.replace(i, eng_xu_digraphs[el_xu_digraphs.index(i)+1])
            for loop in xu_sound_modifiers_v:
                if string[string.find(i)+1] in loop:
                    new_string.replace(i, eng_xu_digraphs[el_xu_digraphs.index(i)])
    for i in el_low:
        if i in el_low:
            new_string.replace(i, eng_low[el_low.index(i)])
    for i in el_cap:
        if i in el_cap:
            new_string.replace(i, eng_cap[el_cap.index(i)])
    return new_string
