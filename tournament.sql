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
-- name: the name of the player
-- wins: the number of wins they have
-- matches: the number of matches they've played
CREATE TABLE player (id SERIAL,
                     name TEXT NOT NULL,
                     wins INTEGER NOT NULL,
                     matches INTEGER NOT NULL,
                     PRIMARY KEY(id));

-- match
-- id: primary KEY
-- winner: player id of the winner, references player
-- loser: player id of the loser, references player
CREATE TABLE match (id SERIAL,
                    winner INTEGER REFERENCES player(id) NOT NULL,
                    loser INTEGER REFERENCES player(id) NOT NULL,
                    PRIMARY KEY(id));
