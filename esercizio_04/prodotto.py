import validatori


def inserisci_prodotto(nome, codice, prezzo, quantita):
    errori = []

    if not validatori.stringa_non_vuota(nome):
        errori.append("Il nome prodotto non può essere vuoto.")

    if not validatori.codice_prodotto_valido(codice):
        errori.append("Codice non valido (deve avere 6 caratteri).")

    if not validatori.prezzo_valido(prezzo):
        errori.append("Prezzo non valido (deve essere maggiore di zero).")

    if not validatori.numero_positivo(quantita):
        errori.append("Quantità non valida (deve essere maggiore di zero).")

    if len(errori) > 0:
        print("Inserimento fallito:")
        for e in errori:
            print(" -", e)
    else:
        print("Prodotto", nome, "inserito con successo!")


inserisci_prodotto("Tastiera meccanica", "KB0042", 89.99, 15)
inserisci_prodotto("", "TROPPOLUNGO", -5, 0)
