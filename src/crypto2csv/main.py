import os
import pandas
import sys

from utils.detailed_data import detailed_data
from utils.historical_data import historical_data

if(len(sys.argv)==2):
    coin=str(sys.argv[1])
    output=detailed_data(coin)
    print(output)