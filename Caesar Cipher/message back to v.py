#message back to vishal
alphabet = "abcdefeghijklmnopqrstuvwxyz"
message_for_v = "hey vish, this is a cool cipher, thanks for showing me, what else do you have?"
translated_message_for_v = ""

for char in message_for_v:
    if char in alphabet:
        character_value = alphabet.find(char)
        translated_message_for_v += alphabet[(character_value + 10) % 26]
    else:
        translated_message_for_v += char

    print(translated_message_for_v)