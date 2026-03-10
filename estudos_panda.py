#instruções de panda para leitura de arquivos JSON

import pandas as pd
import os
import json

# Lê o arquivo JSON e cria um DataFrame
df = pd.read_json(r"C:\Users\azship2\Documents\tst.json")
print(df)

print('\n')

#lê arquivo usando o normalize para transformar o JSON em um DataFrame - para arquivos JSON mais complexos com estruturas aninhadas
with open(r"C:\Users\azship2\Documents\tstnormalized.json") as f:
    data = json.load(f)

df_normalized = pd.json_normalize(data)
print(df_normalized)

print('\n')

#arquivo JSON com lista de objetos - passando a chave da lista para o normalize
with open(r"C:\Users\azship2\Documents\tstListDictionary.json") as D:
    data_list = json.load(D)

df_dic = pd.json_normalize(data_list, record_path='compras', meta = ['id_vendedor', 'id_cliente']) #campo record_path é a chave da lista de objetos que queremos transformar em linhas do DataFrame, e o campo meta são os campos que queremos manter como colunas no DataFrame

print(df_dic)