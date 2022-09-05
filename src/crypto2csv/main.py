import os
import pandas
import sys

from utils.detailed_data import detailed_data
from utils.historical_data import historical_data

if(len(sys.argv)==2):
    coin=str(sys.argv[1])
    output=detailed_data(coin)
    output.to_csv("data.csv")

if(len(sys.argv)==4):
    coin=str(sys.argv[1])
    start=str(sys.argv[2])
    end=str(sys.argv[3])
    output=historical_data(coin,start,end)
    output.to_csv("data.csv")