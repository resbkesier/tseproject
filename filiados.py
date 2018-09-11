# -*- coding: utf-8 -*-
from __future__ import print_function
# Sempre ter o encoding do código na cláusula acima

import zipfile
import requests
import os
# Python 3.5
import pathlib

# Python 2.7
# import errno
#
#
# def mkdir_p(path):
#     try:
#         os.makedirs(path)
#     except OSError as exc:  # Python >2.5
#         if exc.errno == errno.EEXIST and os.path.isdir(path):
#             pass
#         else:
#             raise


# webbrowser.open_new_tab('http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/filiados_{}_{}.zip'.
# format(partidos[i], estados[x]))
partidos = ["avante", "dem", "novo", "pen", "pc_do_b", "pcb", "pco", "pdt", "phs", "pmdb", "pmb", "pmn", "pp", "ppl",
            "pps", "pr", "prb",
            "pros", "prp", "prtb", "psc", "psd", "psdb", "psb", "psdc", "psl", "psol", "pstu", "pt", "ptb", "ptc",
            "pode", "pv", "rede", "sd"]

estados = ["ac", "am", "ap", "ba", "ce", "df", "es", "go", "ma", "mg", "ms", "mt", "pa", "pb", "pe", "pi", "pr", "rj",
           "rn", 'ro', "rr", "rs", "sc", "se", "sp"]

for i in range(len(partidos)):

    for x in range(len(estados)):
        # download dos arquivos do site do tse

        # Define o nome do zip uma única vez, princípio pythônico (DRY - Don't Repeat Yourself)
        zip_file_name = 'filiados_{}_{}.zip'.format(partidos[i], estados[x])

        site_tse = 'http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/{}'.format(zip_file_name)
        r = requests.get(site_tse)
        with open(zip_file_name, 'wb') as code:
            code.write(r.content)
        print(site_tse)

        # barra de progresso (desativada por causar lentidão no download)
        # for d in tqdm(range(len(teste))):
        # sleep(0.01)

        # Extraindo arquivos para uma pasta
        zip_ref = zipfile.ZipFile(zip_file_name)

        # Trabalhando paths com listas para ficar independente de Sistema Operacional
        output_path_structure = ['.', 'Projetos', 'Codigos avulsos', 'Listas Filiados']
        # Sempre use os.path.join(), o operador * (splat) faz a lista funcionar como múltiplos argumentos
        extract_target_path = os.path.join(*output_path_structure)

        # python 3.5
        pathlib.Path(extract_target_path).mkdir(parents=True, exist_ok=True)

        # Python 2.7
        # mkdir_p(extract_target_path)

        # Extract!
        zip_ref.extractall(extract_target_path)
        zip_ref.close()
