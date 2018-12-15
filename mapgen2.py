#!/usr/bin/python
import gmaps
import gmaps.geojson_geometries
from ipywidgets.embed import embed_minimal_html

"""
This script generates a heatmap based on a formatted CSV file.
It uses the google maps API and all of our IP data.

"""

IPFILE = 'iplocs.csv'
f = open(IPFILE)
locs = []
lc = 1

for line in f:
    if 'latitude,' in line:
        continue
    data = line.split(',')
    loc = (float(data[0]), float(data[1]))
    if locs.count(loc) > 100:
        continue
    locs.append(loc)
    print('Line %d processed...' % (lc))
    lc += 1
f.close()
print('Successfully processed %d locations.' % (len(locs)))

gmaps.configure(api_key='')
mlayout = {'width': '1050px', 'height': '650px'}
fig = gmaps.figure(map_type='HYBRID', layout=mlayout)

hmap2 = gmaps.heatmap_layer(locs)
hmap2.max_intensity = 4
hmap2.point_radius = 0.8
hmap2.dissipating = False

hmap = gmaps.heatmap_layer(locs)
hmap.max_intensity = 125
hmap.point_radius = 1.7
hmap.dissipating = False

fig.add_layer(hmap2)
fig.add_layer(hmap)

embed_minimal_html('hmap.html', views=[fig])
