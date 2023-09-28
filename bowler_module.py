import pandas as pd
def bowler_data(link,data):
    bowler_url=pd.read_html(link)
    df_bowling=bowler_url[0]
    df_bowling.drop(['Mat','Inns','Runs'],axis=1,inplace=True)
    req_bowler=df_bowling[(df_bowling['Wkts']>=int(data["wickets-taken"][0])) & (df_bowling['Econ']<=int(data["economy"][0])) & (df_bowling['Ave']<=int(data["avg"][0]))]
    print(req_bowler)
    return req_bowler