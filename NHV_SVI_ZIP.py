#!/usr/bin/python3
import pandas as pd
#Data downloaded from <https://www.atsdr.cdc.gov/placeandhealth/svi/data_documentation_download.html>: 2018 -> Connecticut -> Census Tracts -> CSV File
#ct = pd.read_csv("Connecticut.csv",dtype='string')
uri = "https://svi.cdc.gov/Documents/Data/2018_SVI_Data/CSV/States/Connecticut.csv"
ct = pd.read_csv(uri,dtype='string')
#using HUD Zip - FIPS+Tract mapping at <https://www.huduser.gov/portal/datasets/usps_crosswalk.html>, do crosswalk between SVI data and ZIP: ZIP-TRACT -> 4th Quarter 2018 -> Excel Download
#zip_tract = pd.read_excel("ZIP_TRACT_122018.xlsx",usecols="A:B",dtype={'zip':str,'tract':str})
uri = "https://www.huduser.gov/portal/datasets/usps/ZIP_TRACT_122018.xlsx"
zip_tract = pd.read_excel(uri,usecols="A:B",dtype={'zip':str,'tract':str})
zip_tract_map = {r['tract']:r['zip'] for i,r in zip_tract.iterrows()}
#assign zip code based on FIPS+Tract code, if no map, NA
ct_zip = []
for fips in ct['FIPS']:
    try:
        m = zip_tract_map[fips] 
    except KeyError:
        m = 'NA'
    ct_zip.append(m)
#add to dataframe
ct['ZIP'] = ct_zip
#write out to file
ct.to_csv("Connecticut+ZIP.csv",index=False)
