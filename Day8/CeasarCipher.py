from  art import  logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'
            , 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'
            , 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
stop=False
print(logo)
def ceasar_cipher(text, shift,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift*=-1
    for i in text:
        if i in alphabet:
            index = alphabet.index(i)
            shifted_position = index + (shift % 26)
            end_text += alphabet[shifted_position]
        else:
            end_text += i
    print(f"Here is the {cipher_direction} result:{end_text}")
while not stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar_cipher(text, shift, direction)
    answer=input("Do you want to continue?(yes/no)\n").lower()
    if answer == "no":
        stop=True

