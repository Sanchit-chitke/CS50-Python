# Import the required module
import re
# main function
def main():
    # calling the parse function while taking the input
    print(parse(input("HTML: ")))

# create a fucntion to sort the input
def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>" , s):
        url = re.search(r"(http(s)?:\/\/(www\.)?youtube\.com\/embed\/)([a-z_A-Z_0-9]+)" , s )
        if url:
            split_url = url.groups()
            return "https://youtu.be/" + split_url[3]


if __name__ == "__main__":
    main()