
def conta_caratteri(stringa):
    return len(stringa)


def in_maiuscolo(stringa):
    return stringa.upper()


def contiene_parola(stringa, parola):
    return parola.lower() in stringa.lower()


def inverti(stringa):
    return stringa[::-1]


def conta_vocali(stringa):
    return sum(1 for c in stringa.lower() if c in "aeiou")
