from bs4 import BeautifulSoup
import pandas as pd
import requests
import sqlite3


def scrapeSeasonStats():
    # Database Init
    conn = sqlite3.connect("fantasy_bball_project.db")
    c = conn.cursor()

    c.execute(
        """CREATE TABLE if not exists fantasy_player_stats(round INT, rank INT, value FLOAT, player TEXT, team TEXT, position TEXT, injury_status TEXT, games_played INT, 
        minutes_per_game FLOAT, points_per_game FLOAT, threes_made_per_game FLOAT, rebound_per_game FLOAT, assists_per_game FLOAT, steals_per_game FLOAT, blocks_per_game FLOAT,
        field_goal_percentage FLOAT, field_goal_attempts_per_game FLOAT, free_throw_percentage FLOAT, free_throw_attempts_per_game FLOAT, turnovers_per_game FLOAT,
        three_point_percentage FLOAT, three_point_attempts_per_game FLOAT, two_point_percentage FLOAT, two_point_attempts_per_game FLOAT,
        pV FLOAT, `3V` FLOAT, rV FLOAT, aV FLOAT, sV FLOAT, bV FLOAT, fgpV FLOAT, ftpV FLOAT, toV FLOAT)"""
    )

    # BeautifulSoup Init
    url = "https://basketballmonster.com/playerrankings.aspx"
    page = requests.get(url).text
    bs = BeautifulSoup(page, "html.parser")
    table = bs.find(
        "table",
        class_="table-bordered table-hover table-sm base-td-small datatable ml-0",
    )

    # Define dataframe
    df = pd.DataFrame(
        columns=[
            "Round",
            "Rank",
            "Value",
            "Player",
            "Team",
            "Position",
            "Status",
            "G",
            "M/G",
            "P/G",
            "3/G",
            "R/G",
            "A/G",
            "S/G",
            "B/G",
            "FG%",
            "FGA/G",
            "FT%",
            "FTA/G",
            "TO/G",
            "3%",
            "3A/G",
            "2%",
            "2A/G",
            "pV",
            "3V",
            "rV",
            "aV",
            "sV",
            "bV",
            "fg%V",
            "ft%V",
            "toV",
        ]
    )

    # Collect data
    for row in table.find_all("tr"):
        data = row.find_all("td")

        if data != []:
            data_list = []
            for i in range(len(data)):
                data_list.append(data[i].text.strip())

            df.loc[len(df)] = data_list
            c.execute(
                """INSERT INTO fantasy_player_stats VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
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
                    data_list[29],
                    data_list[30],
                    data_list[31],
                    data_list[32],
                ),
            ),
            conn.commit()

    print(df)


scrapeSeasonStats()
