import pandas as pd

def fetch_wicket_keeper_data(keeper_link, batsman_link, data):
    keeper_url = pd.read_html(keeper_link)
    df_keeper = keeper_url[0]
    batting_url = pd.read_html(batsman_link)
    df_batting = batting_url[0]
    df_batting.drop(['Mat', 'Inns', 'NO', '100', '0'], axis=1, inplace=True)
    df_wkeeper = df_batting.merge(df_keeper, on=['Player'])
    req_wk = df_wkeeper[(df_wkeeper['BF'] > int(data["dismissals"])) & (df_wkeeper['Ave'] > int(data["avg"])) & (
            df_wkeeper['SR'] > int(data["strike-rate"]))]
    return req_wk


def fetch_bowler_data(link, data):
    bowler_url = pd.read_html(link)
    df_bowling = bowler_url[0]
    df_bowling.drop(['Mat', 'Inns', 'Runs'], axis=1, inplace=True)
    req_bowler = df_bowling[
        (df_bowling['Wkts'] >= int(data["wickets-taken"])) & (df_bowling['Econ'] <= int(data["economy"])) & (
                df_bowling['Ave'] <= int(data["avg"]))]
    return req_bowler


def fetch_batsman_data(link, data):
    batting_url=pd.read_html(link)
    df_batting=batting_url[0]
    df_batting.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
    req_batsmen=df_batting[(df_batting['Ave']>=int(data['avg'])) & (df_batting['SR']>=int(data['strike-rate'])) & (df_batting['BF']>=int(data['balls-faced']))]
    print(req_batsmen)
    return req_batsmen


def fetch_all_rounder_data(batsman_link, bowler_link, data):
    batting_url = pd.read_html(batsman_link)
    df_batting = batting_url[0]
    df_batting.drop(['Mat', 'Inns', 'NO', '100', '0'], axis=1, inplace=True)
    bowler_url = pd.read_html(bowler_link)
    df_bowling = bowler_url[0]
    df_bowling.drop(['Mat', 'Inns', 'Runs'], axis=1, inplace=True)
    df_allround = df_batting.merge(df_bowling, on=['Player'])
    req_allround = df_allround[
        (df_allround['SR_x'] >= int(data["wickets-taken"])) & (df_allround['Ave_y'] <= int(data["economy"])) & (
                df_allround['Ave_x'] >= int(data["avg"]))]
    return req_allround
