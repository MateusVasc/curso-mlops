import pandas as pd
import glob

def data_append():
    path = "/home/matt/meu_projeto_ml/data/raw"
    path_pattern = path + "/*.parquet.gzip"

    path_list = glob.glob(path_pattern)
    df_list = []

    for file in path_list:
        df = pd.read_parquet(file)
        df_list.append(df)

    df_appended = pd.concat(df_list, ignore_index=True)
    path_to_save = "/home/matt/meu_projeto_ml/data/processed/"
    df_appended.to_parquet(path_to_save+"df_appended.parquet.gzip", compression="gzip")