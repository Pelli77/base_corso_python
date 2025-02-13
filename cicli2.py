#while
i = 1
while i < 6:
    print(i)
    i += 1

#break    
i = 1  
while i < 6:
    print(i)
    if i == 3:
        break
    
i += 1

# continue
i = 1  
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# print("CTRL+C per uscire...")
# while True:
#     i += 1

# list comprehension (da aggiungere a cicli.py) - altro ciclo for per creare liste da altre liste
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for f in fruits:
    if "a" in f:
        newlist.append(f)
print(newlist)

# alternativa al ciclo sopra
# sintassi
# newlist = [expression for item in iterable if condition == True]
newlist = [f for f in fruits if "a" in f] 



