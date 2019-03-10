### LOG ANALYSIS

SATULURI VIJAYALAKSHMI

## Overview

In this project I was tasked to create a reporting tool which can print reports based on real world web-application data, with fields representing informaton that a webserver would record, such as status codes and URL paths. This reporting tool is use Python program using psycopg2 module to connect the database.

## TASK GIVEN TO US IN THIS PROJECT IS AS FOLLOWS :

1.What are the msot popular articles of the all time?
2.Who are the most popular articles authors of all time?
3.On which days did more than 1% of requests lead to errors?

## REQUIREMENTS

* Python3
* Vagrant
* Virtual Box

## Setup

* Install Vagrant and VirtualBox
* Download fullstack-nanodegree-vm repository.
* Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from there

## Steps to launch the virtual machine.

# open cmd prompt in the folder udacityloganalysis.py

* vagrant up

* vagrant ssh

* cd ..
 
* cd ..
 
* cd vagrant 						----->		to move to vagrant

* ls 								-----> 		shows the list of files in vagrant

* sudo apt-get update 				----->		update if required

* sudo apt-get install postgresql	-----> Install the command if it is not present

* sudo su - postgres

* psql 								-----> 		to move to postgres

* \q									-----> 		to come out from database

* logout								----->		to come out from server

* psql _d news -f newsdata.sql

* psql _d news -f views.sql

* python log.py 						----->		shows the output					

# files present in this project are:

* log.py
* loaganalysisoutput.jpg
 ![loganalysisoutput.jpg](https://github.com/satulurivijayalakshmi/loganalysis/blob/master/loganalysisoutput.jpg)
* views.sql
* readme.md

## views


#### create article view	
		SELECT replace as slug, count(*) as views
		FROM log
		WHERE path<>'/' AND status ='200 OK' GROUP BY path;


### create author view		
		SELECT authors.name as name, articles.slug as slug
		FROM authors INNER JOIN articles
		ON articles.author=authors.id
		ORDER BY authors.id;


### 	
		SELECT Date,Total,Error from
		(select time,date as Date, count(status) as Total,
		sum(case when status = '404 NOT FOUND' then 1 else 0 end) as Error from log
		group by time,date) as result
		where (float*100)/Total > 1.0 order by Percent desc;
