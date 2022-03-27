from lxml import etree
import os
os.listdir
from os.path import isfile, join
from Orange.data import Domain,Table
from Orange.data import (
    Unknown, Variable, ContinuousVariable, DiscreteVariable, StringVariable
)

path='/Users/shuda/OneDrive/Desktop/orange  assg'
path2=os.path.join("/Users/shuda/OneDrive/Desktop/orange  assg")
FichList = [ join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
print( FichList )


#print(os.listdir(path)) # print a list of all files in the directory.It does not include the paths of the files


data = []

for f in FichList :
#iteration over the files to extract all the information below
    parser = etree.XMLParser(recover=True)
    tree = etree.parse(f, parser=parser)
    root = tree.getroot()
    data.append([
        root.findtext(".//year"),
        root.findtext(".//month"),
        root.findtext(".//article-title"),
        'ML'
    ])


year = ContinuousVariable('year')
month = ContinuousVariable('month')
title = StringVariable('title')
topic = StringVariable('topic')

domain = Domain([year, month], metas=[title, topic])
#metas with array with meta attributes
table = Table.from_list(domain, data)

out_data = table

print(data)







