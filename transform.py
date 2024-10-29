import pandas as pd

def exchange_germany(file):

    df = pd.read_csv(file)

    total_exchange_germany_dk1 = df[df['PriceArea'] == 'DK1']['ExchangeGermany'].sum()
    total_exchange_germany_dk2 = df[df['PriceArea'] == 'DK2']['ExchangeGermany'].sum()
    total_exchange_germany = df['ExchangeGermany'].sum()

    print(f"\nDK1 Exchange with Germany: {total_exchange_germany_dk1} MW")
    print(f"DK2 Exchange with Germany: {total_exchange_germany_dk2} MW")
    print(f"Total Exchange with Germany: {total_exchange_germany} MW\n")
