# if
a = 300
b = 300

if a > b:
    print("a è maggiore di b")
  

print("ciao")

if a > b:
    print("a maggiore di b")
elif a == b:
    print("a uguale a b")
elif a == 0:
    print("a è 0")
else:
    print("a minore di b")
    

# operatore ternario
# scorciatoia per if else (quando il corpo di if e else stanno su una riga)
print("A") if a > b else print("B")

# equivale a
if a > b:
    print("A")
else:
    print("B")
    
c = 500

if a > b and c > a:
    print("ciao")
    
if "b" in "roberto":
    print("la lettera b si trova in roberto")
    
anni = 25
patente = True

if patente == True:
    if anni >= 21:
        print("Posso bere tanto")
    else:
        print("Meglio che non beva")
else:
    print("Non posso guidare")
    
# match (switch)
status_code = 200
match status_code:
    case 200 | 201:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Errore sconosciuto")