def mainn():
    encrypted_message: str = input("Please enter encrypted message:")
    k_value = input("Please enter k:")
    k_value = int(k_value)

    encrypted_mess_num = []
    for letter in encrypted_message:
        if letter == " ":
            encrypted_mess_num.append(" ")
        else:
            encrypted_mess_num.append(ord(letter) - 65)
            
    decrypted_mess_num = []
    for item in encrypted_mess_num:
        if item == " ":
            decrypted_mess_num.append(" ")
        else:
            converted_num = 0
            int_encrypted_mess_num = int(item)
            converted_num = (int_encrypted_mess_num - k_value) % 26
            decrypted_mess_num.append(str(converted_num))

    decrypt_message = " "
    for item in decrypted_mess_num:
        if item == " ":
            decrypt_message += " "
        else:
            item = int(item) + 65
            decrypt_message += chr(item)

    print(decrypted_mess_num)

    return decrypt_message


mainn()