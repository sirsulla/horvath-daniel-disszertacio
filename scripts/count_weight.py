import pandas as pd

df_edges = pd.read_excel('edges.xlsx')
df_nodes = pd.read_excel('nodes.xlsx')

# Biztosítsuk, hogy a 'weight' oszlop numerikus legyen és ne tartalmazzon NaN-t (üres mezőt)
df_nodes['weight'] = pd.to_numeric(df_nodes['weight'], errors='coerce').fillna(0).astype(int)
df_edges['weight'] = pd.to_numeric(df_edges['weight'], errors='coerce').fillna(0).astype(int)

# A df_edges oszlopok összeadása a df_nodes megfelelő soraira
for index, row in df_edges.iterrows():
    source = row['source']
    target = row['target']
    weight = row['weight']
    
    # source_id-hoz tartozó sor frissítése
    df_nodes.loc[df_nodes['id'] == source, 'weight'] += weight
    
    # target_id-hoz tartozó sor frissítése
    df_nodes.loc[df_nodes['id'] == target, 'weight'] += weight

print(df_nodes.head())
print(df_nodes['weight'].sum())

# Opcionális - Exportálás xlsx formátumban
# df_nodes.to_excel('nodes_counted.xlsx', index=False)