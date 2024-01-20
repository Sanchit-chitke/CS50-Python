def main():
    text = input("Enter your text here ")
    playback(text)

def playback(text):
    new_text = text.replace(" ", "...")
    print(new_text)

main()