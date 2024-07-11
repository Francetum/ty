



while True:
    user_input = input('rentre un nombre: ')
    try:
        user_input = int(user_input)
        break
    
    except ValueError:
        print('vous devez rentrer un nombre: ')
        
        
        
print(user_input )