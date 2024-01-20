def main():
    user_input = input("enter text here..")
    convert(user_input)

def convert(user_input):
    new_user_input = user_input.replace(":)","🙂").replace(":(","🙁")
    print(new_user_input)
main()