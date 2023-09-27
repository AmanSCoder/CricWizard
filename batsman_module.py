import pandas as pd
import numpy as np

def batsman_data(link,data):
    batting_url=pd.read_html(link)
    df_batting=batting_url[0]
    df_batting.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
    req_batsmen=df_batting[(df_batting['Ave']>=data["avg"]) & (df_batting['SR']>=data["strike-rate"]) & (df_batting['BF']>=data["balls-faced":])]
    print(req_batsmen)
    return req_batsmen