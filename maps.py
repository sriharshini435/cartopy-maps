


import matplotlib.pyplot as plt
import cartopy.crs as c
import cartopy.feature as cf
import numpy as np

map_data = {
"India": [68.1766, 97.3954, 6.7535, 35.5133],
"United States": [-125.0, -66.9346, 24.3963, 49.3844],
"China": [73.4994, 134.7755, 18.1977, 53.5609],
"Brazil": [-73.9872, -34.7299, -33.7473, 5.2718],
"Australia": [113.3389, 153.5695, -43.6346, -10.6682],
"Canada": [-141.0, -52.6176, 41.6766, 83.1139],
"Russia": [19.6604, 180.0, 41.1851, 81.8587],
"South Africa": [16.2817, 32.8939, -34.8192, -22.1266],
"Germany": [5.8663, 15.0419, 47.2701, 55.0581],
"Japan": [122.9346, 153.9867, 24.3963, 45.5515]
}

def map_plot(data, country):
    fig = plt.figure(figsize=(7,7))
    ax = plt.axes(projection = c.PlateCarree() )
    ax. set_extent (map_data[country], crs = c.PlateCarree())
    ax.add_feature(cf.OCEAN)
    ax.add_feature(cf.LAND)
    ax.add_feature(cf.COASTLINE)
    ax.add_feature(cf.BORDERS, edgecolor = 'red' , linestyle = "--")
    ax.add_feature(cf.RIVERS)
    ax.add_feature(cf.LAKES,color = 'green')
    plt.title(f"Map of {country}")
    plt.show()
country = input("enter the country:")
if country in map_data.keys():
    map_plot(map_data, country)
else:
    print("Country not found")




