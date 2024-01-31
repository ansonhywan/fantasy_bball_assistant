from flask import Flask, request, jsonify
import sqlite3
import json

app = Flask(__name__)

DATABASE = "fantasy_bball_project.db"


def connect_db():
    return sqlite3.connect(DATABASE)


@app.route("/season_stats", methods=["GET"])
def get_stats():
    conn = connect_db()
    c = conn.cursor()

    # Example params
    # rank_threshold = players in roster * num teams in league = 13 * 12 = 144
    # category = assists

    params = request.args.to_dict()
    param_list = list(params.values())
    print(param_list[0])

    try:
        query = """SELECT * FROM fantasy_player_stats WHERE rank >= {} ORDER BY {} DESC limit 10"""
        c.execute(query.format(params['rank_threshold'], params['cat1']))
        data = c.fetchall()

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        # Close the database connection
        conn.close()

    return jsonify(data)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
