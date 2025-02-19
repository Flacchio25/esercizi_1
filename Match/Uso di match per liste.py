#Liste

Ingredienti= ["besciamella", "pomodoro", "macinato"]

match Ingredienti:
        case ["besciamella", "pomodoro", "macinato"]:
            print("Lasagne")
        case ["pomodoro", "macinato", *_]:
            print("Spaghetti al ragù")
        case _:
            print("Non so cosa cucinare")

#Lista dinamica
#Chiediamo all'untente di inserire un elenco di ingredienti separati da una virgola


user_input= input("inserisci gli ingredienti separati da una virgola")
#creiamo una lista con gli ingredienti inseriti dall'utente separati da una virgola
ingredienti = [ingredienti.strip().lower() for ingredienti in user_input.split(",")]
#usiamo il match statement per farci suggerire una ricetta

match ingredienti:
    case ["besciamella", "pomodoro", "macinato"]:
        print("Lasagne")
    case ["pomodoro", "macinato", *_]:
        print("Spaghetti al ragù")
    case["pomodoro", "lievito", "farina"]:
        print("Pizza")
    case["riso", "zafferano", "parmigiano"]:
        print("Risotto alla milanese")
    case["scamorza", "prosciutto", "funghi"]:
        print("Pasta al forno")  
    case _:
        print("Non so cosa cucinare")




