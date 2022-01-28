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
a = 1
terms = list()
terms_and_numbers = list()

#extra lists of documents
dog_docs = list()
goat_docs = list()
peace_docs = list()
image_docs = list()



# read document

for row in read:    
    if  a > 1 and a < 5:
     terms.append(row[0])
     print(row [0])
    

     number1 = float(row[1])
     dog_docs.append(number1)

     number2 = float(row[2])
     goat_docs.append(number2)

     number3 = float(row[3])
     peace_docs.append(number3)

     number4 = float(row[4])
     image_docs.append(number4)

     list_vari = [row[0], number1, number2, number3, number4]
     terms_and_numbers.append(list_vari)

     a = a + 1
    if a == 1:
        # dont use row 0
        print("a word 2 door 2")
        a = a + 1
     
csv_file.close() 
print(terms)

print(terms_and_numbers)
print(terms_and_numbers[2])
#calculate document vector lengts

#run query

#show ranked output





    

if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD']=True
	app.config['DEBUG'] = True
	app.config['SERVER_NAME'] = "127.0.0.1:5000"         
	app.run()