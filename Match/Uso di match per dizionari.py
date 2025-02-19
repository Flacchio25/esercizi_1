user = {"nome": "Luca", "ruolo": "admin"}

match user:
    case {"nome": name, "ruolo": "admin"}:
        print(f"Benvenuto amministratore {name}")
    case {"nome": name, "ruolo": "utente"}:
        print(f"Benvenuto utente {name}")
    case _:
        print("Ruolo non riconosciuto")

print(user)