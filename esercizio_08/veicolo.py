class Veicolo:
    
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def mostra_info(self):
        """Stampa le informazioni del veicolo in modo leggibile."""
        print(f"  Marca:   {self.marca}")
        print(f"  Modello: {self.modello}")
        print(f"  Anno:    {self.anno}")

    def __str__(self):
        return f"{self.anno} {self.marca} {self.modello}"
