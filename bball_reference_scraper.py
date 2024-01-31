from bs4 import BeautifulSoup
import pandas as pd
import requests
import sqlite3


def scrapeSeasonStats():
    # Database Init
    conn = sqlite3.connect("fantasy_bball_project.db")
    c = conn.cursor()

    c.execute(
        """CREATE TABLE if not exists player_stats(player TEXT, position TEXT, age INT, team TEXT, games_played INT, games_started INT,
     minutes_played INT, field_goals_made INT, field_goal_attempts INT, field_goal_percentage FLOAT, three_points_made INT, three_point_attempts INT,
     three_point_percentage FLOAT, two_points_made INT, two_point_attempts INT, two_point_percentage FLOAT, effective_field_goal_percentage FLOAT,
     free_throws_made INT, free_throw_attempts INT, free_throw_percentage FLOAT, offensive_rebounds FLOAT, defensive_rebounds FLOAT, 
     total_rebounds FLOAT, assists FLOAT, steals FLOAT, blocks FLOAT, turnovers FLOAT, personal_fouls FLOAT, points FLOAT)"""
    )

    # BeautifulSoup Init
    url = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"
    page = requests.get(url).text
    bs = BeautifulSoup(page, "html.parser")
    table = bs.find("table", class_="stats_table")
    print(table)

    # Define dataframe
    df = pd.DataFrame(
        columns=[
            "Player",
            "Position",
            "Age",
            "Team",
            "G",
            "GS",
            "MP",
            "FG",
            "FGA",
            "FG%",
            "3P",
            "3PA",
            "3P%",
            "2P",
            "2PA",
            "2P%",
            "eFG%",
            "FT",
            "FTA",
            "FT%",
            "ORB",
            "DRB",
            "TRB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
        ]
    )

    # Collect data
    for row in table.tbody.find_all("tr", attrs={"class": "full_table"}):
        data = row.find_all("td")

        print(data[0].text.strip())
        # print(data[28].text.strip())

        if data != []:
            data_list = []
            for i in range(len(data)):
                data_list.append(data[i].text.strip())

            df.loc[len(df)] = data_list
            c.execute(
                """INSERT INTO player_stats VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    data_list[0],
                    data_list[1],
                    data_list[2],
                    data_list[3],
                    data_list[4],
                    data_list[5],
                    data_list[6],
                    data_list[7],
                    data_list[8],
                    data_list[9],
                    data_list[10],
                    data_list[11],
                    data_list[12],
                    data_list[13],
                    data_list[14],
                    data_list[15],
                    data_list[16],
                    data_list[17],
                    data_list[18],
                    data_list[19],
                    data_list[20],
                    data_list[21],
                    data_list[22],
                    data_list[23],
                    data_list[24],
                    data_list[25],
                    data_list[26],
                    data_list[27],
                    data_list[28],
                ),
            ),
            conn.commit()

    print(df)


scrapeSeasonStats()
