not_allowed = ('.', '/', ';')


while True:
    print()
    nickname = input('entre un prenom ')
    invalid_char = 0
    
    for char in not_allowed:
        if char in nickname:
            print(f'le caractère {char} n\'est pas permis')
            invalid_char += 1
    if invalid_char > 0: 
        print(f'le caractère {nickname} n\'est pas permis')
    else:
        break
    
print(f'welcome to {nickname}')
    