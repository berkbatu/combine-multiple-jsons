import pandas as pd
import os

#To get this working, you'll need to modify it according to your file and json structure. Feel free to contact for info.
with open('directory', encoding='utf-8') as inputfile: # pull the file names, I need to merge 100s of files in a folder named as dates. Which have the same Json structure. Final goal is to combine them and export
    df = pd.read_json(inputfile)
filePaths=os.listdir("directory")
for i in range(len(filePaths)):
    with open('directory'+filePaths[i], encoding='utf-8') as inputfile:
            df = pd.read_json(inputfile)
            x=str(filePaths[i].rsplit('_')[2].rsplit('.')[0]) # I needed to pull the file names and insert them into the jsons because file names are the create dates in a 20220202 format. So I process the date and add it in the json.
            y=x[:4]+'-'+x[4:6]+'-'+x[6:8]
            df['Inside the Json'][0]
            for a in range(len(df2['Inside the Json'][0])):
                df['Inside the Json'][0][a]['date']=y #create a date field and add the file name to it

df.to_csv("distettecsv", encoding='utf-8', index=False) # export the data frame to CSV or what you prefer.
        