from conversioni import lunghezza, peso, temperatura

print("=== Conversioni di lunghezza ===")
print(f"  1500 m → {lunghezza.metri_in_chilometri(1500)} km")
print(f"  5 km  → {lunghezza.chilometri_in_metri(5)} m")
print(f"  100 m → {lunghezza.metri_in_miglia(100)} miglia")
print(f"  30 cm → {lunghezza.centimetri_in_pollici(30)} pollici")

print("\n=== Conversioni di peso ===")
print(f"  2.5 kg → {peso.kg_in_grammi(2.5)} g")
print(f"  750 g  → {peso.grammi_in_kg(750)} kg")
print(f"  70 kg  → {peso.kg_in_libbre(70)} lb")

print("\n=== Conversioni di temperatura ===")
print(f"  100°C → {temperatura.celsius_in_fahrenheit(100)}°F")
print(f"  32°F  → {temperatura.fahrenheit_in_celsius(32)}°C")
print(f"  0°C   → {temperatura.celsius_in_kelvin(0)} K")
