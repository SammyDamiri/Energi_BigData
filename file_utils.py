import json
import csv


def save_as_json(response, filename):
    """
    Saves API response as a JSON file (Overwrite existing file).

    Parameters:
    - response (requests.Response): The HTTP response from an API request.
    - filename (str): The base filename to save as (without extension).
    """
    if response.status_code == 200:
        filename += ".json"
        data = response.json()

        with open(filename, '+w') as file:
            json.dump(data, file, indent=4)
        print(f"Data has been saved to {filename}")
    else:
        print(f"Request failed with status code: {response.status_code}")


def save_as_csv(response, filename):
    """
    Saves API response as a CSV file (Overwrite existing file).

    Parameters:
    - response (requests.Response): The HTTP response from an API request.
    - filename (str): The base filename to save as (without extension).
    """
    if response.status_code == 200:
        filename += ".csv"
        data = response.json()

        if 'records' in data:
            records = data['records']

            with open(filename, mode='+w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=records[0].keys())
                writer.writeheader()
                writer.writerows(records)

            print(f"Data has been saved to {filename}")
        else:
            print("Unexpected data structure in response.")
    else:
        print(f"Request failed with status code: {response.status_code}")
