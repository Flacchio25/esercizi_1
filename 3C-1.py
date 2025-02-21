voto = int(input("Inserisci il voto: "))
match voto:
    case 10:
        print("Eccellente")
    case _ if 8 <= voto <= 9:
        print("Molto buono")
    case _ if 6 <= voto <= 7:
        print("Sufficiente")
    case _ if 4 <= voto <= 5:
        print("Insufficiente")
    case _ if 1 <= voto <= 3:
        print("Gravemente insufficiente")
    case _:
        print("Voto non valido")