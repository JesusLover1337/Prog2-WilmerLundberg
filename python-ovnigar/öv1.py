word = input("Skriv ett ord att översätta till rövarspråk: ")
konsonanter = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v","w", "x", "z"]  
word_in_rövarspråk = ""
for letter in word:
    if letter in konsonanter:
        word_in_rövarspråk = word_in_rövarspråk + letter+"o"+letter
    else:
        word_in_rövarspråk = word_in_rövarspråk + letter    
print(word_in_rövarspråk)