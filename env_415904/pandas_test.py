from calculator import add_column, isna


def test_isna():
    assert isna("dog") == False
    assert isna(None) == True


def test_add_column():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    result = add_column(df)
    expected = pd.DataFrame({"a": [1, 2], "b": [3, 4], "sum": [4, 6]})
    pd.testing.assert_frame_equal(result, expected)
