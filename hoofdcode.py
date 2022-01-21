from flask import Flask
from flask import render_template
from flask import request
from pandas import DataFrame, Series
import nltk
import csv


app = Flask(__name__)


@app.route('/')
def  my_choice():
    print('data')
    return 'hi'


#the search engine reads tfidf matrix from a csv file
csv_file = open("stories.csv", "r", newline='')
read = csv.reader(csv_file, delimiter=',')

for row in read:    
    print(row[0], row[1], sep=' ')
    print(row[2], end='\n'*2)
csvfile.close() 


#calculate document vector lengts

#run query

#show ranked output

#Cosinescore(q) acording to manning pg. 125
float Scores[n] = 0
intialize length[n]
for each query term t:
do calculate wt,d and fetch postings list for t
    for each pair (d,tftd) in posting list:
        do Scores[d] += wft,d x wt,q
Read the array Length[d]
for each d:
do Scores[d] = Scores[d]/Length[d]
return Top K components of Scores[]
#end manning



    

if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD']=True
	app.config['DEBUG'] = True
	app.config['SERVER_NAME'] = "127.0.0.1:5000"         
	app.run()