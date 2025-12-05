from pandas import read_csv

from pathlib import Path
from sys import path


script_dir = Path(path[0])



passengers = read_csv(
    script_dir / 'ts_passengers.csv', 
    index_col=0,
    date_format='%Y-%m'
)

