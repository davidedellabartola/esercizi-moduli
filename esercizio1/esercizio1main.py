import esercizio1modulo

a = int(input("inserisci numero a: "))
b = int(input("inserisci numero b: "))

risultato_somma = esercizio1modulo.somma(a, b)
risultato_prodotto = esercizio1modulo.prodotto(a, b)
controllo_pari = esercizio1modulo.è_pari(a)

print(risultato_somma)
print(risultato_prodotto)
print(controllo_pari)