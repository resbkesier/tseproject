# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import csv
# Comment

def retorna_arquivos(caminho):
    for root, dirs, files in os.walk(caminho):
        if len(files) > 0:
            arquivos_desejados = filter(
                lambda file_name: file_name.startswith('filiados_') and file_name.endswith('.csv'), files)
            arquivos_com_caminho = [os.path.join(root, arquivo) for arquivo in arquivos_desejados]
            return arquivos_com_caminho


def adiciona_dados_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, encoding='iso-8859-1') as csvfile:
        conteudo = csv.reader(csvfile, delimiter=';')
        primeira_linha = True
        dados_primeira_linha = None
        for row in conteudo:
            if not primeira_linha:
                dados.append(row)
            else:
                dados_primeira_linha = row
                primeira_linha = False
        csvfile.close()
    return dados, dados_primeira_linha


def retorna_todos_dados(lista_de_arquivos):
    dados = []
    for arquivo in lista_de_arquivos:
        dados, dados_primeira_linha = adiciona_dados_arquivo(dados, arquivo)
    return dados, dados_primeira_linha


def retorna_dados_ordenados(dados):
    # ordena por partido e por estado
    return sorted(dados, key=lambda filiado: filiado[4] + filiado[6])


def grava_dados(nome_arquivo, dados, dados_primeira_linha):
    with open(nome_arquivo, 'w', encoding='iso-8859-1') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows([dados_primeira_linha])
        writer.writerows(dados)
        arquivo.close()


if __name__ == '__main__':
    dados, dados_primeira_linha = retorna_todos_dados(retorna_arquivos('Projetos'))
    dados_ordenados = retorna_dados_ordenados(dados)

    grava_dados('ordenados.csv', dados_ordenados, dados_primeira_linha)
