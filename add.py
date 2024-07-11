
list_valid = ("a"," b"," c", "d", "e", "f", "g", "h", "i", "j", "k", "l"," m", "n" 
              , "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" )
def addition(nb1, nb2):
    return nb1 + nb2

def isaletter(user_input):
    while True:
        user_input = input("Entrez une lettre : ").lower()
        if user_input in list_valid:
            print(f"La lettre {user_input} est valide.")
            break
        else:
            print("La lettre entrée n'est pas valide. Veuillez réessayer.")


if __name__ == '__main__':
    addition()
    
if __name__ == '__main__':
    isaletter()