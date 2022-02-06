import csv
from turtle import pos

from sympy import lowergamma

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
     
    

     number1 = float(row[1])
     dog_docs.append(number1)

     number2 = float(row[2])
     goat_docs.append(number2)

     number3 = float(row[3])
     peace_docs.append(number3)

     number4 = float(row[4])
     image_query.append(number4)

     list_vari = [row[0], number1, number2, number3, number4]
     terms_and_numbers.append(list_vari)

     a = a + 1
    if a == 1:
        # dont use row 0
        print("run document")
        
        a = a + 1
       
     
csv_file.close() 


print(terms_and_numbers)
print(terms_and_numbers[2])




scores = {}

voorbeeld_b = image_query # current query used is image_song.txt


for document, value  in documents_and_values.items():
    voorbeeld_a = value
    print("for", document, ":")

    dotproducts = []
    pos_index = 0

    for cijfers in voorbeeld_a: 
        a_term = cijfers
    
       

        try:
            b_term = voorbeeld_b[pos_index]
        except: 
            print("")

        pos_index = pos_index + 1

        
        dotproduct = (a_term * b_term)
        dotproducts.append(dotproduct)



        new_dotproduct = 0

        for dp in dotproducts:
            new_dotproduct = new_dotproduct + dp

    

      

        powers_a = []
        powers_b = []
        for cijfer_3 in voorbeeld_a:
            power_a = cijfer_3 ** (2)
            powers_a.append(power_a)

        sum_powers_a = 0
        sum_powers_b = 0

        for cijfer in powers_a:
            sum_powers_a= sum_powers_a + cijfer



        for cijfer_3 in voorbeeld_b:
            power_b = cijfer_3 ** (2)
            powers_b.append(power_b)

        for cijfer in powers_b:
            sum_powers_b= sum_powers_b + cijfer

        length_a = sum_powers_a ** (0.5)
        length_b = sum_powers_b ** (0.5)


        #vectorlenght conclusie 
        calculated_vector = (new_dotproduct) / (length_a * length_b)
    
    print("similarity: ", calculated_vector)
    
    print("termweight:", new_dotproduct)
    
    scores[document] = str(calculated_vector)
        





#show ranked output
unranked = scores.items()
ranked = sorted(unranked, key=lambda score: score[1], reverse=True)
print(ranked)

ranked_texts = []
ranked_scores = []



i = 0

for a in ranked:
    ranked_texts.append(ranked[i][0])
    ranked_scores.append(float(ranked[i][1]))
    i = i + 1



scales = []
for score in ranked_scores:
    float(score)
    if score < 1:
        scale = "low"
        scales.append(scale)
    if score > 1:
        scale = "high"
        scales.append(scale)

rank = []
x = len(ranked_scores)
for a in range(x):
    rank.append(a)

matrix = [["position", "document", "similarity", "scale"],rank,ranked_texts,ranked_scores,scales]
print(matrix)

# lemmingsation

