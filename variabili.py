# variabili
nome_completo = "gianni rossi"
colore = "rosso"

print(colore)

colore = "giallo"

print(colore)

numero = 9

# tipi dato
stringa = "ciao" # str

# numerici
intero = 9 # int
decimale = 9.9 # float

# booleani
attivo = True # bool
maggiorenne = False


print(type(intero))
print(type(attivo))

totale = 10 + numero
print(totale)

numero2 = "900"
# totale = 10 + numero2 # errore

# conversione di tipo di dato (casting)
n = int(numero2)
totale = 10 + n
print(totale)

s = numero2 + colore
print(s)

t = "900" + "30"
print(t)

# sequenze
lista = [1,2,3] # list
lista = ["pera", "mela", "banana"]
tupla = (1, "pippo", True) # tuple
r = range(10) # range

print(type(lista))
print(type(tupla))
print(type(r))

# mapping
baggio = {
    "nome": "Roberto",
    "cognome": "Baggio",
    "anni": 54
} # dict (dictionary)

# none
x = None
x = "" # stringa vuota (non è None)
x = 0 # zero (non è None)
x = [] # lista vuota (non è None)

# RARI
# set
insieme = {"ciao","io","lui"} # set

# byte
b = b"ciao" # byte
b = bytearray(5)