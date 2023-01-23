import hashlib
def uppercase(entry):
    for x in entry:
        if (x.isupper()) == True:
            return 1

def lowercase(entry):
    for x in entry:
        if (x.islower()) == True:
            return 1

def number(entry):
    for x in entry:
        try:
            int(x)
            return 1
        except ValueError:
            pass
def special_character(entry):
    character_list = ("!", "@", "#", "$", "%", "^", "&", "*")
    for x in entry:
        for y in character_list:
            if x == y:
                return 1
def verif_password(entry):
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

while True:
    entry = input("Veuillez entrée votre mot de passe")
    match verif_password(entry):
        case 0:
            print("Votre mot de passe est trop court veuillez recommencer")
        case 1:
            print("Votre mot de passe ne continent pas de majuscule,veuillez recommencer")
        case 2:
            print("Votre mot de passe ne contient pas de lettre en minuscules, veuillez recommencer")
        case 3:
            print("Votre mot de passe ne contient pas de chiffre, veuillez recommencer")
        case 4:
            print("Votre mot de passe ne continet pas de caractère spéciaux, veuillez recommencer")
        case "OK":

            hash_object = hashlib.sha256()
            hash_object.update(entry.encode())
            hex_hash = hash_object.hexdigest()

            print(hex_hash)

