import json
import random


def ladda_citat_fran_fil(fil):
    f=open (fil, "r", encoding="utf-8")
    citat_dict=json.load(f)

    return citat_dict

def alla_citat(Citat):
    for i in range(len(Citat)):
        print(Citat[i-1]['citat'])




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




def lagg_till_citat(citatlista):
    nycitat = (input("Vad har Edward sagt nu? "))
    citatlista.append(nycitat)
    return citatlista


def slumpa_citat(citatlista):
    a = random.randint(1,len(citatlista))
    print(citatlista[a-1]['citat'])
    return


def huvudprogram():
    på = True
    Citat=ladda_citat_fran_fil("Data.json")
    while på == True:
        val=input("""
        1. Skriv ut specifikt citat     2. Se citatlista
        3. Lägg till citat              4. Ta bort citat
        5. Slumpa citat                 6. Stäng av program      
        """)
        if val == "1":
            skrivutval = int(input(f"Vilket nr vill du skriva ut 1-{len(Citat)}?"))
            print()
            print(Citat[skrivutval-1]['citat'])
        if val == "2":
            alla_citat(Citat)
        if val == "3":
            Citat = lagg_till_citat(Citat)
        if val == "4":
            break
        if val =="5":
            slumpa_citat(Citat)
        if val == "6":
            på=False

        pass




if __name__ == "__main__":
    huvudprogram()