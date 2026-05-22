def filtra_per_anno(veicoli, anno_minimo):
    return [v for v in veicoli if v.anno >= anno_minimo]


def prendi_anno(veicolo):
    return veicolo.anno

def ordina_per_anno(veicoli):
    return sorted(veicoli, key=prendi_anno)


def stampa_lista(veicoli):
    i = 1
    for v in veicoli:
        print(i, v)
        i = i + 1