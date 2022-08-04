import pandas as pd
import numpy as np
from scipy.stats import zscore

# Dropping Features with too few signals
def DropFeatures(file, threshold=0.4):
    file_input_shape = file.shape
    file.replace('NAN', np.nan, inplace=True)
    thd = file.shape[1] * threshold
    file.dropna(axis=0, thresh=thd, inplace=True)
    print(f'Dropped features: {file.shape[0] / file_input_shape[0]}')
    return file

def ReplacingMissingValues(file, minimizationfactor=0.2):
    file.set_index('Mebol', inplace=True)
    file_inputted = file.T
    for element in range(len(file)):
        elm = file.iloc[element, :].astype(float)
        min_elm05 = np.min(elm) * minimizationfactor
        file_inputted[elm.name].replace(np.nan, min_elm05, inplace=True)
        file_inputted = file_inputted.astype('float')
    file = file_inputted
    print(f'Values replaced by {100* minimizationfactor}% of the least abundant signal of each feature.')
    return file

def Standardization(df):
    df = zscore(df, axis=0)
    print(f'Data are transformed by zscore')
    return df

def ReplacingFeatureName(df):
    ind1, newcol = [], []
    metabol = df.columns
    letters = np.array(list('abcdefghijklmnopqrstuvwxyz'))
    for element in metabol:
        ind1.append(element.split(' [')[0])
    ind1 = pd.DataFrame(ind1, columns=['old'])
    lettervec = letters[ind1['old'].groupby(ind1['old']).cumcount()]
    for line, letter in zip(ind1['old'], lettervec):
        newcol.append(line + " " + letter)
    df.columns = newcol
    newind = []
    for element in df.index:
        newind.append(element.strip())
    df.index=newind
    print(f'Feature names are changed for better visualization')
    return df.T
