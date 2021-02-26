import operator

import practica1


if __name__ == '__main__':
    texto = "La noche cae, brumosa ya y morada.  Vagas claridades malvas y verdes perduran tras la torre de la iglesia.  El camino sube, lleno de sombras, de campanillas, de fragancia de hierba,  de canciones, de cansancio y de anhelo."
    textoaux = "SECRETO DE UNO SECRETO SEGURO"

    print("\n\n-------------PRIMEROS 3 EJERCICIOS-------------\n\n")
    probLetra, frecAbs, letrasDif = practica1.ejercicio_1(texto, "d")

    print("La probabilidad de la letra 'd' es: " + str(probLetra))
    print("La frecuencia absoluta del texto es: " + str(frecAbs))
    print("La entropía del texto es: " + str(practica1.ejercicio_2(letrasDif)))
    letrasPro = practica1.ejercicio_3(letrasDif.copy())
    letrasPro = sorted(letrasPro.items(), key=operator.itemgetter(1), reverse=True)
    print("Símbolo      Frencuencia         Probabilidad")
    for letra in enumerate(letrasPro):
        print("'"+letra[1][0]+"'\t\t\t\t" + "'" + str(letrasDif.get(letra[1][0])) +"'" + "  \t\t\t" + "'"+str(letrasPro[letra[0]][1])+"'")

    #EXTRA
    print("\n\n-------------PARTE EXTRA-------------\n\n")
    textoExtra = practica1.divisionEn2(texto)
    frecAbsExtra = practica1.frecuenciaAbsoluta(textoExtra)
    print("La frecuencia absoluta del texto es: " + str(frecAbsExtra))
    print("La entropía del texto es: " + str(practica1.ejercicio_2(textoExtra)))
    letrasProExtra = practica1.ejercicio_3(textoExtra.copy())
    letrasProExtra = sorted(letrasProExtra.items(), key=operator.itemgetter(1), reverse=True)
    print("Símbolo      Frencuencia         Probabilidad")
    for letra in enumerate(letrasProExtra):
        print("'"+letra[1][0]+"'\t\t\t" + "'" + str(textoExtra.get(letra[1][0])) +"'" + "    \t\t\t" + "'"+str(letrasProExtra[letra[0]][1])+"'")








