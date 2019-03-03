'''
GOAL:
Given a folder filled with .csv files, this program will create
a database for the entire folder and each individual .csv file
will be its own table in the database.
'''

import csv
import psycopg2
import os
import time

class DatabaseFromCSV():
    # connection to database
    con = psycopg2.connect(dbname='postgres', user='psql_admin', password='password')

    # path to folder containing .csv files
    folder_path = './baseballdatabank-2019.2/core/'

    def start(self):
        # time how long to create database
        start = time.time()

        # create database
        dbname = input('What would you like to name the database? ')
        self.con.autocommit = True
        cur = self.con.cursor()
        cur.execute('CREATE DATABASE {};'.format(dbname))

        # connect to newly created database
        self.con = psycopg2.connect(dbname=dbname, user='psql_admin', password='password')
        self.con.autocommit = True

        # ho through all files in given folder path and create a table for each .csv file
        files = os.listdir(self.folder_path)
        for file in files:
            if file[-4:] == '.csv':
                self.create_table(file)
            
        # calculate total time to create database
        total_time = time.time() - start
        print('***** DONE - Time: ', total_time)

    def create_table(self, name):
        cur = self.con.cursor()
        table = name[:-4].lower()

        with open('{}{}'.format(self.folder_path, name)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            all_records = ""

            for row_num, row in enumerate(csv_reader):
                if row_num == 0:
                    # Create table with this row being the column headers
                    column_names = ""

                    for col_num, r in enumerate(row):                        
                        r = r.replace('\'', '')

                        if (col_num == 0):
                            column_names = column_names + "\"{}\" VARCHAR(200)".format(self.clean_column_name(r))
                        else:
                            column_names = column_names + ", \"{}\" VARCHAR(200)".format(self.clean_column_name(r))

                    cur.execute('CREATE TABLE {} ({});'.format(table, column_names))

                else: 
                    # create a new record of this row
                    record = ""

                    for col_num, r in enumerate(row):
                        if not r:
                            record = record + ", null"
                            continue
                        
                        r = r.replace('\'', '')

                        if (col_num == 0):
                            record = record + "\'{}\'".format(r)
                        else:
                            record = record + ", \'{}\'".format(r)

                    if row_num == 1:
                        all_records = all_records + "({})".format(record)
                    else: 
                        all_records = all_records + ", ({})".format(record)
            
            # insert all records at once to minimize database calls
            cur.execute('INSERT INTO {} VALUES {};'.format(table, all_records))

            print(name, ' is complete.')

    @staticmethod
    def clean_column_name(name):
        name = name.replace('\'', '')
        name = name.replace('.', '_')
        if name == '2B':
            name = 'DBL'
        if name== '3B':
            name = 'TPL'
        return name


DatabaseFromCSV().start()