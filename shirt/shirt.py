# Import the required modules
import sys
from os.path import splitext
from PIL import Image, ImageOps
# Main function
def main():
    # Calling the check command line function
    check_command_line()
    # Try and exception while opening the image
    try:
        image_file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Variable to store the shirt image
    shirt_file = Image.open("shirt.png")
    # Storing the size of the shirt image
    size = shirt_file.size
    # Variable to store the fit image
    muppet = ImageOps.fit(image_file,size)
    # pasting the shirt file onto muppet
    muppet.paste(shirt_file, shirt_file)
    # Saving the output
    muppet.save(sys.argv[2])
# Check commandline function
def check_command_line():
    # Checking the lenght of command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Using splitext to split the commandline argv
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    # Check the extension of the file
    if check_extension(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid output")
    # f the extension of two files are not same then exit the code wiht msg
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")
# Extension checking function
def check_extension(file):
    # If the file extensions are not in the file return false else true
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False
# Calling the main function
if __name__ == "__main__":
    main()