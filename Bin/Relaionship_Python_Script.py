import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import logging
import datetime
import sys
import os
import glob
import sys
#os.getcwd()
#os.chdir('../../Consensus/Bin')
BIN_DIR= os.getcwd()
PROJ_DIR = os.path.dirname(BIN_DIR)
LOG_DIR = os.path.join(PROJ_DIR, 'Logs')
now = datetime.datetime.now()
logfile = "Relationships_{0}.log".format(now.strftime('%Y-%m-%d_%H%M%S'))
logging.basicConfig(filename=os.path.join(LOG_DIR, logfile), level=logging.DEBUG, 
        format='PID:%(process)d - %(asctime)s - %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.info('Log file created')
# Reading config file
conf_path = os.path.join(BIN_DIR, "config.txt")
with open(conf_path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content] 
try:
    INPUT_DIR = content[0]
    OUTPUT_DIR = content[1]
except Exception as error:
        logging.error("Failed to Find Input/Output Folder: {}".format(content))
        logging.exception(error)
        sys.exit(1)
else:
        logging.info('Input and Output directories found')
i=0
path_in= os.path.join(INPUT_DIR, "*.csv")
for filename in glob.glob(path_in):
     i=i+1
     file = os.path.basename(filename)
     out =  "output_"+file
     outfile = os.path.join(OUTPUT_DIR,out)
     try:
         df = pd.read_csv(filename)
     except Exception as error:
        logging.error("Failed to read the file: {}".format(filename))
        logging.exception(error)
        sys.exit(1)
     else:
        logging.info("Retrieving the files in the input folder")
     #print(file)
     df['Artifact_ID']=range(1, 1+len(df))
     val = df['Artifact_ID'].max()+1
     df['Artifact_ID']=df['Artifact_ID'].apply(str)
     grp = df.groupby(['Parent Name','Parent Artifact Type']).agg({'Artifact_ID' : lambda x: ' '.join(x)})
     grp = grp.reset_index(level=['Parent Name', 'Parent Artifact Type'])
     grp.columns = ['Name','Artifact Type','Diagram Relationship']
     grp['Artifact_ID']=range(val, val+len(grp))
     grp['Artifact_ID']=grp['Artifact_ID'].apply(str)
     df.drop(df.columns[[0,1]], axis=1, inplace=True)
     df['Diagram Relationship']=''
     df = df[['Child Name', 'Child Artifact Type', 'Diagram Relationship','Artifact_ID']]
     df.columns= ['Name','Artifact Type','Diagram Relationship','Artifact_ID']
#list(df.columns.values)
     new_grp = pd.concat([df,grp],ignore_index=True).drop_duplicates().reset_index(drop=True)
     new_grp=new_grp[['Artifact_ID', 'Diagram Relationship','Name','Artifact Type']]
     logging.info('Processing completed for File: {}'.format(filename))
#writing output to a csv
     try:
        new_grp.to_csv(outfile, index = False)
     except Exception as error:
        logging.error("Could not write the dataframe to csv")
        logging.exception(error)
        sys.exit(1)
     else:
        logging.info('Processing Completed Successfully')
print("Processing Done")   