"""Requests and extracts a dataframe from a given link, and checks the dataframe for columns, length, and column types."""
import io
import requests
import pandas as pd

def read_link(some_link):
    """Extracts a dataframe from a provided link."""
    urlData = requests.get(some_link).content
    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    return df

def test_create_dataframe(dataframe, col_list):
    """Checks df has right columns, >= 10 rows, values of the same column are the same type."""
    count = 0
    if set(dataframe.columns) == set(col_list):
        count += 1

    if len(dataframe) >= 10:
        count += 1

    types = []
    for col in dataframe:
        types.append(type(dataframe.loc[0, col]))
    counter = 0
    failed_count = 0
    for i, col in enumerate(dataframe):
        for entry in dataframe[col]:
            if type(entry) == types[i]:
                counter += 1
            else:
                failed_count += 1

    if failed_count == 0:
        count += 1
    if count == 3:
        print('True')
    else: return 'False'
