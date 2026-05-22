import io_module
import logica

VOCI_MENU = [
    "Area rettangolo",
    "Perimetro rettangolo",
    "Converti Celsius → Fahrenheit",
]


def esegui_scelta(scelta):
    if scelta == 1:
        b = io_module.chiedi_float("  Base (m): ")
        h = io_module.chiedi_float("  Altezza (m): ")
        io_module.stampa_risultato("Area", logica.area_rettangolo(b, h))

    elif scelta == 2:
        b = io_module.chiedi_float("  Base (m): ")
        h = io_module.chiedi_float("  Altezza (m): ")
        io_module.stampa_risultato("Perimetro", logica.perimetro_rettangolo(b, h))

    elif scelta == 3:
        c = io_module.chiedi_float("  Temperatura in °C: ")
        io_module.stampa_risultato("Fahrenheit", logica.celsius_in_fahrenheit(c))


def main():
    while True:
        io_module.mostra_menu(VOCI_MENU)
        scelta = io_module.chiedi_scelta(len(VOCI_MENU))
        if scelta == 0:
            break
        esegui_scelta(scelta)

