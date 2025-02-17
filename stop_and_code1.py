
#creo lista vuota e chiedo allo studente quanti voti vuole inserire
lista = []
numero_voti = input("Quanti voti vuoi inserire? ")
try:
    numero_voti = int(numero_voti)
    print("Bene, hai deciso di inserire: ", numero_voti, "voti")
    print("--------------")
except ValueError:
    print("ATTENZIONE: Devi inserire un numero valido!")
    print("--------------")
    exit()

# recupero i voti con un ciclo for e li aggiungo alla lista
for x in range(numero_voti):
    try:
        voto = input("Inserisci un voto: (0-10): ")
        voto = int(voto)
        lista.append(voto)
    except ValueError:
        print("ATTENZIONE: Hai inserito un voto non corretto!")
        print("--------------")
print("")
print("---RISULTATI---")
print("Voti inseriti: ", lista)

# calcolo la somma e la media dei voti
somma_voti = 0
media_voti = 0
for voto in lista:
    somma_voti = somma_voti + voto
    media_voti = somma_voti / numero_voti
print("Somma voti: ", somma_voti)
print("Media voti: ", media_voti)

# trovo il voto più alto e quello più basso inseriti
voto_piu_alto = max(lista)
voto_piu_basso = min(lista)
print(f"Voto massimo: {voto_piu_alto}")
print(f"Voto minimo: {voto_piu_basso}")

# trovo quanti voti ci sono sopra la media e sotto la media
voti_superiori_media = []
voti_inferiori_media = []

for voto in lista:
    if voto >= 6:
        voti_superiori_media.append(voto)
    else:
        voti_inferiori_media.append(voto)

voti_superiori_media = len(voti_superiori_media)
voti_inferiori_media = len(voti_inferiori_media)

print(f"Voti sopra la media: {voti_superiori_media}")
print(f"Voti sotto la media: {voti_inferiori_media}")

# stampo un messaggio se ci sono voti insufficienti
voti_insufficienti = []

for voto in lista:
    if voto < 6:
        voti_insufficienti.append(voto)
print(f"Voti insufficienti: {len(voti_insufficienti)}")

# determino se lo studente è promosso o bocciato
if media_voti >= 6:
    print("Risultato: Promosso")
else:
    print("Risultato: Bocciato!")
