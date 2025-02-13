eta = input("Quanti anni hai? ") # valore ritornato da input è sempre una stringa

#gestione errori try/except
try:
    eta_int = int(eta)
    
    if eta_int >= 18:
        print("Maggiorenne")
    else:
        print("Minorenne")
        
except: # intercetto ogni errore che può capitare
    print("Specificare un numero")
    
print("FINITO")

try:
    x = 10 / 0
except ZeroDivisionError as e: # intercetto un tipo di errore specifico
    print(e)
    print("Non si può dividere per 0")
    
try:
    file = open("pippo.txt", "r")
    lista = [1, 2, 3]
    n = lista[9]
except FileNotFoundError:
    print("Errore: file non trovato")
except IndexError:
    print("Errore: Lista troppo corta")