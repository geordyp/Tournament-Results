#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        pg = psycopg2.connect("dbname={}".format(database_name))
        cursor = pg.cursor()
        return pg, cursor
    except:
        print("Failed to connect to the database.")

def deleteMatches():
    """Remove all the match records from the database."""
    pg, cursor = connect()
    cursor.execute("DELETE FROM match;")
    pg.commit()
    pg.close()


def deletePlayers():
    """Remove all the player records from the database."""
    pg, cursor = connect()
    cursor.execute("DELETE FROM player;")
    pg.commit()
    pg.close()


def countPlayers():
    """Returns the number of players currently registered."""
    pg, cursor = connect()
    cursor.execute("SELECT * FROM count_players;")
    result = cursor.fetchone()
    pg.close()
    return result[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    pg, cursor = connect()
    cursor.execute("INSERT INTO player (name) VALUES (%s);", (name,))
    pg.commit()
    pg.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    pg, cursor = connect()
    cursor.execute("SELECT * FROM standings;")
    results = cursor.fetchall()
    pg.close()
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    pg, cursor = connect()
    cursor.execute("INSERT INTO match (winner, loser)\
        VALUES (%s, %s);", (winner, loser))
    pg.commit()
    pg.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairings = []
    standings = playerStandings()

    i = 1
    # loop through the standings
    for player in standings:
        if i % 2 == 0:
            id2 = player[0]
            name2 = player[1]

            # every, other loop we'll have a tuple that can be appended
            pairings.append((id1, name1, id2, name2))
        else:
            id1 = player[0]
            name1 = player[1]

        i = i + 1

    return pairings
