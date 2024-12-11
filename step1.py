import pandas as pd

# Liste des fichiers CSV à charger
files = ['carac.csv', 'lieux.csv', 'veh.csv', 'vict.csv']

# Lire le premier fichier
df = pd.read_csv('data/'+files[0], sep=';', encoding='UTF-8')

# Fusionner chaque fichier avec le DataFrame df en utilisant la colonne 'Num_Acc'
for file in files[1:]:
    df_temp = pd.read_csv('data/'+file, sep=';', encoding='UTF-8')
    df = pd.merge(df, df_temp, on='Num_Acc', how='outer')  # 'outer' pour garder toutes les lignes, vous pouvez changer selon votre besoin

# Sauvegarder le DataFrame fusionné dans un nouveau fichier CSV
df.to_csv('merged_data.csv', index=False)

# Afficher un aperçu du DataFrame fusionné
print(df.head())
