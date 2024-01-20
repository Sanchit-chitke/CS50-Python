def main():
    # get the user input
    sentence = input("Input: ")
    # message without vowels
    message_without_vowels = shorten(sentence)
    # print the output
    print("Output: " + message_without_vowels)




def shorten(sentence):
    word_without_vowels =""
    # loop through the input
    for letter in sentence:
    # find the vowels to ommit
        if not letter.lower() in ['a','e','i','o','u']:
            # add the letter to the word_without_vowels
            word_without_vowels += letter
    # return the word without the vowels
    return word_without_vowels

if __name__ == "__main__":
    main()