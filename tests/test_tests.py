from src.greeklt.capitalize import capitalize
from src.greeklt.remove_accentuation import remove_accentuation
from src.greeklt.greek_transliteration import greek_transliteration
from src.greeklt.convert_final_s import convert_final_s


def test_capitalize():

    assert capitalize("γάιδαρος") == "ΓΑΪΔΑΡΟΣ"
    assert capitalize("γαιδαρος") == "ΓΑΙΔΑΡΟΣ"


def test_remove_accentuation():

    assert remove_accentuation("γάιδαρος") == "γαϊδαρος"
    assert remove_accentuation("γαιδαρος") == "γαιδαρος"


def test_transilteration():

    assert greek_transliteration("fvtia") == "φωτια"
    assert greek_transliteration("kaWiki") == "καΐκι"
    assert greek_transliteration("p;ita soybl;aki") == "πίτα σουβλάκι"
    assert (
        greek_transliteration("Gamow htane den htane na ginei")
        == "Γαμος ητανε δεν ητανε να γινει"
    )


def test_convert_final_s():

    assert convert_final_s("Φάροσ ΦΑΡΟΣ φάρος") == "Φάρος ΦΑΡΟΣ φάρος"
