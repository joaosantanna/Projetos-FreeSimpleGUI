from random import choice

"""
modulo do madlibs que recebe a lista de 
personagens , adjetivos e verbos , monta 
e devolve a frase

entradas :

saidas: uma frase montada ao acaso usando as entradas

"""

personagens = [
    "Bob Esponja",
    "Darth Vader",
    "Chaves",
    "Batman",
    "Goku",
    "Elsa",
    "Shrek",
    "Harry Potter",
    "Lula Molusco",
    "Homer Simpson",
]

adjetivos = [
    "desajeitado",
    "confuso",
    "radiante",
    "atrapalhado",
    "maluco",
    "preguiçoso",
    "falante",
    "dramático",
    "hiperativo",
    "misterioso",
]

verbos = [
    "dançar",
    "gritar",
    "cozinhar",
    "correr",
    "cantar",
    "tropeçar",
    "reclamar",
    "dormir",
    "pular",
    "explodir",
]


def listas_default():
    """
    funçao que retorna as listas default dentro de um dicionario, as chaves
    do dicionario são personagens , verbo e adjetivo , e os valores são os valores
    das respectivas listas defaula

    entrada: nenhuma

    retorno : dicionario contendo as listas de valores default
    """
    listas_padrao = {
        "personagens": personagens,
        "adjetivos": adjetivos,
        "verbos": verbos,
    }
    return listas_padrao


def madlibs(personagens=personagens, adjetivos=adjetivos, verbos=verbos):
    """
    madlibs - função que recebe a lista de personagens , adjetivos e verbos
    para monta a frase e devolver o resultado. Para montar a lista usa a função
    choice do modulo random

    entrada: lista de personagens , lista de adjetivos e lista de verbos. Caso nada
    seja passado usar as lista defaul

    retorno : frase montada com os parametros sorteados

    """
    personagem1 = choice(personagens)
    personagem2 = choice(personagens)
    personagem3 = choice(personagens)
    personagem4 = choice(personagens)
    adjetivo1 = choice(adjetivos)
    adjetivos.remove(adjetivo1)
    adjetivo2 = choice(adjetivos)
    adjetivos.remove(adjetivo2)
    adjetivo3 = choice(adjetivos)
    adjetivos.remove(adjetivo3)
    adjetivo4 = choice(adjetivos)
    verbo1 = choice(verbos)
    verbos.remove(verbo1)
    verbo2 = choice(verbos)
    verbos.remove(verbo2)
    verbo3 = choice(verbos)
    verbos.remove(verbo3)
    verbo4 = choice(verbos)

    madlibs = f"{personagem1} {adjetivo1} decidiu {verbo1} com {personagem2}, mas {personagem3}\
 {adjetivo2} começou a {verbo2}, então {personagem4} {adjetivo3} simplesmente resolveu\
 {verbo3} enquanto {personagem1} {adjetivo4} tentava {verbo4}."

    return madlibs
