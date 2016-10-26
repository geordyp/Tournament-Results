## Tournament_Results
Developed the database schema for a Swiss tournament and
wrote python code to interface with the database. In a
Swiss tournament, players are not eliminated when they lose
a match, but are paired in each round with opponents having
(approximately) the same win-loss record.


## Author
tournament.py - Geordy Williams
tournament.sql - Geordy Williams
tournament_test.py - Udacity

## Motivation

Created this as part of my Udacity Full Stack Web
Development Nanodegree.

## Setup
1. Fork the [fullstack-nanodegree-vm repo](https://github.com/udacity/fullstack-nanodegree-vm) and clone to your machine.
2. cd into /vagrant/tournament and replace its contents with
   this repo's code
3. From the tournament directory use the command 'vagrant up'
   followed by 'vagrant ssh'
4. Once vagrant is up and running cd to into /vagrant/tournament
5. tournament.sql in the tournament directory creates the
   database schema and views. To build and access the database
   run 'psql' followed by '\i tournament.sql'. To exit psql
   use '\q'.
6. The Vagrant VM provided in the fullstack repo already has
   PostgreSQL server installed so once step 5 is complete,
   you're good to run the tests. Use the command
   'python tournament_test.py' to run the tests.
