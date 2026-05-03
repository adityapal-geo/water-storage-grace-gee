# WATER STORAGE MAPPING USING GRACE DATA


import ee
import geemap
import xarray as xr
!pip install xee
import xee



ee.Authenticate()
ee.Initialize(
    project = 'promising-idea-432505-i4',
     opt_url = 'https://earthengine-highvolume.googleapis.com'
)



map = geemap.Map(basemap = 'SATELLITE')
map


loc = map.draw_last_feature.geometry()



loc


international_asset = (
    ee.FeatureCollection("projects/promising-idea-432505-i4/assets/INTERNATIONAL")
    .filterBounds(loc)
    .geometry()
)

map.addLayer(international_asset, {},'INTERNATIONAL_ASSET')
map


collection = (
    ee.ImageCollection("NASA/GRACE/MASS_GRIDS_V04/MASCON_CRI")
    .filterDate('2010','2025') 
    .select('lwe_thickness')
    .map(lambda img: img.clip(international_asset).copyProperties(img, img.propertyNames()))
)
collection


ds = xr.open_dataset(
    collection,
    engine = 'ee',
    crs = 'EPSG:4326',
    geometry = international_asset,
    scale = 1
)


ds = ds.sortby('time') * 1


ds_month = ds.groupby('time.month').mean('time')
ds_month



ds_month.lwe_thickness.plot.contourf(
    x = 'lon',
    y = 'lat',
    col = 'month',
    robust = True,
    col_wrap = 4,
    cmap ='turbo_r',
    levels = 20
)



ds_annual = ds.resample(time = 'Y').mean('time')
ds_annual


ds_annual.lwe_thickness.plot.contourf(
    x = 'lon',
    y = 'lat',
    col = 'time',
    cmap = 'turbo_r',
    robust = True,
    col_wrap = 5,
    levels = 20
)


ds_mean = ds_annual.mean('time')
ds_anomaly = ds_annual - ds_mean



import matplotlib.pyplot as plt



ds_anomaly.lwe_thickness.plot.contourf(
    x = 'lon',
    y = 'lat',
    col = 'time',
    col_wrap = 5,
    robust = True,
    cmap = 'turbo_r',
    levels = 20
)

plt.savefig('water_storage_anomaly.png', dpi = 360, bbox_inches = 'tight')