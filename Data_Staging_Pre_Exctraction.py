import io
import os
from io import StringIO
import pandas as pd


def load_dataset_with_np(file: str, *args, **kwargs) -> str:
    import numpy as np
    # Load a dataset with 5 rows and 3 columns
    data = np.loadtxt('dataset.txt', delimiter=',', skiprows=1, usecols=(0, 1, 2))

    # Print the shape of the dataset
    return str(data.shape)


def load_dataset_with_pandas(file: str, *args, **kwargs) -> str:
    import pandas as pd

    # Load a dataset with 5 rows and 3 columns
    data = pd.read_csv('dataset.csv', usecols=['col1', 'col2', 'col3'])

    # Print the shape of the dataset
    return str(data.shape)


def get_table_of_data() -> tuple:
    import pandas as pd

    # Different table formats
    table_lists = [["Name", "Age", "City"],
                   ["John Smith", 30, "New York"],
                   ["Jane Doe", 25, "Chicago"],
                   ["Bob Johnson", 40, "Los Angeles"]
                   ]

    table_dicts = {
        1: {"Name": "John Smith", "Age": 30, "City": "New York"},
        2: {"Name": "Jane Doe", "Age": 25, "City": "Chicago"},
        3: {"Name": "Bob Johnson", "Age": 40, "City": "Los Angeles"}
    }

    table_pandas_df = pd.DataFrame({
        "Name": ["John Smith", "Jane Doe", "Bob Johnson"],
        "Age": [30, 25, 40],
        "City": ["New York", "Chicago", "Los Angeles"]
    })

    return table_lists, table_dicts, table_pandas_df


def convert_DataFrame_to_csv(df: pd.DataFrame) -> io.StringIO:
    # convert the DataFrame to a CSV string
    csv_string = df.to_csv(index=False)

    # create a file object from the CSV string
    file = StringIO(csv_string)

    # return the file object
    return file


# create a DataFrame with some data
df = pd.DataFrame({
    "Name": ["John Smith", "Jane Doe", "Bob Johnson"],
    "Age": [30, 25, 40],
    "City": ["New York", "Chicago", "Los Angeles"]
})

# get the CSV file object
csv_file = convert_DataFrame_to_csv(df)

# read the CSV file
csv_data = csv_file.read()

# print the CSV data
print(csv_data)

# write the CSV data to a file
with open("data.csv", "w") as f:
    f.write(csv_data)

# print table of lists
print("Table of Lists: \n{}\n".format(get_table_of_data()[0]))

# print table of dicts
print("Table of Dicts: \n{}\n".format(get_table_of_data()[1]))

# print pandas DatFrame
print("Pandas DataFrame: \n{}\n".format(get_table_of_data()[2]))

user_response = input("Open csv generated? [y/n]: ")
if user_response == "y":
    os.startfile('data.csv')
else:
    pass
