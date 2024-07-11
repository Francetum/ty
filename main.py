class Transaction:
    def __init__(self, title, description, amount):
        self.title = title
        self.description = description
        self.amount = amount
        self.wallet = amount * 1.2  # Initialisation de l'attribut wallet
        self.interest = amount / 5 # Initialisation de l'attribut interest
        
        
    def display_info(self):
        print(f"Voici les infos : le titre : {self.title}, le montant est de : {self.amount}, la description : {self.description} et vos intérêts sont de {self.interest}" )
        
    # add money in the wallet
    def add_money(self):
        add_amount = input("veuillez verser un montant sur votre compte : ")
        self.wallet += int(add_amount)
        print(f"vous avez ajouté {add_amount} à votre compte, votre nouveau solde est : {self.wallet}")
    
    # retire money from the wallet
    def withdraw_money(self):
        withdraw_amount = input("veuilllez retirer le montant de votre choix : ")
        if int(withdraw_amount) <= self.wallet:
            self.wallet -= int(withdraw_amount)
            print(f"vous avez retiré {withdraw_amount} de votre compte, votre nouveau solde est : {self.wallet}")
        else:
            print("Fonds insuffisants pour effectuer cette transaction.")
            
    # creat an historique of the transaction 
    def history_transaction(self):
        print(f"Voici l'historique de votre transaction : \n- Le titre : {self.title}, le montant est de : {self.amount}, la description : {self.description}")
        print(f"Vos intérêts sont de : {self.interest}")
        print(f"Votre solde actuel est de : {self.wallet}")
            
transaction1 = Transaction("pret", "pour martin", 3)
transaction1.add_money()  # Ajout d'argent pour tester le retrait
transaction1.withdraw_money()
