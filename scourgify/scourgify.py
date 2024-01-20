# Import required modules
import csv
import sys
# Main function
def main():
    # Calling the function
    check_command_line()
    # Variable to store the output
    output =[]
    # Try to open and read the file while excepting the error
    try:
        with open(sys.argv[1],'r') as csv_file:
            # Using csv.DictReader to read the file
            reader = csv.DictReader(csv_file)
            # for loop to check the file
            for row in reader:
                # Using the split function to split the name into first and last
                name = row['name'].split(",")
                # appending or storing the name last name and house in output variable
                output.append({"first":name[1].lstrip(), "last":name[0] , "house":row["house"]})
    # Excepting the FileNotFoundError
    except FileNotFoundError:
        # Exit message
        sys.exit(f"Could not read {sys.argv[1]}")
        # Using opne function to write into the new file
    with open(sys.argv[2],'w') as file:
        # Using csv.DictWriter fucntion
        writer = csv.DictWriter(file, fieldnames = ["first","last","house"])
        writer.writerow({"first":"first","last":"last","house":"house"})
        for row in output:
            writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})
# Defining the function to check the command line arguments
def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a csv file")
# calling the main function 
if __name__ == "__main__":
    main()