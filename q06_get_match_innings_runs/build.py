# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

# Solution
def get_match_innings_runs():
    df=pd.DataFrame(ipl_df[['match_code','inning','runs']])
    new_df=df.groupby(['match_code','inning']).sum()
    return new_df
