"""
https://github.com/magiclabs/email_screening_question/tree/master/Backend

Assumptions:
- no ordering of csv needed as rows are already in chronological order
"""

import argparse
import csv 

DATA_FILE = 'data.csv'

def main():
    parser = argparse.ArgumentParser(description='weather stats')
    parser.add_argument('--debug', help='print debug data', action='store_true')
    parser.add_argument('--test_data', help='use test data instead of data.csv fir development', action='store_true')
    parser.add_argument('-s', '--start_date', required=True,
                        help='start date range for Part 3', type=float)
    parser.add_argument('-e', '--end_date', required=True,
                        help='end date range for Part 3', type=float)
    args = parser.parse_args()

    if args.end_date < args.start_date:
        print('end date cannot be before start date')
        return False

    if args.test_data:
        data = [
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

    else:
        with open(DATA_FILE) as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

    if args.debug:
        print('first 10 rows of data:')
        for i in range(10):
            print(data[i])

    lowest_temp_pair = lowest_temp(data=data)

    unique_stations = make_set_of_stations(data=data)
    if args.debug:
        print('unique_stations len: {}, data len: {}'.format(len(unique_stations), len(data)))

    most_fluctuation_all_dates = fluctuation(unique_stations=unique_stations, data=data, debug=args.debug)
    
    most_fluctiation_date_range = fluctuation(
        unique_stations=unique_stations, data=data, start_date=args.start_date, end_date=args.end_date, debug=args.debug)

    solution = {'Part 1': lowest_temp_pair, 'Part 2': most_fluctuation_all_dates, 'Part 3': most_fluctiation_date_range}
    
    if args.debug:
        print('solution:', solution)
    
    return solution

def make_set_of_stations(data) -> set:
    return set(row['station_id'] for row in data)

def lowest_temp(data) -> tuple:

    print('calculating lowest temp')

    sorted_by_temp = sorted(data, key = lambda i: float(i['temperature_c']))
    lowest_temp = sorted_by_temp[0]

    print('lowest temp calculation complete: {} temp at {}'.format(
        lowest_temp['temperature_c'], lowest_temp['station_id'], lowest_temp['date']))

    return (lowest_temp['station_id'], lowest_temp['date'])

def fluctuation(unique_stations, data, start_date=None, end_date=None, debug=False) -> str:

    print('calculating fluctionations with date limits: {} {}'.format(start_date, end_date))
    
    station_fluctuation_map = dict.fromkeys(unique_stations, {}) 
    
    if debug:
        print(station_fluctuation_map)

    for row in data:
        date = float(row['date'])
        if start_date and not start_date <= date <= end_date:
            continue
        
        temp = float(row['temperature_c'])
        station = row['station_id']
        
        if not station_fluctuation_map.get(station):
            station_fluctuation_map[station] = {'prev_temp': temp, 'fluctuation': 0}
            continue
        prev_temp = station_fluctuation_map[station]['prev_temp']
        fluctuation = station_fluctuation_map[station]['fluctuation']
        
        if prev_temp:
            fluctuation += abs(temp - prev_temp)

        station_fluctuation_map[station]['prev_temp'] = temp
        station_fluctuation_map[station]['fluctuation'] = fluctuation

    if debug:
        print('station fluctuation map:', station_fluctuation_map)

    station_fluctuation_map_final = {}
    for station in station_fluctuation_map:
        if station_fluctuation_map.get(station):
            station_fluctuation_map_final[station] = station_fluctuation_map.get(station)

    if not station_fluctuation_map_final:
        print('no data between input dates')
        return None

    largest_fluctuation_station = max(
        station_fluctuation_map_final, key=lambda x: station_fluctuation_map_final[x].get('fluctuation'))
    
    print('fluctuation calculation complete: {}'.format(largest_fluctuation_station))

    return largest_fluctuation_station


if __name__ == '__main__':
    main()