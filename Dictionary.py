def findWord(dict, input_word):
    if input_word in dict:
        print(dict[input_word])
    else:
        print("Your word is unvailable!")


dict = {"Hello": "Xin Chao", "Bye": "Tam Biet", "dog":"cho","cat":"meo","rhino":"te giac","intention":"du dinh"}
input_word = input("Type something to translate: ")
findWord(dict, input_word)