import hashlib
import json

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
def fetch_array():
    import json
    f = open("password.json", "r")
    json_array = f.read()
    f.close
    # Retourne un array
    try:
        return json.loads(json_array)
    #Si aucuns mots de passe n'est présent dans le fichier password.json
    except json.decoder.JSONDecodeError:
        #Création de l'array
        return []
def hash_and_upload(password):

    def hash_pass():
        hash_object = hashlib.sha256()
        hash_object.update(password.encode())
        hex_hash = hash_object.hexdigest()
        print(hex_hash)
        return hex_hash

    def is_here(array,password):
        for x in array:
            if x == password:
                return 1

    def send_array():
        password_list=fetch_array()
        hashed_pass = hash_pass()
        if is_here(password_list, hashed_pass):
            print("Le mot de passe est déjà présent dans la base de donnée")
            return 1
        hashed_pass = [hashed_pass]
        password_list.extend(hashed_pass)
        json_array=json.dumps(password_list)
        f = open("password.json", "w")
        f.write(json_array)
        f.close

    if send_array() == 1:
        return 1

while True:
    choice = input("Souhaitez-vous entrée un nouveau mot de passe(N) ou consulter la liste des hash enregistrer(H) ?")
    match choice:
        case "N":
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
                    if hash_and_upload(entry)==1:
                        pass
                    else:
                        print("Le mot de passe a bien été enregistrer")
                        break
        case "H":
            print("Voici la liste des Hash disponibles")
            for x in fetch_array():
                print(x)
