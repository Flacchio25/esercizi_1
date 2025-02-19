n:int= int(input("Inserisci posizione finale"))
if n==1:
    print(f"{n}st!")
elif n==2:
    print(f"{n}nd!")
elif n==3:
    print(f"{n}rd!")
else: 
    print(f"{n}th!")

#Con Match il codice è più pulito e leggibile
n = int(input("Insert finishing position: "))

match n:
    case 1:
        print(f"{n}st!")
    case 2:
        print(f"{n}nd!")
    case 3:
        print(f"{n}rd!")
    case _:
        print(f"{n}th!")















