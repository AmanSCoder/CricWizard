from enum import Enum

from batsman_module import batsman_data
from bowler_module import bowler_data
from allrounder_module import allrounder_data
from wicketkeeper_module import wicketkeeper_data

from flask import Blueprint, render_template, request as req, flash, redirect, url_for
import json
links={}
link={}

class PlayerTypes(Enum):
    BATSMAN = "batsman"
    BOWLER = "bowler"
    WICKETKEEPER = "wicketkeeper"
    ALLROUNDER = "allrounder"


bp = Blueprint("main", __name__)


@bp.route("/", methods=("GET", "POST"))
def index():
    from app.data import devs
    if req.method == "GET":
        return render_template("main/index.html", devs=devs)

    # POST method
    age, player = req.form["age"], req.form["player-type"]
    global link
    print("printing")
    print(age)
    print(player)
    f=open(r"/home/aman/new_folder/cricwizard/app/links.json")
    links=json.load(f)
    link=links[str(age)]
    print(link)

    error = None
    if not age or not player:
        error = "Both Age and Player type is needed"
    # if error occurs, then flash the error on screen and redirect
    if error:
        flash(error)
        return render_template("main/index.html", devs=devs)

    return redirect(url_for("main.player_info", age=age, player_type=player))


@bp.route("/player-info")
def player_info():
    from app.data import devs
    age, player_type = req.args.getlist("age"), req.args.getlist("player_type")
    # print("printing")
    # print(age)
    # print(player_type)
    # f=open('D:\Project upload\CricWizard\\app\links.json')
    # links=json.load(f)
    # link=links[str(age[0])]
    # print(link)


    # data check
    player_type = player_type if player_type else PlayerTypes.ALLROUNDER.value
    if isinstance(player_type, list):
        player_type = player_type[0]

    return render_template("main/player-info.html", devs=devs, player_type=player_type)


@bp.route("/result")
def result():
    from app.data import devs

    # get data from url
    player_type = req.args.getlist("player_type")
    age=req.args.getlist("age")
    # data check
    player_type = player_type if player_type else PlayerTypes.ALLROUNDER.value
    if isinstance(player_type, list):
        player_type = player_type[0]
    
    
    match player_type:
        case PlayerTypes.BATSMAN.value:
            data = {
                "avg": req.args.getlist("avg"),
                "strike-rate": req.args.getlist("strike-rate"),
                "balls-faced": req.args.getlist("balls-faced")
            }
            exact_link=link[player_type.capitalize()]
            tabledata=batsman_data(exact_link,data)
            print(tabledata)

        case PlayerTypes.ALLROUNDER.value:
            data = {
                "wickets-taken": req.args.getlist("strike-rate"),
                "economy": req.args.getlist("ball-avg"),
                "avg": req.args.getlist("bat-avg")
            }
            tabledata=allrounder_data(link['Batsman'],link['Bowler'],data)
            print(tabledata)
        case PlayerTypes.WICKETKEEPER.value:
            data = {
                "dismissals": req.args.getlist("dismissals"),
                "avg": req.args.getlist("avg"),
                "strike-rate": req.args.getlist("strike-rate")
            }
            tabledata=wicketkeeper_data(link['Wicketkeeper'],link['Batsman'],data)
            print(tabledata)
        case _:
            # bowler data
            data = {
                "wickets-taken": req.args.getlist("wickets-taken"),
                "economy": req.args.getlist("economy"),
                "avg": req.args.getlist("avg")
            }
            exact_link=link[player_type.capitalize()]
            tabledata=bowler_data(exact_link,data)
            print(tabledata)
    print(data)

    return render_template("main/results.html", devs=devs)
