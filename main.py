import hashlib


def verif_password(entry):
    def uppercase(password):
        for x in password:
            if (x.isupper()):
                return 1

    def lowercase(password):
        for x in password:
            if (x.islower()):
                return 1

    def number(password):
        for x in password:
            try:
                int(x)
                return 1
            except ValueError:
                pass

    def special_character(password):
        character_list = ("!", "@", "#", "$", "%", "^", "&", "*")
        for x in password:
            for y in character_list:
                if x == y:
                    return 1

    if len(entry)>=8:
        if uppercase(entry) == 1:
            if lowercase(entry) == 1:
                if number(entry) == 1:
                    if special_character(entry) == 1:
                        return "OK"
                    else: return 4
                else: return 3
            else: return 2
        else: return 1
    else :return 0

def hash_and_upload(password):
    def hash(password):
        hash_object = hashlib.sha256()
        hash_object.update(password.encode())
        hex_hash = hash_object.hexdigest()
        print(hex_hash)
        return hex_hash

    def fetch_array():
        import json
        f = open("password.json", "r")
        array = f.read()
        f.close
        # Retourne un array
        return json.loads(array)
    def send_array():
        hashed_pass = [hash(password)]
        hashed_pass.extend
        json





while True:
    entry = input("Veuillez entrée un mot de passe contenant au minimum:\n-8 caractères\n-Une lettre minuscule\n-Une "
                  "lettre majuscule\n-Un chiffre\n-un caractère special contenue dans cette liste (!, @, # , $ , "
                  "% , ^ , & , * )\n:")
    match verif_password(entry):
        case 0:
            print("Votre mot de passe est trop court, veuillez recommencer")
        case 1:
            print("Votre mot de passe ne continent pas de majuscule,veuillez recommencer")
        case 2:
            print("Votre mot de passe ne contient pas de lettre en minuscules, veuillez recommencer")
        case 3:
            print("Votre mot de passe ne contient pas de chiffre, veuillez recommencer")
        case 4:
            print("Votre mot de passe ne contient pas de caractères spéciaux, veuillez recommencer")
        case "OK":
            hash_and_upload(entry)
            break

