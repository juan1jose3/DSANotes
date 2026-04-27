def toGoatLatin(sentence):
    vowels = ["a","e","i","o","u"]
    splited = sentence.split(" ")

    word_counter = 0

    new_word = ""
    for word in splited:
        if word[0].lower() in vowels:
            word+="ma"
            
        else:
            first = word[0]
            word += first + "ma"
            word = word[1:]

        word_counter += 1
        word+= "a" * word_counter
        new_word += word + " "
    return new_word.strip()


        




print(toGoatLatin("The quick brown fox jumped over the lazy dog"))