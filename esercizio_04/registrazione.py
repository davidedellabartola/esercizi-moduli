import validatori


def registra_utente(nome, email, eta, password):
    print("\n--- Registrazione utente ---")
    errori = []

    if not validatori.stringa_non_vuota(nome):
        errori.append("Il nome non può essere vuoto.")

    if not validatori.email_valida(email):
        errori.append("Email non valida (deve contenere @).")

    if not validatori.eta_valida(eta):
        errori.append("Età non valida (deve essere tra 0 e 120).")

    if not validatori.password_valida(password):
        errori.append("Password troppo corta (minimo 8 caratteri).")

    if len(errori) > 0:
        print("Registrazione fallita:")
        for e in errori:
            print(" -", e)
    else:
        print("Utente", nome, "registrato con successo!")


registra_utente("Mario Rossi", "mario@example.com", 30, "sicura123")
registra_utente("", "emailsbagliata", 200, "corta")
