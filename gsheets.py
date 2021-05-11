import pygsheets
import pandas as pd
from datetime import datetime as dt

spreadsheet_id = '1o_o4vil2VPIjO_XEECPz9yz3IAImEd8R1l9GQZkEeUY'

def init():
    #authorization
    gc = pygsheets.authorize(service_file='./credentials.json')

    spreadsheet = gc.open_by_key(spreadsheet_id)

    worksheet = spreadsheet[1] #get the second sheet, which is where all our stuff is, this is of type Worksheet

    worksheet.clear(start='A2')

    return worksheet

def writetosheets(df, worksheet):
    df.insert(0,'Timestamp', dt.now().strftime("%m/%d/%Y, %H:%M:%S"))
    #convert dataframe to a list without the headers!
    df_matrix = df.values.tolist()

    if(len(df_matrix) == 0):
        print("warning, no job postings found")
        return

    # append to the worksheet your dataframe (overwrite=false means it will add new rows every time you insert)
    worksheet.append_table(df_matrix, start='A1', dimension="ROWS", end=None, overwrite=False)