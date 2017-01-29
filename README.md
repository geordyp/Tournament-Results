# Tournament_Results
Developed the database schema for a Swiss tournament and wrote python code to interface with the database. In a Swiss tournament, players are not eliminated when they lose a match, but are paired in each round with opponents having (approximately) the same win-loss record.

## Technologies Used
* PostgreSQL

## Setup
1. After cloning this repo to your machine, cd into 'Tournament_Results'.
2. Enter the command `vagrant up`. This command can take awhile to run. Ignore the error `default: stdin: is not a tty`.
3. Enter the command 'vagrant ssh'.
4. Once vagrant is up and running cd into '/vagrant'.
5. Enter the command `python tournament_test.py` to run the tests.

#### Note
* tournament.sql in the tournament directory creates the database schema and views. To build and access the database first run `psql` then `\i tournament.sql`. To exit psql use `\q`.


## Authors
* tournament.py - Geordy Williams
* tournament.sql - Geordy Williams
* tournament_test.py - Udacity
* pg_config.sh - Udacity
* Vagrantfile - Udacity
