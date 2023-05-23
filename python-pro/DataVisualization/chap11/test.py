import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
print(data.columns)
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
ele = list(data["ELEV"])


def color_by_ele(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


location = list(data["LOCATION"])
maps = folium.Map(location=[43.72576808396264, -79.29017544986058], zoom_start=6, titles="Mapbox Bright")
fgv = folium.FeatureGroup(name='Volcanoes')
for lt, ln, na, lo, fu in zip(lat, lon, name, location, ele):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=na + lo, icon=folium.Icon(color=color_by_ele(fu))))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
maps.add_child(fgv)
maps.add_child(fgp)
maps.add_child(folium.LayerControl())
maps.save('map1.html')
