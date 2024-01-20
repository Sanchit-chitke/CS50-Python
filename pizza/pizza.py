# Importing the required modules
import csv
import sys
from tabulate import tabulate
# defining the main function
def main():
    # Calling the function
    check_command_line()
    # Variable to store the file data
    data = []
    # try to open file and catch the error
    try:
        with open(sys.argv[1],'r') as csvfile:
            # Using the reader method to read the file
            reader = csv.reader(csvfile)
            # for loop to get the data
            for row in reader:
                data.append(row)
    # catching the error
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(data[1:], headers=data[0], tablefmt ="grid"))
# Function to check the command line arguments
def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()