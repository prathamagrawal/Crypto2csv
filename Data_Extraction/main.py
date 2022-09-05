
from collections import deque
import pandas
from utils.api_call import get_data
from utils.detailed_data import detailed_data
from utils.get_dates import get_dates
from utils.process import process
from utils.historical_data import historical_data

output=detailed_data("bitcoin")
output.to_csv("output.csv")