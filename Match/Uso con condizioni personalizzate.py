#Uso di match con condizioni personalizzate
# #Possiamo anche applicare condizioni direttamente nei case:

n=int(input("Inserisci un numero: "))
n = int(input("Insert a number: "))

match n:
    case n if n > 0 and n % 2 == 0:
        print(f"{n} is positive and even")
    case n if n > 0 and n % 2 != 0:
        print(f"{n} is positive and odd")
    case n if n < 0 and n % 2 == 0:
        print(f"{n} is negative and even")
    case n if n < 0 and n % 2 != 0:
        print(f"{n} is negative and odd")
    case _:
        print("The inserted number is 0!")