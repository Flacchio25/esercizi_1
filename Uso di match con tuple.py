#Possiamo individuare un punto in un piano cartesiano con una tupla:
#Cos'è una tupla in Python? Una tupla è una struttura dati simile a una lista, ma immutabile (cioè, una volta creata, non puoi modificarne gli elementi).




point=(3, 5)

match point:
    case(0,0):
        print("Origine")
    case(X,0):
        print(f"Punto sull'asse X: ({x}, 0)")
    case(0,Y):
        print(f"Punto sull'asse Y: (0, {y})")
    case _:
        print(f"Punto generico: {point}")
#In questo caso, se il punto è sull'origine, sull'asse X, sull'asse Y o in un punto generico, verrà stampato il messaggio corrispondente.

#Riconoscere dati di una persona

persona = ("Marco", 25, "Italia")

match persona:
    case ("Marco", età, nazione):
        print(f"Marco ha {età} anni e vive in {nazione}")
    case ("Luca", età, nazione):
        print(f"Luca ha {età} anni e vive in {nazione}")
    case (nome, età, nazione):
        print(f"{nome} ha {età} anni e vive in {nazione}")

