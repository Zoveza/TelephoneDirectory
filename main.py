from os.path import exists
from csv_creator import creating
from format import writing_scv
from format import writing_txt


path = 'Telephonedirectory.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()