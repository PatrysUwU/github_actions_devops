from calculator import isna


def test_isna():
    assert isna("dog") == False
    assert isna(None) == True
