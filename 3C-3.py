oggetti = []
for _ in range(3):
    oggetto = input("Inserisci un oggetto: ")
    oggetti.append(oggetto)
match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer","tablet"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria non riconosciuta")
