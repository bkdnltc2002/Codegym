def countword(message):
    num_words={}
    message=message.lower()
    text_list=message.split(" ")

    for word in text_list:
        if word not in num_words:
            num_words.update({word:0})

    for word in text_list:
        word=word.strip()
        if word in num_words:
            num_words[word]+=1

    return num_words


message=input("Type something: ")
print(countword(message))
