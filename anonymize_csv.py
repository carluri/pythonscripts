from pathlib import Path
import csv
import random
from faker import Faker

fake=Faker()

p = Path('.')

# Find all files in folder
fileslist=list(p.glob('**/*.csv'))

# Set the folder for the anonymized files
outfolder = 'anon'

for file in fileslist:
    randid=random.randint(10000,99999)
    randid2=random.randint(10000,99999)
    a=fake.date_between(start_date='+10y',end_date='+14y')
    randdate=f'{str(a.day).zfill(2)}-{str(a.month).zfill(2)}-{a.year}'
    
    readFile=open(file,'r')
    writeFile=open(f'./{outfolder}/{randid2}.csv', 'w') 
    print(file)
    for row in readFile:
        # Add for fields to be changed
        if 'Field1' in row:
            writeFile.write(f'Field1={randid}\n')
        elif 'Field2' in row:
            writeFile.write(f'Field2={randid2}\n')
        elif 'Date' in row:
            writeFile.write(f'Date={randdate}\n')
        else: 
            writeFile.write(row)
    
    #Close and write new files
    readFile.close()
    writeFile.close()