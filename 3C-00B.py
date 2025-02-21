nome = input("Inserisci il nome: ")
gender = input("Inserisci il genere (m/f): ")
#match statement
match gender:   
    case "m":
        print(f"Nome: {nome}")
        print("Gender: Maschio")
    case "f":
        print(f"Nome: {nome}")
        print("Gender: Femmina")
    case _:
        print(f"Non è possibile generare un documento di identità")
