#! /usr/bin/python

#This script requires you to have config.py and main.py in the main folder that contains the
#voters folder. This also requires the addition of the csv library
#This is written using python 2.7 on a centos 7 machine

# written by: Tyler Denton
# date: 17 May 2017


from config import config
import json
import os

def main():
    list = config()
    list.add_orange("./voters/orange.txt")
    list.add_seminole("./voters/seminole.txt")
    for file in os.listdir("./voters/alachua"):
      list.add_alachula("./voters/alachua/{}".format(file))
    list.import_alachua()
    #This is where I would normally write the json doc to couchbase
    list.write_csv()
    
if __name__=="__main__":
  main()


##########SQL STATEMENTS############################
# DECLARE @birthdate60 date			   #
# SET @birthdate60 = DATEADD(yy, 0, -60)	   #
# Select party, county, count(regnum)  		   #
#      FROM `table` 				   #
#      WHERE `table`.birthDate > @birthdate60     #
#      GROUP BY `table`.county, `table`.party      #
####################################################


