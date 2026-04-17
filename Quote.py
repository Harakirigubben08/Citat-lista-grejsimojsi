import json
import random
på=True

def ladda_citat_fran_fil(fil):
    f=open (fil, "r", encoding="utf-8")
    citat_dict=json.load(f)

    return citat_dict


def spara_citat_till_fil(citatlista, filnamn):
    """
    Sparar alla citat till en textfil.
    
    Parametrar:
        citatlista (list): Listan med citat som ska sparas
        filnamn (str): Namnet på filen att skriva till
    """
    # TODO: Implementera funktionen
    # Tips: Använd open() med "w"
    # Tips: Loop'a igenom listan och skriv varje citat + "\n"
    pass


def visa_alla_citat(citatlista):
    """
    Skriver ut alla citat med numrering.
    
    Parametrar:
        citatlista (list): Listan med citat som ska visas
    """
    # TODO: Implementera funktionen
    # Tips: Använd enumerate() för att få index
    # Tips: Använd strip() för att ta bort radbrytningar
    pass


def lagg_till_citat(citatlista):
    """
    Lägger till ett nytt citat i listan.
    Användaren får mata in citat och författare.
    
    Parametrar:
        citatlista (list): Listan som citatet ska läggas till i
    
    Returnerar:
        bool: True om citatet lades till, False annars
    """
    # TODO: Implementera funktionen
    # Tips: Använd input() för att fråga efter citat och författare
    # Tips: Formatet bör vara "Citatet - Författare"
    pass


def slumpa_citat(citatlista):
    """
    Visar ett slumpmässigt citat från listan.
    
    Parametrar:
        citatlista (list): Listan att välja citat från
    """
    # TODO: Implementera funktionen
    # Tips: Använd random.randint() eller random.choice()
    # Tips: Kontrollera att listan inte är tom först
    pass


def huvudprogram():
    while på == True:
        val=input("""
        1. Skriv ut specifikt citat     2. Se citatlista
        3. Lägg till citat              4. Ta bort citat
        5. Slumpa citat         
        """)
        Citat=ladda_citat_fran_fil("Data.json")
        if val == "1":
            skrivutval = int(input(f"Vilket nr vill du skriva ut 1-{len(Citat)}?"))
            print()
            print(Citat[skrivutval-1]['citat'])

        # TODO: Implementera huvudprogrammet
        # 1. Ladda befintliga citat med ladda_citat_fran_fil()
        # 2. Skapa en while-loop som visar menyn
        # 3. Hantera användarens val med if/elif/else
        # 4. Vid val 2: lägg till citat och spara med spara_citat_till_fil()
        # 5. Vid val 4: avsluta loopen
        pass




if __name__ == "__main__":
    huvudprogram()