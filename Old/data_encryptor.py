import random
import string
chars = " "+string.punctuation+string.digits+string.ascii_letters
charslist = list(chars)

key = ["'", 'I', '&', 'X', '?', 'L', '(', '"', 'y', 'H', '5', '_', '!', 'x', '3', 'h', '\\', ')', 'E', '|', ';', 'b', 'q', '#', 'j', 's', '2', 'n', 'z', 'U', 'g', 'a', 'Q', 'N', '<', 'c', 'Z', '}', 'J', ':', '9', 'd', 'V', '>', 'A', 'p', '^',
       'l', ',', '@', 'k', ']', '8', '0', 'e', 'i', 'D', '1', 'R', '`', 'v', '+', 'o', 'B', 'T', 'G', 'm', 'u', '[', 'Y', '-', 'O', '=', '*', '/', ' ', 't', 'S', 'C', 'F', 'W', '~', 'w', 'M', '7', '4', 'f', '6', 'P', 'r', 'K', '%', '{', '.', '$']

def encrypt_data(userinput):
    # FOR OUTPUT BEAUTY
    #  Encryption has been started
    print("")
    # change letters
    # {
    cipher_text = ""
    for i in userinput:
        index = charslist.index(i)
        cipher_text += key[index]
    # }
    # print(cipher_text)
    cipher_text = cipher_text[-1::-1]
    # print(cipher_text)
    # choice tree charar=cter for start and end
    my_string = "abcdefghijklmnopqrstuvwxyz"
    random_char1l = random.sample(my_string, 5)
    random_char2l = random.sample(my_string, 5)
    # change list into string
    random_char1s = "".join(random_char1l)
    random_char2s = "".join(random_char2l)
    # append tree charar=cter at start and end
    final_string = random_char1s+cipher_text+random_char2s
    return final_string

def decrypt_data(userinput):
# decryption
    #  Decryption has been started
    # REMOVE STARTED THREE LETTERS
    start_rm_string = userinput[5:]
    # REMOVE ENDED THREE LETTERS
    end_rm_string = start_rm_string[:-5]
    # print(end_rm_string)
    plain_text = ""
    for i in end_rm_string:
        index = key.index(i)
        plain_text += charslist[index]
    plain_text = plain_text[::-1]
    length = len(plain_text)
    #  Decrypt text is :
    # plain_text=plain_text[-1]+plain_text[:length-1]
    return plain_text


if __name__ == "__main__" :
    # INPUt FROM USER (MESSAGE)
    print("Enter message : ")
    userinput = input()

    # encrypt or decrypt OPTIONS
    print("Do you want to 1[encrypt] or 2[decrypt]")
    agree = input()
    if agree == "1":
        print(encrypt_data(userinput))
    else:
        print(decrypt_data(userinput))
