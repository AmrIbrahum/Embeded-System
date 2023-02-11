def caesar(msg, key):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    new_message = ""
    for c in msg:
        position = alphabet_lower.find(c.lower())
        new_position = (position + key) % len(alphabet_lower)
        new_character = alphabet_lower[new_position]
        if c.isupper():
            new_character = new_character.upper()
        new_message += new_character

    return new_message


for i in range(26):
    print(i, caesar("iqfihhih", -i))