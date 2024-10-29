import requests

def get_data(year):
    """
    Retrieves real-time electricity production data for a specified year from the Energidataservice API.

    Parameters:
    - year (int): The target year for which data should be fetched (e.g., 2024).
    - limit (int): The max number of lines to get (defaut=100).

    Returns:
    - requests.Response: The HTTP response object from the API request, which contains the data for the specified year.
    """
    url = 'https://api.energidataservice.dk/dataset/ElectricityProdex5MinRealtime'

    params = dict(
        offset=0,
        start=f"{year}-01-01T00:00",
        end=f"{year}-12-31T00:00",
        sort="Minutes5UTC DESC",
        limit=0
    )
    print(f"\nFetching Energi data for {year}...")
    return requests.get(
        url=url,
        params=params
    )