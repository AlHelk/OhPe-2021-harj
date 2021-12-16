from datetime import datetime
import pickle

salit = {"Sali 1": 50, "Sali 2": 45, "Sali 3": 70}
naytokset = []

def lataa_tiedosto():
    with open("jotai.txt", "rb") as tiedosto:
        return pickle.load(tiedosto)

def tallenna_tiedostoon():
    with open("jotai.txt", "wb") as tiedosto:
        pickle.dump(naytokset, tiedosto) 

def tallenna_naytos_listaan(elokuva: str, kesto: int, sali: str, pvm: str, klo: str, varaukset = 0):
    ajankohta = datetime(int(pvm[2]), int(pvm[1]), int(pvm[0]), int(klo[0]), int(klo[1])) 
    vapaat_paikat = salit[sali] - varaukset
    naytoksen_tiedot = (elokuva, kesto, sali, vapaat_paikat, ajankohta)
    naytokset.append(naytoksen_tiedot)

def varaa_paikka(naytos, maara):
    a = list(naytos)
    if a[3] >= maara:
        a[3] -= maara
        b = tuple(a)
        c = naytokset.index(naytos)
        naytokset[c] = b
    else:
        print("Salissa ei ole tarpeeksi tilaa!")
    
def tulosta_naytos(naytos):
    print(f"Elokuva: {naytos[0]}\nKesto: {naytos[1]} minuuttia\nAjankohta: {naytos[4]}\n{naytos[2]}\nVapaita paikkoja: {naytos[3]}")

def lisaa_naytos():
    elokuva = str(input("Anna elokuvan nimi: "))
    kesto = int(input("Elokuvan kesto minuuteissa: "))
    sali = str(input("Valitse sali: "))
    pvm = str(input("Päivämäärä: ")).split(".")
    klo = str(input("Kellonaika: ")).split(":")

    tallenna_naytos_listaan(elokuva, kesto, sali, pvm, klo)

naytokset = lataa_tiedosto()