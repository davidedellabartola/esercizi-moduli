

def mostra_menu(voci):
    print("\n" + "=" * 35)
    print("       MENU PRINCIPALE")
    print("=" * 35)
    for i, voce in enumerate(voci, start=1):
        print(f"  {i}. {voce}")
    print("  0. Esci")
    print("=" * 35)


def chiedi_scelta(num_voci):
    while True:
        try:
            scelta = int(input("Scelta: "))
            if 0 <= scelta <= num_voci:
                return scelta
            print(f"Inserisci un numero tra 0 e {num_voci}.")
        except ValueError:
            print("Input non valido. Inserisci un numero intero.")


def chiedi_float(messaggio):
    while True:
        try:
            return float(input(messaggio))
        except ValueError:
            print("Valore non valido. Inserisci un numero.")


def stampa_risultato(etichetta, valore):
    print(f"\n  → {etichetta}: {valore:.4g}")
