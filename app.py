import energydata
import file_utils

response = energydata.get_data(2020)
file_utils.save_as_csv(response, 'Data/response_data')
file_utils.save_as_json(response, 'Data/response_data')
