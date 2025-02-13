# una funzione è un blocco di codice pensato per essere ripetuto
def mia_funzione():
    print("=============")
    print("Ciao dalla funzione")
    print("=============")
    
mia_funzione() # per lanciare la funzione

for n in range(5):
    mia_funzione()
 
# parametro o argomento della funzione    
def saluta(nome):
    print(f"Ciao {nome.upper()}")
    
saluta("Gigi")
saluta("Mario")

#parametri multipli
def presentati(nome, cognome, anni):
    mag_min = ""
    
    if anni >= 18:
        mag_min = "maggiorenne"
    else:
        mag_min = "minorenne"
        
    print(f"Ciao sono {nome} {cognome} e sono {mag_min}")

presentati("Mario", "Rossi", 67)
presentati(anni=45, nome="Riccardo", cognome="Pelli") # si potrebbero anche passare così i parametri

# torna un valore che posso mettere in una variabiile e riutilizzare
def somma(n1, n2):
    return(n1+n2)
    
risultato = somma(3, 5)
print(f"Il risultato è: {risultato}")
print(f"Il risultato al quadrato è: {risultato**2}")

# parametri di default/opzionali
def spedisci(prodotto, paese="Italia"):
    print(f"Il prodotto {prodotto} è stato spedito in {paese}")
    
spedisci("Bici", "Italia")
spedisci("Ciabatte")
spedisci("Pantaloni", "Spagna")

# *args
def somma_multipla(*numeri):
    totale = 0
    
    for n in numeri:
        totale += n
        
    return totale

print(somma_multipla(3,45,34,78,6))
print(somma_multipla(12,4,88))

# print esempio eclatante
print("Ciao", "Riccardo", "Saluti", 89, True)