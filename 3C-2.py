voto_laurea = int(input("Inserisci il voto di laurea: "))
match voto_laurea:
    case _ if 106 <= voto_laurea <= 110:
        print("GPA 4.0")
    case _ if 101 <= voto_laurea <= 105:
        print("GPA 3.7")   
    case _ if 96 <= voto_laurea <= 100:
        print("GPA 3.3")
    case _ if 91 <= voto_laurea <= 95:
        print("GPA 3.0")
    case _ if 86 <= voto_laurea <= 90:
        print("GPA 2.7")
    case _ if 81 <= voto_laurea <= 85:
        print("GPA 2.3")
    case _ if 76 <= voto_laurea <= 80:
        print("GPA 2.0")   
    case _ if 70 <= voto_laurea <= 75:
        print("GPA 1.7")   
    case _ if 66 <= voto_laurea <= 69:
        print("GPA 1.0")
    case _:
        print("voto non valido")