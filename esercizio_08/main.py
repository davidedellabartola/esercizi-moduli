from veicolo import Veicolo
import supporto

veicoli = [
    Veicolo("Fiat", "500", 2019),
    Veicolo("Toyota", "Yaris", 2015),
    Veicolo("BMW", "Serie 3", 2022),
    Veicolo("Volkswagen", "Golf", 2018),
    Veicolo("Tesla", "Model 3", 2021),
]

print("=== Tutti i veicoli ===")
for v in veicoli:
    print(f"\n{v}")
    v.mostra_info()

print("\n=== Veicoli dal 2020 in poi ===")
recenti = supporto.filtra_per_anno(veicoli, 2020)
supporto.stampa_lista(recenti)

print("\n=== Veicoli ordinati per anno ===")
ordinati = supporto.ordina_per_anno(veicoli)
supporto.stampa_lista(ordinati)
