from pandas import read_csv

from pathlib import Path
from sys import path


script_dir = Path(path[0])

births = read_csv(
    script_dir / 'ts_births.csv', 
    index_col='date',
    date_format='%Y-%m-%d',
)


