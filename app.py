from flask import Flask, jsonify
from flask_cors import CORS
from models.user import User
from models.api_client import Steam
from models.user_transformer import User_transformer
from models.game_transformer import Game_transformer
from models.csgo_stats_transformer import Csgo_stats_transformer

app = Flask(__name__)
CORS(app)


@app.route('/howmuchtimehaveiwasted/')
def no_steamid():
    return jsonify('Please provide a steamid'), 400


@app.route('/howmuchtimehaveiwasted/<steamid>',  methods=["GET"])
def get_user(steamid):
    try:
        user_data = Steam().get_user_data(steamid)
        games_data = Steam().get_user_games(steamid)
        stats_data = Steam().get_user_csgo_stats(steamid)
    except:
        return jsonify('There was a problem finding that user'), 400

    games = Game_transformer().transform_games_list(games_data)
    csgo_stats = Csgo_stats_transformer().transform_csgo_stats(stats_data)
    user = User_transformer().transform_user(user_data, games, csgo_stats)

    return jsonify(user.to_json())


if __name__ == '__main__':
    app.run()
