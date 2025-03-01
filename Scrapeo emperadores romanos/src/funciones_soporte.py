import pandas as pd
import numpy as np
def info_df(dataframe):
    """
    Función que devuelve información general sobre el DatFrame que le pasemos.

    Args:
        df (DataFrame): DataFrame con información que queramos revisar

    Returns:
        DataFrame: DataFrame con información general sobre las columnas del DataFrame que se le ha pasado a la función: tipo de datos, número de
        registros, número de valores nulos, porcentaje de los valores nulos sobre el total
    """
    info_df = pd.DataFrame()
    info_df["Tipo_dato"] = dataframe.dtypes
    info_df["numero_registros"] = [dataframe[elemento].value_counts().sum() for elemento in dataframe]
    info_df["Numero_nulos"] = round(dataframe.isnull().sum())
    info_df["%_nulos"] = round((dataframe.isnull().sum()/dataframe.shape[0])*100, 2)
    return info_df

def limpieza_caracteres(dataframe, columna):
    # Eliminamos los elementos invisibles de los caracteres que lo contienen
    dataframe[columna] = dataframe[columna].apply(lambda x: x.replace("\u200b", "") if "\u200b" in x else x)
    elementos = ["[a]","[d]","[o]","[p]","[w]","[y]","[aa]","[ae]","[m]", "[ab]", "c.", "c. ", "¿", "?","[r]", "[n]", "[z]", "[ac]", "[ad]","(en Italia)"]
    for i in elementos:
	    dataframe[columna] = dataframe[columna].apply(lambda x: x.replace(i, "") if i in x else x)

def limpieza_fechas(dataframe, columna):
     # Eliminamos los "de" dentro de las fechas
    dataframe[columna] = dataframe[columna].str.replace("de", "")