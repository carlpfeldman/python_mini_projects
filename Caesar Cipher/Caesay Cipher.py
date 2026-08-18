alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translated_message = ""

for char in message:
    if char in alphabet:
        character_value = alphabet.find(char)
        translated_message += alphabet[(character_value + 10) % 26]
    else:
        translated_message += char

    #print(translated_message)


