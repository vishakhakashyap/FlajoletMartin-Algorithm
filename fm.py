import random
import math
import csv

def trailing_zeros(x):
    """Counting number of trailing zeros
    in the binary representation of x."""
    if x == 0:
        return 1
    count = 0
    while x & 1 == 0:
        count += 1
        x >>= 1
    return count

def flajolet_martin(dataset, k):
    """Number of distinct elements using
    the Flajolet-Martin Algorithm."""
    max_zeros = 0
    dataset_as_int = []

    for item in dataset:
        try:
            dataset_as_int.append(int(item))
        except ValueError:
            pass  # Skip non-integer values

    for i in range(k):
        hash_vals = [trailing_zeros(random.choice(dataset_as_int)) for _ in range(len(dataset_as_int))]
        max_zeros = max(max_zeros, max(hash_vals))

    return 2 ** max_zeros

# Read data from a CSV file
csv_file = 'dataset.csv'  # Replace with the path to your CSV file

# Create an empty list to store the data from the CSV file
data = []

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    for row in reader:
        data.extend(row)

# Example
dist_num = flajolet_martin(data, 10)
print("Estimated number of distinct elements:", dist_num)