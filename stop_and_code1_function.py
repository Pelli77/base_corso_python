# Inserisco i voti
def inserimento_voti():
    lista = []
    
    try:
        numero_voti = int(input("Quanti voti vuoi inserire? "))
        print("Bene, hai deciso di inserire:", numero_voti, "voti")
        print("--------------")
    except ValueError:
        print("ATTENZIONE: Devi inserire un numero valido!")
        print("--------------")
        exit()

    # recupero i voti con un ciclo for e li aggiungo alla lista
    for x in range(numero_voti):
        try:
            voto = int(input(f"Inserisci un voto {x + 1}: (0-10) "))
            lista.append(voto)
        except ValueError:
            print("ATTENZIONE: Hai inserito un voto non corretto!")
            print("--------------")
    
    print("Lista dei voti inseriti:", lista)
    print("--------------")
    return lista

# calcolo la somma e la media dei voti
def calcola_media_voti(lista):
    somma_voti = 0
    for voto in lista:
        somma_voti += voto
    media_voti = somma_voti / len(lista)
    return somma_voti, media_voti

# determino se lo studente è promosso o bocciato
def stampa_risultato(media_voti):
    if media_voti >= 6:
        print("-----------")
        print("Risultato: Promosso!")
        print("-----------")
    else:
        print("-----------")
        print("Risultato: Bocciato!")
        print("-----------")

# trovo il voto più alto e più basso
def voto_extremo(lista):
    voto_piu_alto = max(lista)
    voto_piu_basso = min(lista)
    return voto_piu_alto, voto_piu_basso

# conto i voti superiori e inferiori alla media
def conta_voti_media(lista, media_voti):
    voti_superiori_media = 0
    voti_inferiori_media = 0

    for voto in lista:
        if voto >= media_voti:
            voti_superiori_media += 1
        else:
            voti_inferiori_media += 1

    return voti_superiori_media, voti_inferiori_media

# stampo il numero di voti insufficienti
def voti_insufficienti(lista):
    voti_insufficienti = []
    for voto in lista:
        if voto < 6:
            voti_insufficienti.append(voto)
    print(f"Voti insufficienti: {len(voti_insufficienti)}")
    return voti_insufficienti

# funzione principale che gestisce il programma
def principale():
    # chiedo i voti e li salvo nella lista
    lista_voti = inserimento_voti()

    # calcolo la somma e la media dei voti
    somma_voti, media_voti = calcola_media_voti(lista_voti)
    print(f"La somma dei voti inseriti è: {somma_voti}")
    print(f"La media dei voti inseriti è: {media_voti}")

    # determino se lo studente è promosso o bocciato
    stampa_risultato(media_voti)

    # trovorova il voto più alto e più basso
    voto_piu_alto, voto_piu_basso = voto_extremo(lista_voti)
    print(f"Voto massimo: {voto_piu_alto}")
    print(f"Voto minimo: {voto_piu_basso}")

    # conto i voti sopra e sotto la media
    voti_superiori_media, voti_inferiori_media = conta_voti_media(lista_voti, media_voti)
    print(f"Voti sopra la media: {voti_superiori_media}")
    print(f"Voti sotto la media: {voti_inferiori_media}")

    # mostro il numero di voti insufficienti
    voti_insufficienti(lista_voti)

# lancio la funzione principale
principale()

