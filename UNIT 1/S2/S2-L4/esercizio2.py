import math

def perimetro_quadrato(lato):
    quadrato=perimetro_quadrato
    return lato * 4
def perimetro_cerchio(raggio):
    cerchio=perimetro_cerchio
    return math.pi * raggio * 2
def perimetro_rettangolo(lunghezza, larghezza):
    rettangolo=perimetro_rettangolo
    return (lunghezza + larghezza) * 2


scelta=input("Scegli di quale figura geometrica vuoi calcolare il perimetro (quadrato, cerchio, rettangolo):   ")

if scelta == "quadrato":
    lato = float(input("inserisci la lunghezza del lato:  "))
    perimetro=perimetro_quadrato(lato)
    print(f"il perimetro del quadrato è: {perimetro}")

elif scelta == "cerchio":
    raggio = float(input("Inserisci il raggio del cerchio:  "))
    perimetro=perimetro_cerchio
    print(f"il perimetro del cerchio è:  {math.pi * raggio * 2}")

elif scelta == "rettangolo":
    lunghezza = float(input("inserisci la lunghezza del rettangolo:  "))
    larghezza = float(input("inserici la larghezza del rettangolo:  "))
    perimetro=perimetro_rettangolo
    print(f"il perimetro del rettangolo è:  {(lunghezza + larghezza) * 2}")

else:
    print("penso proprio che dovresti prenotare una visita dall'oculista...")