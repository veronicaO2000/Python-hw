#File:       Data.py

#Purpose:    Contains the latitudes and longitude

france_latlong = {}

# open france lat long file
france_lat_long_file = open("france-latlong.txt")

for input_line in france_lat_long_file:
    input_line = input_line.strip()

    if input_line != "" and input_line[0] != "#":
        if "," in input_line:
            input_line = input_line.replace(",", "")
                
        city_info = input_line.split(' ')
        france_latlong[city_info[0]] = {}

        france_latlong[city_info[0]]['lat'] = float(city_info[-2])
        france_latlong[city_info[0]]['long'] = float(city_info[-1])

france_lat_long_file.close()