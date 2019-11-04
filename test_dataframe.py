"""Imports a dataframe and tests it for its columns, length, and column types."""
import df_from_url

LINK = "https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD"
DATAFRAME = df_from_url.read_link(LINK)
COL_LIST = list(DATAFRAME.columns)

def test_dataframe():
    """Test for columns, length, and column types and raises appropriate errors."""
    df_from_url.test_create_dataframe(DATAFRAME, COL_LIST)
    if set(DATAFRAME.columns) != set(COL_LIST):
        raise ValueError("columns are not the same")
    if len(DATAFRAME) <= 10:
        raise ValueError("not enough rows in dataframe")
    types = []
    for col in DATAFRAME:
        types.append(type(DATAFRAME.loc[0, col]))
    for i, col in enumerate(DATAFRAME):
        for entry in DATAFRAME[col]:
            if type(entry) == types[i]:
                pass
            else:
                raise TypeError("types in columns must be the same")

def test_columns():
    """Test that columns are of the same type."""
    try:
        df_from_url.test_create_dataframe(DATAFRAME, COL_LIST)
    except TypeError:
        pass

def test_nan():
    """Test that there are no null values in dataframe."""
    if DATAFRAME.isnull().values.any():
        raise ValueError("nan values found")
    else:
        pass

def test_one_row():
    """Test the length of the dataframe."""
    if len(DATAFRAME) >= 1:
        pass
    else: raise ValueError("dataframe is not at least 1 row")
