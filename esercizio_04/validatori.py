def stringa_non_vuota(valore):
    if len(valore) == 0:
        return False
    return True


def numero_positivo(valore):
    if valore > 0:
        return True
    return False


def eta_valida(eta):
    if eta >= 0 and eta <= 120:
        return True
    return False


def email_valida(email):
    if "@" in email:
        return True
    return False


def password_valida(password):
    if len(password) >= 8:
        return True
    return False


def prezzo_valido(prezzo):
    if prezzo > 0:
        return True
    return False


def codice_prodotto_valido(codice):
    if len(codice) == 6:
        return True
    return False
