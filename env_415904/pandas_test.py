from calculator import isna


def isna_test():
    assert isna("dog") == False
    assert isna(None) == True
