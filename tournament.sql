-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- remove our database if it already exists so we can keep using this file
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

\c tournament

-- For debugging
-- DROP TABLE IF EXISTS match;
-- DROP TABLE IF EXISTS player;

-- player
-- id: primary key
-- matches: the number of matches they've played
CREATE TABLE player (id SERIAL,
                     name TEXT NOT NULL,
                     PRIMARY KEY(id));

-- match
-- id: primary KEY
-- winner: player id of the winner, references player
-- loser: player id of the loser, references player
CREATE TABLE match (id SERIAL,
                    winner INTEGER REFERENCES player(id) NOT NULL,
                    loser INTEGER REFERENCES player(id) NOT NULL,
                    PRIMARY KEY(id));

CREATE VIEW wins AS SELECT player.id, player.name, count(match.winner) AS wins FROM player LEFT JOIN match ON player.id = match.winner GROUP BY player.id ORDER BY wins DESC;
CREATE VIEW losses AS SELECT player.id, player.name, count(match.loser) AS losses FROM player LEFT JOIN match ON player.id = match.loser GROUP BY player.id ORDER BY losses DESC;
CREATE VIEW standings AS SELECT wins.id, wins.name, wins.wins, sum(wins.wins) + sum(losses.losses) AS matches FROM wins LEFT JOIN losses ON wins.id = losses.id GROUP BY wins.id, wins.name, wins.wins ORDER BY wins DESC;

CREATE VIEW count_players AS SELECT count(id) FROM player;
