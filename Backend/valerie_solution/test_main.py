
import csv
import main 

test_data = [
    {'station_id': '1', 'date': '10.0', 'temperature_c': '15'},
    {'station_id': '1', 'date': '10.1', 'temperature_c': '0'},
    
    {'station_id': '2', 'date': '10.0', 'temperature_c': '20'},
    {'station_id': '2', 'date': '10.1', 'temperature_c': '10'},
    {'station_id': '2', 'date': '10.2', 'temperature_c': '20'},
    {'station_id': '2', 'date': '10.3', 'temperature_c': '10'},

    {'station_id': '3', 'date': '10.0', 'temperature_c': '15'},
    {'station_id': '3', 'date': '10.1', 'temperature_c': '20'},
    {'station_id': '3', 'date': '10.2', 'temperature_c': '15'},
    {'station_id': '3', 'date': '10.3', 'temperature_c': '20'}
    ]

def test_lowest_temp() -> None:
    assert main.lowest_temp(test_data) == ('1', '10.1')

def test_set_of_stations() -> None:
    assert main.make_set_of_stations(test_data) == {'1','2','3'}

def test_fluctuation() -> None:
    unique_stations = set(row['station_id'] for row in test_data)

    start_date = None
    end_date = None
    assert main.fluctuation(unique_stations, test_data, start_date, end_date) == '2'

    start_date = 10.0 
    end_date = 10.1 
    assert main.fluctuation(unique_stations, test_data, start_date, end_date) == '1'

    start_date = 5 
    end_date = 9 
    assert main.fluctuation(unique_stations, test_data, start_date, end_date) == None
