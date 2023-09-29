import pandas as pd
def wicketkeeperdata(keeper_link,batsman_link,data):
    keeper_url=pd.read_html(keeper_link)
    df_keeper=keeper_url[0]
    batting_url=pd.read_html(batsman_link)
    df_batting=batting_url[0]
    df_batting.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
    df_wkeeper= df_batting.merge(df_keeper, on=['Player'])
    req_wk=df_wkeeper[(df_wkeeper['BF']>int(data["dismissals"][0])) & (df_wkeeper['Ave']>int(data["avg"][0])) & (df_wkeeper['SR']>int(data["strike-rate"][0])) ]
    return req_wk