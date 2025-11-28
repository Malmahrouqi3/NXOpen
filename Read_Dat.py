def Read_Dat (filename):
    import numpy as np
    import pandas as pd
    import os
    # Define the filename

    # Get the current directory (where your Python code is)
    file_dir = os.getcwd()
    file_path = os.path.join(file_dir, filename)


    # Open the file
    with open(file_path, "r") as f:
    # Read the data lines
        data_lines = f.readlines()

    # Initialize an empty list to store points
    points = []

    # Read the data using pandas.read_csv
    #add "z", if you are using dat with 3 dimensions
    data = pd.read_csv(file_path, header=None, names=["x", "y"], sep=" ")  # Adjust delimiter if needed

    # Print the data
    points = data.values
    points = [[row[0], row[1], 0] for row in points]
    return points
