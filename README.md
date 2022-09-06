# Crypto2csv

<p align="center">
  <img src="https://user-images.githubusercontent.com/58286330/188595309-6f7c6adb-ad2b-4196-b000-6200c93ee3ae.png" width="500" title="Crypto2csv">
</p>

Crypto2csv is a python package accessible via command line for accessing crytocurrencies data in a readable csv format. 

## Setting up Crytpo2Csv

open the terminal in the folder in which you wish to download the package. 

### Activate the python environment:

Windows: 
```
path\to\venv\Scripts\activate.bat
```

Unix or MacOS:
```
source /path/to/venv/bin/activate
```

MacOS (with M1 Chipset):
```
conda activate environment-name
```

If you haven't setup python environment, you could refer to the official docs. <br />
Link: [Official Docs](https://docs.python.org/3/tutorial/venv.html) <br />
Simplified Resource: [Simplified Resource](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) <br />

### Prerequisites
To use crypto2csv, you need requests library for API calling, pandas for constructing the dataframe, and json for data parsing. 
You don't need to install anything before hand. 

### Installation
Open the terminal, activate the environment and enter the following command:
```
pip install crypto2csv
```
You have successfully installed the latest version of crypto2csv! 


## Usage
There are 2 commands as of the moment. <br />
### Get Detailed Information <br /> 
```
crypto2csv "coin-name"
```
The command returns a csv file in the folder location with an extensive details for the cryptocurrency coin. 
The obtained csv files contains more than 75+ fields of information. The information is extracted to the latest date by coingecko. 

### Get Interval Information <br />
```
crypto2csv "coin-name" "start-date" "end-date" 
``` 
The command returns a csv file with an details for the cryptocurrency coin over a specified date range.

The obtained csv files contains more than 14+ fields of information. 
Note: The specified date should be in the format `DD-MM-YYYY` 

Distributed under the *MIT License*. See [`LICENSE`](https://github.com/prathamagrawal/crypto2save/LINCENSE) for more information.










