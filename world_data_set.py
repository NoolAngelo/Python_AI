import pandas as pd
df = pd.read_csv('world_educational_data.csv')

ship_1 = df[(df['Shipment type']=='1 Day')]