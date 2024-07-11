list_valid = ("a"," b"," c", "d", "e", "f", "g", "h", "i", "j", "k", "l"," m", "n" 
              , "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" )
# tu ne peux vérifier qu 'un seul caracteres , a arranger pour verifier un mot , ex mettre ds un boucle

while True:
    user_input = input("Entrez une lettre : ").lower()
    if user_input in list_valid:
        print(f"La lettre {user_input} est valide.")
        break
    else:
        print("La lettre entrée n'est pas valide. Veuillez réessayer.")
        
print(user_input)