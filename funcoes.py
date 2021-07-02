# -*- coding: utf-8 -*-
lista = [
    "NOME_FUNCIONARIO",
    "CARGO",
    "CATEGORIA",
    "NOME_UNIDADE",
    "JORNADA",
    "SITUAÇÃO"
]

def to_upper_case(arquivo):
    for l in lista:
        arquivo[l] = arquivo[l].str.upper()
    return arquivo