from flask import Flask, redirect, request, render_template, flash
import requests
import http.client


app = Flask(__name__)
app.secret_key = 'thisisasecret'



#### Request Sample

import http.client

conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.american-football.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/players?id=1", headers=headers)

res = conn.getresponse()
data = res.read()





@app.route('/')
def home():
    """Home Page"""
    return render_template('index.html')


@app.route('/request_players', methods=["POST", "GET"])
def find_players():
    if request.method == "GET":
        player_id = request.args.get('player_id', '')  # Use `args.get` for GET parameters
        player_name = request.args.get('player_name', '')
        season = request.args.get('season', '')
        player_search = request.args.get('search', '')

        params = {"id": player_id,
                  "name": player_name,
                  "season": season,
                  "search": player_search}
                  

        filtered_params = {k: v for k, v in params.items() if v}
        try:
            url = "https://v1.american-football.api-sports.io/players"
            headers = {
                'x-rapidapi-host': "v1.american-football.api-sports.io",
                'x-rapidapi-key': "5c29d88f6d83d617fff6d52b9a13fd6e"
            }
            
            response = requests.get(url, headers=headers, params=filtered_params)
            response.raise_for_status()  # Raise an error on bad status
            data = response.json()

            return render_template('result.html', data=data, player_id=player_id, player_name=player_name,
                                    season=season, player_search=player_search)

        except requests.exceptions.RequestException as e:
            flash(f'Error: {e}')
            return redirect('/')
    


@app.route('/request_teams', methods=["POST", "GET"])
def find_teams():
    if request.method == "GET":
        team_id = request.args.get('team_id', '') 
        team_name = request.args.get('team_name', '')

        params = {"id": team_id,
                  "name": team_name,
                  }

        filtered_params = {k: v for k, v in params.items() if v}
        try:
            url = "https://v1.american-football.api-sports.io/teams"
            headers = {
                'x-rapidapi-host': "v1.american-football.api-sports.io",
                'x-rapidapi-key': "5c29d88f6d83d617fff6d52b9a13fd6e"
            }
            
            response = requests.get(url, headers=headers, params=filtered_params)
            response.raise_for_status()  # Raise an error on bad status
            data_team = response.json()

            return render_template('team_result.html', data_team=data_team, team_name=team_name,
                                   team_id=team_id)

        except requests.exceptions.RequestException as e:
            flash(f'Error: {e}')
            return redirect('/')



@app.route('/request_games', methods=["POST", "GET"])
def find_games():
    if request.method == "GET":
        game_id = request.args.get('game_id','')
        date = request.args.get('date_of_game', '')
        team_id = request.args.get('team_id', '')


        params = {"id": game_id,
                  "date": date,
                  "team": team_id}

        filtered_params = {k: v for k, v in params.items() if v}
        try:
            url = "https://v1.american-football.api-sports.io/games"
            headers = {
                'x-rapidapi-host': "v1.american-football.api-sports.io",
                'x-rapidapi-key': "5c29d88f6d83d617fff6d52b9a13fd6e"
            }
            
            response = requests.get(url, headers=headers, params=filtered_params)
            response.raise_for_status()  # Raise an error on bad status
            data_game = response.json()

            return render_template('game_result.html', data_game=data_game, game_id=game_id,
                                   team_id=team_id, date=date, )

        except requests.exceptions.RequestException as e:
            flash(f'Error: {e}')
            return redirect('/')



@app.route('/request_games_team_stats', methods=["POST", "GET"])
def find_team_stats():
    if request.method == "GET":
        game_id = request.args.get('game_id','')
        team_id = request.args.get('team_id', '')    


        params = {"id": game_id,
                  "team": team_id
                  }

        filtered_params = {k: v for k, v in params.items() if v}

        try:
            url = "https://v1.american-football.api-sports.io/games/statistics/teams"
            headers = {
                'x-rapidapi-host': "v1.american-football.api-sports.io",
                'x-rapidapi-key': "5c29d88f6d83d617fff6d52b9a13fd6e"
            }
            
            response = requests.get(url, headers=headers, params=filtered_params)
            response.raise_for_status()  # Raise an error on bad status
            data_stats = response.json()

            return render_template('team_stats.html', data_stats=data_stats, game_id=game_id,
                                   team_id=team_id  )

        except requests.exceptions.RequestException as e:
            flash(f'Error: {e}')
            return redirect('/')


@app.route('/request_games_player_stats', methods=["POST", "GET"])
def find_player_stats():
    if request.method == "GET":
        game_id = request.args.get('game_id','')
        player_id = request.args.get('player_id', '')
        team_id = request.args.get('team_id', '')  
        group = request.args.get('group', '')  
        ### Group Categories: (VALID GROUPS) "defensive" "fumbles" "interceptions" "kick_returns"
        ####           "kicking" "passing" "punt_returns" "punting" "receiving" "rushing"


        params = {"id": game_id,
                  "player": player_id,
                  "team": team_id,
                  "group": group
                  }

        filtered_params = {k: v for k, v in params.items() if v}
        try:
            url = "https://v1.american-football.api-sports.io/games/statistics/players"
            headers = {
                'x-rapidapi-host': "v1.american-football.api-sports.io",
                'x-rapidapi-key': "5c29d88f6d83d617fff6d52b9a13fd6e"
            }
            
            response = requests.get(url, headers=headers, params=filtered_params)
            response.raise_for_status()  # Raise an error on bad status
            data_player = response.json()

            return render_template('player_stats.html', data_player=data_player, game_id=game_id,
                                   team_id=team_id, player_id=player_id, group=group )

        except requests.exceptions.RequestException as e:
            flash(f'Error: {e}')
            return redirect('/')


def parse_json(response):
    charlist =[]
    for item in response['results']:
        char = {
            'name': item['name'],
            'height': len(item['height']),
        }

        charlist.append(char)
        return charlist
    
    
if __name__ == "__main__":
    app.run(debug=True)