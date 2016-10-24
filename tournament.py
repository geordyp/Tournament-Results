#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    pg = connect()
    cursor = pg.cursor()
    cursor.execute("DELETE FROM match;")
    cursor.execute("UPDATE player SET wins = 0, matches = 0;")
    pg.commit()
    pg.close()


def deletePlayers():
    """Remove all the player records from the database."""
    pg = connect()
    cursor = pg.cursor()
    cursor.execute("DELETE FROM player;")
    pg.commit()
    pg.close()


def countPlayers():
    """Returns the number of players currently registered."""
    pg = connect()
    cursor = pg.cursor()
    cursor.execute("SELECT count(id) FROM player;")
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
    pg = connect()
    cursor = pg.cursor()
    # Leaving out id so that the SQL database schema will handle it
    cursor.execute("INSERT INTO player (name, wins, matches)\
        VALUES (%s, 0, 0);", (name,))
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
    pg = connect()
    cursor = pg.cursor()
    cursor.execute("SELECT * FROM player ORDER BY wins DESC;")
    results = cursor.fetchall()
    pg.close()
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    pg = connect()
    cursor = pg.cursor()
    # Leaving out id so that the SQL database schema will handle it
    cursor.execute("INSERT INTO match (winner, loser)\
        VALUES (%s, %s);", (winner, loser))
    # Update player wins and matches columns for winner based on match insert
    cursor.execute("UPDATE player SET wins = w.num, matches = m.num\
        FROM (SELECT count(id) AS num FROM match WHERE winner = %s) As w,\
        (SELECT count(id) AS num FROM match WHERE winner = %s OR loser = %s)\
        As m WHERE player.id = %s;", (winner, winner, winner, winner))
    # Update player wins and matches columns for loser based on match insert
    cursor.execute("UPDATE player SET wins = w.num, matches = m.num\
        FROM (SELECT count(id) AS num FROM match WHERE winner = %s) As w,\
        (SELECT count(id) AS num FROM match WHERE winner = %s OR loser = %s)\
        As m WHERE player.id = %s;", (loser, loser, loser, loser))
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
