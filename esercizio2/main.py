
from stringhe import conta_caratteri, inverti

import stringhe
testi = ["Python è fantastico", "Hello World", "Moduli e Package"]

for testo in testi:
    print(f"Testo: '{testo}'")
    print(f"  Caratteri:  {conta_caratteri(testo)}")
    print(f"  Invertita:  {inverti(testo)}")
    print(f"  Maiuscolo:  {stringhe.in_maiuscolo(testo)}")
    print(f"  Vocali:     {stringhe.conta_vocali(testo)}")
    print()

print(f"  'fantastico' in primo testo: {stringhe.contiene_parola(testi[0], 'fantastico')}")
print(f"  'java' in primo testo:       {stringhe.contiene_parola(testi[0], 'java')}")
