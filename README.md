# Tournament_Results
Developed the database schema for a Swiss tournament and wrote python code to interface with the database. In a Swiss tournament, players are not eliminated when they lose a match, but are paired in each round with opponents having (approximately) the same win-loss record.

## Setup
1. Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) to your machine.
2. cd into '/vagrant/tournament' and replace its contents with this repo's code.
3. From the 'fullstack-nanodegree-vm/vagrant' directory enter the command `vagrant up`. This command can take awhile to run. Ignore the error `default: stdin: is not a tty`.
4. Enter the command 'vagrant ssh'.
5. Once vagrant is up and running cd into '/vagrant/tournament'
6. tournament.sql in the tournament directory creates the database schema and views. To build and access the database first run `psql` then `\i tournament.sql`. To exit psql use `\q`.
6. The Vagrant VM provided in the fullstack repo already has PostgreSQL server installed so once step 5 is complete, you're good to run the tests. Enter the command `python tournament_test.py` to run the tests.

## Authors
* tournament.py - Geordy Williams
* tournament.sql - Geordy Williams
* tournament_test.py - Udacity
