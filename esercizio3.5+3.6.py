invitati = ["Adolf","Musso","Musko","Hawking"]
for invitato in invitati:
    if invitato == 'Adolf':
        print(f"Ad {invitato}: Best pittore austriaco vie npo qua.")
    elif invitato == 'Musso':
        print(f"A {invitato}: Zio oggi famo na cena clamorosa semo io te e altri due fenomeni.")
    elif invitato == 'Musko':
        print(f"Ad {invitato}: Elon stasera conoscerai i tuoi mentori.")
    elif invitato == 'Hawking':
        print(f"A {invitato}: ZZZcccvvZ.")
print("Messaggio a tutti gli invitati: Regà Musko ci ha pisciati")
invitati[2] = "Trump"
print(invitati)


invitati = ["Adolf","Musso","Hawking","Trump"]
for invitato in invitati:
    if invitato == 'Adolf':
        print(f"A {invitato}: o te non ce piscià")
    elif invitato == 'Musso':
        print(f"A {invitato}: Patatone non hai idea di chi viene a cena stasera")
    elif invitato == "Hawking":
        print(f"C3-P8 te ce stai sì?!")


#Esercizio 3.6

print("Regà FERMI ho trovato un tavolo più grosso, mo ne chiamo altri tre, famo il panico stasera")
invitati.insert(0,"Osama BinL")
invitati.insert(2,"Xin gin Ping")
invitati.append("Aldo moro",)
print(invitati)

for invitato in invitati:
    if invitato == 'Adolf':
        print(f"A {invitato}: o te non ce piscià")
    elif invitato == 'Musso':
        print(f"A {invitato}: Patatone non hai idea di chi viene a cena stasera")
    elif invitato == "Hawking":
        print(f"C3-P8 te ce stai sì?!")
    elif invitato == 'Osama BinL':
        print(f"HANNO HITTATO LA SECONDA TORRE")
    elif invitato == 'Xin gin Ping':
        print(f"BIN CHI LING")
    elif invitato == 'Aldo moro':
        print(f"Forza rossi")