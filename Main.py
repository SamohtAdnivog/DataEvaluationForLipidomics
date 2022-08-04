from DataPreparation import *
import pandas as pd

df = pd.read_csv('Lipidomics_Annotated_combined.csv')

df = DropFeatures(df)
df = ReplacingMissingValues(df)
df = Standardization(df)
df = ReplacingFeatureName(df)

print(df.head())