import pandas as pd
def allrounder_data(batsman_link,bowler_link,data):
    batting_url=pd.read_html(batsman_link)
    df_batting=batting_url[0]
    df_batting.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
    bowler_url=pd.read_html(bowler_link)
    df_bowling=bowler_url[0]
    df_bowling.drop(['Mat','Inns','Runs'],axis=1,inplace=True)
    df_allround= df_batting.merge(df_bowling, on=['Player'])
    req_allround=df_allround[(df_allround['SR_x']>=int(data["wickets-taken"][0])) & (df_allround['Ave_y']<=int(data["economy"][0])) & (df_allround['Ave_x']>=int(data["avg"][0]))]
    return req_allround