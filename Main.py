from DataPreparation import *
from Statistics import *
import pandas as pd

df = pd.read_csv('Lipidomics_Annotated_combined.csv')

print(f"Data will be processed...\nShape of the imputted feature table: \t{df.shape}")

df = DropFeatures(df)
df = ReplacingMissingValues(df)
df = Standardization(df)
df = ReplacingFeatureName(df)


print(f"Data is prepared")
print(f"Shape of the cleaned feature table: \t{df.shape}")

# Total patients
white = df.filter(like='W', axis=1)
cortex = df.filter(like='C', axis=1)
temporal = df.filter(like='T', axis=1)
frontal = df.filter(like='F', axis=1)
temporal_white = df.filter(like="TW", axis=1)
temporal_cortex = df.filter(like="TC", axis=1)
frontal_white = df.filter(like="FW", axis=1)
frontal_cortex = df.filter(like="FC", axis=1)

# Healthy patients
control = df.filter(regex="^1", axis=1)
control_cortex = control.filter(like='C', axis=1)
control_white = control.filter(like='W', axis=1)
control_frontal = control.filter(like='F', axis=1)
control_temporal = control.filter(like='T', axis=1)
frontal_white_control = frontal_white.filter(regex="^1", axis=1)
frontal_cortex_control = control_cortex.filter(like='F', axis=1)
temporal_white_control = control_white.filter(like='T', axis=1)
temporal_cortex_control = control_cortex.filter(like='T', axis=1)

#df = unistats(control_frontal, control_temporal)

