import csv
import json
data=[]
with open('c:/Users/harek/Desktop/training/hk_anck/csvfile.csv','r') as c_file:
    reader=csv.reader(c_file)
    for row in reader:
        data.append(row)
with open("jsonfile",'w') as j_file:
    json.dump(data,j_file)
#data=f.read()
#with open('new.json','w') as js:
 #   json.dump(data,js)
#f.close()
print("file created succesfully")
