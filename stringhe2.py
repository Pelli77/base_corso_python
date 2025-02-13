# concatenazione di stringhe
a = "Ciao"
b = "Mondo"
c = a + " " + b + "!"
print(c)

qta = 9
codice = "xyz123"
prezzo = 9.99

# "Voglio 9 pezzi del prodotto con codice XYZ123 per 9.99 euro."
ordine = "Voglio {} pezzi del prodotto con codice {} per {} euro."
print(ordine.format(qta, codice, prezzo))

# f strings
ordine_completo = f"Voglio {qta * 2} pezzi del prodotto con codice {codice.upper()} per {prezzo} euro."
print(ordine_completo)


txt = "Siamo \"Quelli bravi\"" # escape
txt = 'Siamo "Quelli bravi"'
txt = """
Ciao
sono io

Arrivederci
"""
print(txt)