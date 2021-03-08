import pandas as pd
import pyarrow.parquet as pq


table = pq.read_table('data/aiheroes_recipe.parquet')
df = table.to_pandas()

df.to_csv('data/aiheroes_recipe.csv')
