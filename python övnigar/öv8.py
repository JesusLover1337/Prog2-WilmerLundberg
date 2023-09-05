x = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def qwe(shift,text):
    new_text = ""
    for letter in text:
        if letter == " ":
            new_text = new_text + " "
        else:
            letter_index = x.index(letter)
            new_letter_index = letter_index + shift
            if new_letter_index > len(x) - 1:
                new_letter_index = new_letter_index - len(x)
            new_text = new_text + x[new_letter_index]
    return new_text
def asd(shift,text):
    new_text = ""
    for letter in text:
        if letter == " ":
            new_text = new_text + " "
        else:
            letter_index = x.index(letter)
            new_letter_index = letter_index - shift
            if new_letter_index < 0:
                new_letter_index = new_letter_index + len(x) 
            new_text = new_text + x[new_letter_index]
    return new_text
    
text = input("skriv en text: ")
shift = int(input("hur mycket ska texten shiftas? "))
new_text = qwe(shift,text)
print(f"Här är din crypterade text: {new_text}")

text2 = input("skriv den crypterade texten: ")
shift2 = int(input("hur mycket har texten shiftas? "))
new_text2 = asd(shift2,text2)
print(new_text2)