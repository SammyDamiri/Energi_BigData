import energydata
import file_utils
import transform


def run(year):
    response = energydata.get_data(year)
    file_utils.save_as_csv(response, 'Data/response_data')
    transform.exchange_germany("Data/response_data.csv")
    transform.total_consumption("Data/response_data.csv")


if __name__ == "__main__":
    year = input("\nEnter a year to get data for: ")
    run(year)
