from flask import Flask,render_template,jsonify
from flask import request
import pandas as pd
import lxml
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
@cross_origin()
def home_page():
    return render_template("index.html")

@app.route("/selection",methods=['POST'])
@cross_origin()
def selection_process():
    if(request.method=='POST'):
        global playerType
        playerType=request.form['myPlayer']
        if(playerType=='batsman'):
            return render_template('batsman.html')
        if(playerType=='bowler'):
            return render_template('bowler.html')
        if(playerType=='wicket'):
            return render_template('wicket.html')
        if(playerType=='all'):
            return render_template('all.html')

# def batsman_data(key1,key2,key3):
#     batting_url=pd.read_html("https://www.espncricinfo.com/records/tournament/batting-highest-career-batting-average/icc-men-s-t20-world-cup-2022-23-14450")
#     df_batting=batting_url[0]
#     df_batting.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
#     req_batsmen=df_batting[(df_batting['Ave']>=key1) & (df_batting['SR']>=key2) & (df_batting['BF']>=key3)]
#     print(req_batsmen)
#     return render_template('results.html',tables=[req_batsmen.to_html(classes='data')],titles=req_batsmen.columns.values)
    
    
# def bowler_data(key1,key2,key3):
#     bowler_url=pd.read_html("https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-men-s-t20-world-cup-2022-23-14450")
#     df_bowling=bowler_url[0]
#     df_bowling.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
#     req_bowler=df_bowling[(df_bowling['Wkts']>=key1) & (df_bowling['Econ']>=key2) & (df_bowling['Ave']>=key3)]
#     return render_template('results.html',tables=[req_bowler.to_html(classes='data')],titles=req_bowler.columns.values)
    

# def wicket_data(key1,key2,key3):
#     keeper_url=pd.read_html("https://www.espncricinfo.com/records/tournament/keeping-most-dismissals-career/icc-men-s-t20-world-cup-2022-23-14450")
#     df_keeper=keeper_url[0]
#     batting_url=pd.read_html("https://www.espncricinfo.com/records/tournament/batting-highest-career-batting-average/icc-men-s-t20-world-cup-2022-23-14450")
#     df_batting=batting_url[0]
#     df_batting.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
#     df_wkeeper= df_batting.merge(df_keeper, on=['Player'])
#     req_wk=df_wkeeper[(df_wkeeper['Dis']>key1) & (df_wkeeper['Ave']>key2) & (df_wkeeper['SR']>key3) ]
#     return render_template('results.html',tables=[req_wk.to_html(classes='data')],titles=req_wk.columns.values)
    


# def all_data(key1,key2,key3):
#     batting_url=pd.read_html("https://www.espncricinfo.com/records/tournament/batting-highest-career-batting-average/icc-men-s-t20-world-cup-2022-23-14450")
#     df_batting=batting_url[0]
#     df_batting.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
#     bowler_url=pd.read_html("https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-men-s-t20-world-cup-2022-23-14450")
#     df_bowling=bowler_url[0]
#     df_bowling.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
#     df_allround= df_batting.merge(df_bowling, on=['Player'])
#     req_allround=df_allround[(df_allround['SR_x']>=key1) & (df_allround['Avg_y']>=key2) & (df_allround['Ave_x']>=key3)]
#     return render_template('results.html',tables=[req_allround.to_html(classes='data')],titles=req_allround.columns.values)
    
    



@app.route('/result',methods=['POST'])
@cross_origin()
def result_process():
    if(request.method=='POST'):
        key1=int(request.form['key1'])
        key2=int(request.form['key2'])
        key3=int(request.form['key3'])
        print(playerType)
        if(playerType=='batsman'):
            batting_url=pd.read_html("https://www.espncricinfo.com/records/tournament/batting-highest-career-batting-average/icc-men-s-t20-world-cup-2022-23-14450")
            df_batting=batting_url[0]
            df_batting.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
            req_batsmen=df_batting[(df_batting['Ave']>=key1) & (df_batting['SR']>=key2) & (df_batting['BF']>=key3)]
            print(req_batsmen)
            return render_template('results.html',tables=[req_batsmen.to_html(classes='data')],titles=req_batsmen.columns.values)
            
        elif(playerType=='bowler'):
            bowler_url=pd.read_html("https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-men-s-t20-world-cup-2022-23-14450")
            df_bowling=bowler_url[0]
            df_bowling.drop(['Mat','Inns','Runs'],axis=1,inplace=True)
            req_bowler=df_bowling[(df_bowling['Wkts']>=key1) & (df_bowling['Econ']<=key2) & (df_bowling['Ave']<=key3)]
            return render_template('results.html',tables=[req_bowler.to_html(classes='data')],titles=req_bowler.columns.values)

        elif(playerType=='wicket'):
            keeper_url=pd.read_html("https://www.espncricinfo.com/records/tournament/keeping-most-dismissals-career/icc-men-s-t20-world-cup-2022-23-14450")
            df_keeper=keeper_url[0]
            batting_url=pd.read_html("https://www.espncricinfo.com/records/tournament/batting-highest-career-batting-average/icc-men-s-t20-world-cup-2022-23-14450")
            df_batting=batting_url[0]
            df_batting.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
            df_wkeeper= df_batting.merge(df_keeper, on=['Player'])
            req_wk=df_wkeeper[(df_wkeeper['BF']>key1) & (df_wkeeper['Ave']>key2) & (df_wkeeper['SR']>key3) ]
            return render_template('results.html',tables=[req_wk.to_html(classes='data')],titles=req_wk.columns.values)

        elif(playerType=="all"):
            batting_url=pd.read_html("https://www.espncricinfo.com/records/tournament/batting-highest-career-batting-average/icc-men-s-t20-world-cup-2022-23-14450")
            df_batting=batting_url[0]
            df_batting.drop(['Mat','Inns','NO','100','0'],axis=1,inplace=True)
            bowler_url=pd.read_html("https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-men-s-t20-world-cup-2022-23-14450")
            df_bowling=bowler_url[0]
            df_bowling.drop(['Mat','Inns','Runs'],axis=1,inplace=True)
            df_allround= df_batting.merge(df_bowling, on=['Player'])
            req_allround=df_allround[(df_allround['SR_x']>=key1) & (df_allround['Ave_y']<=key2) & (df_allround['Ave_x']>=key3)]
            return render_template('results.html',tables=[req_allround.to_html(classes='data')],titles=req_allround.columns.values)
            
if __name__=="__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
