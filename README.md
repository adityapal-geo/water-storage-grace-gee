

# Water Storage Mapping using GRACE (GEE + Xarray)

This project demonstrates how to analyze terrestrial water storage changes using NASA GRACE data in Google Earth Engine (GEE) with Xarray and XEE.

---

## Features

* GRACE Mascon dataset processing
* Monthly water storage analysis
* Annual water storage trends
* Water storage anomaly calculation
* Visualization using Matplotlib

---

## Dataset

* **Source**: NASA GRACE Mascon (Mass Concentration Blocks)
* **Collection**: `NASA/GRACE/MASS_GRIDS_V04/MASCON_CRI`
* **Band Used**: `lwe_thickness` (Liquid Water Equivalent Thickness)

---


## Google Earth Engine Setup

```python
import ee

ee.Authenticate()
ee.Initialize(
    project='your-project-id',
    opt_url='https://earthengine-highvolume.googleapis.com'
)
```


---

## Outputs

* Monthly water storage maps
* Annual water storage maps
* Water storage anomaly maps
* High-resolution PNG export


---

## Applications

* Drought monitoring
* Hydrological analysis
* Climate change studies
* Groundwater storage assessment

---

## Notes

* Remove `!pip install xee` from the script before running locally
* Ensure Earth Engine authentication is completed
* Draw your ROI interactively using geemap

---

## Author

**Aditya Pal**

---

