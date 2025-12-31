prijzen={
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}
aanbieding = prijzen["aardbei"] * 0.8
# Het volgende punt is inconsistent: de berekening "aanbieding" is op basis van de waarde van "aardbei", 
# maar in "reclame_tekst" staat "vanille-ijs". Niet aangepast, omdat het zo in de opdracht staat. 
reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}")
# Het volgende punt vond ik verwarrend, omdat een bedrag normaal gesproken 2 decimalen heeft, maar in de opdracht staat: 
# "Op de open plek na de dubbele punt plaatst u DE INDEX DIE HOORT BIJ de eerste nul na de KOMMA" (komma = punt??). 
# Dat betekent dan dus dat de output exclusief (tot, niet t/m) die 0 is. 
# Output inclusief die 0 en dus met 2 decimalen zou het de index 63 zijn ;)
reclame_tekst2 = reclame_tekst[:62]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = (reclame_tekst3.split(" "))
# In de volgende opdrachten staat niet dat er iets verwijderd moet worden, dus heb ik alles laten staan.
# Hierdoor krijg je dus natuurlijk drie resultaten achter elkaar. Ik weet niet of dit zo de bedoeling was,
# maar zo stond het er letterlijk ;)
for el in reclame_tekst4:
    print(el)
for el in reclame_tekst4:
    print(el.lower())
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())