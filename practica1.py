
import math
import operator

#Con esta funcion, recibimos como parámetro el texto que queremos analizar y la letra de la cual queremos sacar la
#probabiliad. Además, devolvemos en forma de tupla, tanto la frencuencia absoluta de la frase, como la probabilidad de la
#letra pasada como parámetro

def letras(texto):
    letrasDiferen = dict()
    for caracter in texto:
        if caracter in letrasDiferen.keys():
            letrasDiferen[caracter] = letrasDiferen[caracter] + 1
        else:
            letrasDiferen[caracter] = 1
    return letrasDiferen

def frecuenciaAbsoluta(letrasDiferen):
    frecuenciaAbs = sum(letrasDiferen.values())
    return frecuenciaAbs

def probabilidadDeLetra(letrasDiferen, frecuenciaAbs, letra):
    probabilidadLetra = letrasDiferen[letra] / frecuenciaAbs
    return probabilidadLetra

def letrasProbabilidad(letrasDiferen):
    f = frecuenciaAbsoluta(letrasDiferen)
    for caracter in letrasDiferen:
        letrasDiferen[caracter] = probabilidadDeLetra(letrasDiferen, f, caracter)
    return letrasDiferen

def ejercicio_1(texto, letra):
    letrasDiferen = letras(texto)
    frecuenciaAbs = frecuenciaAbsoluta(letrasDiferen)
    probabilidadLetra = probabilidadDeLetra(letrasDiferen, frecuenciaAbs, letra)
    return probabilidadLetra, frecuenciaAbs, letrasDiferen

def ejercicio_2(letrasDiferen):
    entropia:float = 0
    for caracter in letrasDiferen:
        p = probabilidadDeLetra(letrasDiferen, frecuenciaAbsoluta(letrasDiferen), caracter)
        entropia += p * math.log2(1/p)
    return entropia

def ejercicio_3(letrasDiferen):
    return letrasProbabilidad(letrasDiferen)

def divisionEn2(texto):
    indice = 0
    textoprueba = dict()
    while indice < len(texto)-1:
        letra = texto[indice] + texto[indice+1]
        if letra in textoprueba:
            textoprueba[letra] = textoprueba[letra] + 1
        else:
            textoprueba[letra] = 1
        indice += 2
    return textoprueba