import os
import csv

class Country(object):

    def __init__(self, name, code, lng, lat):
        self.name = name
        self.code = code
        self.lng = lng
        self.lat = lat

def load_countries():
    path = os.path.join('countries.csv')
    if os.path.exists(path):
        countries = []
        with open(path, 'r') as csv_fh:
            country_reader = csv.reader(csv_fh, delimiter=',')
            next(country_reader, None) # ignore the header in the file
            # Generate a list of countries
            for row in country_reader:
                # if a country does not have a lng or lat ignore it.
                if row[2].upper() == 'NONE' or row[3].upper() == 'NONE':
                    print(
                        'Ignoring {} it has no lng or lat values, '
                        'we cannot put this on the map.'.format(
                            row[0]
                        )
                    )
                    continue
                countries.append(
                    Country(
                        name=row[0].lower(),
                        code=row[1].upper(),
                        lng=float(row[2]),
                        lat=float(row[3])
                    )
                )
        return countries
    else:
        raise print('Cannot find country.csv, make sure this file is in project root')
