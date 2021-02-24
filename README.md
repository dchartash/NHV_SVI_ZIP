# New Haven Social Vulnerability Index Script
Script to link Connecticut Zip Codes to Social Vulnerability Index (SVI) using _4th quarter 2018_ data.
Social Vulnerability Index documentation can be found here: <https://www.atsdr.cdc.gov/placeandhealth/svi/documentation/SVI_documentation_2018.html>

- SVI data downloaded from the Centers for Disease Control at <https://www.atsdr.cdc.gov/placeandhealth/svi/data_documentation_download.html> by selecting 2018 -> Connecticut -> Census Tracts -> CSV File.
- Zip code data downloading from United States Department of Housing and Urban Development at <https://www.huduser.gov/portal/datasets/usps_crosswalk.html> to crosswalk zip codes to census tract data by selecting ZIP-TRACT -> 4th Quarter 2018 -> Excel Download.

Output writes to `Connecticut+ZIP.csv` in the directory where the script has been run, data is hardlinked to URLs from CDC and HUD and ingested directly.
New Haven County can be selected by filtering on the `COUNTY` variable.

* * *

## Python Environment Tested 

- Python 3.7.3 (default, Jul 25 2020, 13:03:44) [GCC 8.3.0] on linux

## Depends: 

- pandas version 1.0.3
