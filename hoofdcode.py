from flask import Flask
from flask import render_template
from flask import request
from pandas import DataFrame, Series
import nltk
import csv
from nltk.stem import  SnowballStemmer
nltk.download("punkt")
from werkzeug.utils import secure_filename

app = Flask(__name__)

#folder from which uploading documents can be chosen
UPLOAD_FOLDER = '/'



#the search engine reads tfidf matrix from a csv file
csv_file = open("stories_collection\stories.csv", "r", newline='')
read = csv.reader(csv_file, delimiter=',') 
a = 1
terms = list()
terms_and_numbers = list()

#extra lists of documents
dog_docs = list()
goat_docs = list()
peace_docs = list()
image_query = list()

# all_documents
documents_and_values = {"d_01_greedog.txt" : dog_docs, "d_02_obstgoat.txt" : goat_docs, "d_03_peace.txt" : peace_docs}


# read document

for row in read:    
    if  a > 1:
     terms.append(row[0])
     
    
    # put each termweight in the corresponding document
     number1 = float(row[1])
     dog_docs.append(number1)

     number2 = float(row[2])
     goat_docs.append(number2)

     number3 = float(row[3])
     peace_docs.append(number3)

     number4 = float(row[4])
     image_query.append(number4)

     list_vari = [row[0], number1, number2, number3, number4]
     #combine each term with its correstponding termweights in the documents
     terms_and_numbers.append(list_vari)

     a = a + 1
    if a == 1:
        # dont use row 0
        print("run document")
        
        a = a + 1
       
#close the filenumber 1
csv_file.close() 


# list to store the scores for each document (calculated below)
scores = {}

example_b = image_query # current query used is image_song.txt

#for each document calculate the dotproduct
for document, value  in documents_and_values.items():
    example_a = value
    print("for", document, ":")

    #list to store dotprocucts in
    dotproducts = []
    # the index of 
    pos_index = 0

    #store each digit in document a and in document b through a loop 
    for digit in example_a: 
        a_term = digit
    
       
        #check if document a and b are the same length
        try:
            b_term = example_b[pos_index]
        except: 
            print("")

        # keep increasing the index of doc b equally to the index of the digits in doc a
        pos_index = pos_index + 1

        # calculate the dotpoduct for each iteration of the digits in document a 
        dotproduct = (a_term * b_term)
        dotproducts.append(dotproduct)


        # the default value of the dotproduct is zero
        new_dotproduct = 0

        # calculate the termweights for each document 
        for dp in dotproducts:
            new_dotproduct = new_dotproduct + dp

    

      
        # store the powers of document a and b 
        powers_a = []
        powers_b = []

        # calculate the powers of document a
        for cijfer_3 in example_a:
            power_a = cijfer_3 ** (2)
            powers_a.append(power_a)

        # the default of the sum of the powers of the digits in document a and b are 0
        sum_powers_a = 0
        sum_powers_b = 0

        # all the powers of a will be summed up
        for cijfer in powers_a:
            sum_powers_a= sum_powers_a + cijfer


        # calculate the powers of document a
        for cijfer_3 in example_b:
            power_b = cijfer_3 ** (2)
            powers_b.append(power_b)

        # all the powers of a will be summed up
        for cijfer in powers_b:
            sum_powers_b= sum_powers_b + cijfer

        length_a = sum_powers_a ** (0.5)
        length_b = sum_powers_b ** (0.5)


        #the vectorlenght calculated for each document
        calculated_vector = (new_dotproduct) / (length_a * length_b)
    
    print("similarity: ", calculated_vector)
    
    print("termweight:", new_dotproduct)
    
    # the scores of the document are the calculated vectorlengths
    scores[document] = str(calculated_vector)
        




#each document will be ranked through their corresponding score
unranked = scores.items()
ranked = sorted(unranked, key=lambda score: score[1], reverse=True)
print(ranked)

# all text ordered by rank
ranked_texts = []
# all scores ranked
ranked_scores = []


# default of i  is 0, used to order by rank
i = 0


for a in ranked:
    # each first value corresponts to a text that will be stored in ranked text
    ranked_texts.append(ranked[i][0])
    # each second value corresponts to a score that will be stored in ranked_scores
    ranked_scores.append(float(ranked[i][1]))
    i = i + 1


# for each score determing if the ranking is low or high
scales = []
for score in ranked_scores:
    float(score)
    if score < 1:
        scale = "low"
        scales.append(scale)
    if score > 1:
        scale = "high"
        scales.append(scale)

# rank stores the position of the documents
rank = []
x = len(ranked_scores)
for a in range(x):
    rank.append(a+1)

# build a matrix that can be printed in a html file
matrix = [["position", "document", "similarity", "scale"],rank,ranked_texts,ranked_scores,scales]
print(matrix)

csv_file.close()
# lemmingsation



# open the english version of stop_words.txt
stop_doc = open("stop_words\english", "r", newline='')

# list to store stopwords in
stopwords = []

# read through stop_words.txt and store each stopword in "stopwords = []"
while(True): 
    data = stop_doc.readline()
    if not data:
        break
    stop_word = data.strip()
    stopwords.append(stop_word)



print(stopwords)
# close the document containing the stopwords
stop_doc.close()


# use covid.txt to test the lemming
with open("news_collection\d1_covid.txt", "r") as covid:
    corpus = covid.read()
    
# from the body of the tekst divide each term into sentences and words
sents = nltk.sent_tokenize(corpus)
print(sents)
words = nltk.word_tokenize(corpus)
print(words)

# list to store final_tokens in 
final_tokens = []
# puntionation characters that need to be removed
remove_characters = ["!", "#", "(", ")", "*", "-", "+" ,"/", ";", ":", "<", ">", "=", "?", "@", "[", "]", "^", "_", "\`", "{", "}", "~", "\\", "\"", "\'", "1", "2", "3", "4", "6", "7", "8", "9", "0", ",", "."]

# for each word in the text check if they are not stopwords or puntiation marks 
for word in words: 
    if not word in stopwords:
        if not word in remove_characters:
            # if not the case store the words in "final_tokens"
            final_tokens.append(word)


# each words will be reduced to its stem
stemmer = SnowballStemmer('english')
stemmed_words = [stemmer.stem(word) for word in final_tokens]



# open a website to show results into 
@app.route('/')
def  my_GUI():
    my_matrix = matrix
    return render_template('GUI.html', matrix_py = my_matrix)

# when uploading a text check if it is uploaded successfully
@app.route('/files', methods = ['GET', 'POST'])
def upload_fileS():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
def chosen_file():
    print("Gekozen:", request.form["Select a document"])




if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.config['DEBUG'] = True
    app.config['SERVER_NAME'] = "127.0.0.1:5000"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run()