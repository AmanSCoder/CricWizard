import pandas as pd
import numpy as np

def batsman_data(link,data):
    batting_url=pd.read_html(link)
    df_batting=batting_url[0]
    df_batting.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
    req_batsmen=df_batting[(df_batting['Ave']>=int(data['avg'][0])) & (df_batting['SR']>=int(data['strike-rate'][0])) & (df_batting['BF']>=int(data['balls-faced'][0]))]
    print(req_batsmen)
    return req_batsmen