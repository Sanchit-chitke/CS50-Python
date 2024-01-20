# Importing the sys moudule
import sys
# defining the main function
def main():
    # calling the function
    check_command_line_argv()
    # Using try and exception to catch the error
    try:
        file = open(sys.argv[1], 'r')
        lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")
    # new variable to store the count of lines in file
    count_lines = 0
    for line in lines:
        if check_line(line) == False:
            count_lines += 1
    print(count_lines)
# defining the the function
def check_command_line_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

if __name__ == "__main__":
    main()