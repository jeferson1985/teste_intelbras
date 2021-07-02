# -*- coding: utf-8 -*-
import pandas as pd
import funcoes

arquivo = pd.read_csv('arquivo-desafio.csv', delimiter=';')

# Metodo para remoção das linhas que não possuem cargo 
arquivo.drop(arquivo[arquivo['CATEGORIA'].isna()].index, inplace=True)
# Metodo para transformar todas os valores em UPPERCASE
arquivo = funcoes.to_upper_case(arquivo)
# Metodo para retirar a frase ' HORAS SEMANAIS' na coluna JORNADA
arquivo['JORNADA'] = arquivo['JORNADA'].str.replace(" HORAS SEMANAIS", "")
# Criação de coluna concatenando NOME_FUNCIONARIO com SITUAÇÃO
arquivo["NOME_SITUACAO"] = arquivo["NOME_FUNCIONARIO"] + " | " + arquivo["SITUAÇÃO"]
# Quantidade de pessoas com o sobrenome SILVA
silvas = (arquivo["NOME_FUNCIONARIO"].str.contains("SILVA")).sum()
# Quantidade de linhas que o primeiro nome é ANA
anas = (arquivo["NOME_FUNCIONARIO"].str.match("^ANA")).sum()
# Quantidade de cargos diferentes
quant_cargos = len(arquivo.groupby(['CARGO']).mean())
# Quantidade de pessoas que trabalham somente 40h semanais
quant_40 = (arquivo.groupby('JORNADA').JORNADA.count()).get("40")
# Porcentagem de pessoas que trabalham 40h semanais
porc_40 = quant_40 * 100 / len(arquivo)
# Metodo para trazer a linha com DATA_ADMISSAO == "2012-06-15" and DATA_DESLIGAMENTO == "2012-12-04"
# Porém quando foi limpado as linhas das pessoas que não possuem JORNADA a única linha que trouxe
# Era 30 da funcionária ALESSANDRA BOMBARDA MÜLLER 
data_admissao = arquivo.query('DATA_ADMISSAO == "2012-06-15" and DATA_DESLIGAMENTO == "2012-12-04"')

print(data_admissao)
print(anas)

