import numeri

a = int(input("inserisci numero a: "))
b = int(input("inserisci numero b: "))

risultato_somma = numeri.somma(a, b)
risultato_prodotto = numeri.prodotto(a, b)
controllo_pari = numeri.è_pari(a)

print(risultato_somma)
print(risultato_prodotto)
print(controllo_pari)