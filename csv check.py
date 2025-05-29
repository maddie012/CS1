import csv
'''fields = ['name', 'age', 'food']

rows = [ ['mia','13','cookie'],
         ['josie', '16', 'ice cream'],
         ['max', '15', 'pizza']]

with open('GFG', 'w', newline = '') as csvfile:
    write = csv.writer(csvfile)
    write.writerow(fields)
    write.writerows(rows)'''


'''data_list = [['apple', 1], ['banana', 2], ['cherry', 3]]
with open('output.csv', 'w', newline = '') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data_list)'''




def export_to_csv(filename, headers, *arrays):
    """
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    """
    if not arrays:
        raise ValueError("At least one array must be provided.")
    
    num_rows = len(arrays[0])
    for arr in arrays:
        if len(arr) != num_rows:
            raise ValueError("All arrays must have the same length.")
    
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        for i in range(num_rows):
            row = [arr[i] for arr in arrays]
            csvwriter.writerow(row)

# Example Usage
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
occupations = ["Engineer", "Teacher", "Doctor"]

export_to_csv("people.csv", ["Name", "Age", "Occupation"], names, ages, occupations)

