import pandas as pd


def exchange_germany(file):

    df = pd.read_csv(file)

    total_exchange_germany_dk1 = df[df['PriceArea'] == 'DK1']['ExchangeGermany'].sum()
    total_exchange_germany_dk2 = df[df['PriceArea'] == 'DK2']['ExchangeGermany'].sum()

    print(f"\nDK1 Exchange with Germany: {total_exchange_germany_dk1} MW")
    print(f"DK2 Exchange with Germany: {total_exchange_germany_dk2} MW")
    print(f"Total Exchange with Germany: {total_exchange_germany_dk1 + total_exchange_germany_dk2} MW\n")


def total_consumption(file):

    df = pd.read_csv(file)

    plant_production = df[['ProductionLt100MW', 'ProductionGe100MW']].sum().sum()
    wind_production = df[['OffshoreWindPower', 'OnshoreWindPower']].sum().sum()
    solar_production = df['SolarPower'].sum()
    total_exchange = df[['ExchangeGermany', 'ExchangeNetherlands', 'ExchangeGreatBritain', 'ExchangeNorway', 'ExchangeSweden', 'ExchangeGreatBelt', 'BornholmSE4']].sum().sum()

    total_consumption = plant_production + wind_production + solar_production + total_exchange
    wind_production_pct = wind_production / total_consumption * 100
    solar_production_pct = solar_production / total_consumption * 100
    net_export_pct = total_exchange / total_consumption * 100

    print("Some consumption and production data for Denmark:")
    print(f"Total Electricity Consumption = {total_consumption} MW")
    print(f"{wind_production_pct:.2f}% of total consumption came from wind production.")
    print(f"{solar_production_pct:.2f}% of total consumption came from solar production.")
    print(f"{net_export_pct:.2f} of total consumption was exported.")
