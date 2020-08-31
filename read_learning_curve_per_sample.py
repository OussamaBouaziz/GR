# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from matplotlib import pyplot as plt
import platform
from pathlib import Path
import os , sys
#This function can be improved :
    #Solve the MAJ problem
    #Correct the path :
        #C:\Users\User\Documents\GitHub\benchmark1\grobid-dictionaries_data\DLF\(anything)

def ask():

    print("Write the path to the dictionary whose scoring you want to visualize. ")
    urpath = input()

    if platform.system() == 'Windows':
        dict_path_arr = str(urpath).split('\\')
    else:
        dict_path_arr = str(urpath).split('/')




    index = dict_path_arr.index("grobid-dictionaries_data")
    dict_name1 = dict_path_arr[index + 1]

    while len(dict_path_arr) - 1 > (index + 1):
        dict_path_arr.remove(dict_path_arr[index + 2])

    #for i in range(index):
        #index = dict_path_arr.index("grobid-dictionaries_data")
        #dict_path_arr.remove(dict_path_arr[index - 1])

    dict_root1 =  Path(get_root_from_table(dict_path_arr))
    if platform.system() == 'Windows':
        urpath  = "\\".join(dict_path_arr)
        urpath2 = urpath + "\evalWAPITI"
    else:
        urpath = str(urpath).split('/')
        urpath2 = urpath + "/evalWAPITI"

    dirt = os.listdir(urpath2)
    print(urpath2)

    return dict_path_arr, dict_root1, dict_name1, dirt


def get_root_from_table(table):
    root_path=""
    for element in table:
        if element == "evalWAPITI":
            break
        else:
            if not (element ==""):
                root_path += element +"/"

    return root_path

def get_feature_for_model(model_name, dictionary, ff):
    dictionary = dictionary[2]



    if model_name == "dictionary-segmentation":
        ff="Bigram"

    if model_name == "dictionary-body-segmentation":
        ff="Engineered"

    if model_name == "lexical-entry":
        if dictionary =="DLF" or dictionary == "Eebd" :
            ff="Bigram"
        else:
            ff="Engineered"

    if model_name == "form":
        if dictionary =="Eebd" :
            ff="Unigram"
        else:
            ff="Bigram"

    if model_name == "gramGrp":
        ff="Unigram"

    if model_name == "sense":
        if dictionary == "Eebd" :
            ff="Unigram"
        else:
            ff="Engineered"

    if model_name == "sub-sense":
        ff="Bigram"

#ff = "Bigram" if [(model_name = sub-sense, form, dictionary-segmentation)
    # or (model_name=lexical_entry and dictionary= DLF or Eebd) or
#ff = "Engineered if model_name = dictionary-body-segmentation
#ff = Unigram if model_name = gramGrp

    return ff


def getarraysfromdict(dictModel,kk):
    sizearray=[0]
    scorearray=[0]

    #print("get root from this table >>> ", dictionary[0])
    #print(get_root_from_table(dictionary[0]), "<<< this root")
    #print("dict root ", dictionary[1])

    for i in range(1,5):
        filepath = dictionary[1]/ "dataset" / dictModel/ "corpus/batches"/str(i)/"size.txt"
        fileName="Feature"+kk+"DataLevel"+str(i)+".txt"
        filepathData = dictionary[1]/ "evalWAPITI" / dictionary[2] /dictModel/ str(fileName)
        print ("sizepath ", filepath)
        print ("datapath ", filepathData)
        #fill in the batche size array incrementally

        with open(filepath) as fp:
            line = fp.readline()
            previous=sizearray[i - 1]
            sizearray.append(int(previous) + int(str(line).split(' ')[0]))
            print ("Batches' sizes",sizearray,)

        #fill in the fscore of macroaverage
        with open(filepathData) as fp:
            line = fp.readline()
            #OB : the above defined variable does not seem to be used, why is it there?
            while line:
                line=" ".join(line.split())
                if "(macro" in str(line).split(' '):
                    splitLine = str(line).split(' ')
                    # print (splitLine)
                    scorearray.append(splitLine[len(splitLine) - 2])
                line = fp.readline()
    return sizearray, scorearray;



fk="Engineered"
#OB: These are void tables that will be filled with the batch sizes for each dictionary and the scorings that we want to detect.
ds_size=[]
ds_score=[]

dbs_size=[]
dbs_score=[]

le_size=[]
le_score=[]

form_size=[]
form_score=[]

gramGrp_size=[]
gramGrp_score=[]

sense_size=[]
sense_score=[]

subsense_size=[]
subsense_score=[]

def get_curve_dictionary (arrModels,fk):
        dictname = dictionary[2]


        for dictModel in arrModels:
            if dictModel in os.listdir(dictionary[1] / "dataset/"):
                print("***", dictModel, "****")
                #This can be improved into a dictionary in order to avoid having so many "ifs"
                    #(if dictModel== "dictionary-segmentation") <-- this can be a problem because there are two actions involved.
                if dictModel== "dictionary-segmentation":
                    fk=get_feature_for_model(dictModel, dictname, fk)
                    ds_size, ds_score = getarraysfromdict( dictModel,  fk)

                if dictModel== "dictionary-body-segmentation":

                    dbs_size, dbs_score = getarraysfromdict( dictModel,  fk)

                if dictModel== "lexical-entry":
                    le_size, le_score = getarraysfromdict( dictModel,  fk)

                if dictModel== "form":
                    form_size, form_score = getarraysfromdict( dictModel,  fk)

                if dictModel== "gramGrp":
                        gramGrp_size, gramGrp_score = getarraysfromdict( dictModel,  fk)
                # print("skip")

                if dictModel== "sense":
                    sense_size, sense_score = getarraysfromdict( dictModel,  fk)

                if dictModel== "sub-sense":
                    subsense_size, subsense_score = getarraysfromdict( dictModel,  fk)



        #OB: plotting everything I guess

        fig = plt.figure()
        fig.set_size_inches(20.5, 10.5,44)
        x = np.array(range(0, 110, 1))

        plt.plot( [float(x) for x in ds_size], [float(x) for x in ds_score], label='Dictionary Segmentation', linewidth=5.0, color='deepskyblue')
        plt.plot( [float(x) for x in dbs_size], [float(x) for x in dbs_score], label='Dictionary Body Segmentation', linewidth=5.0, color='teal')
        plt.plot( [float(x) for x in le_size], [float(x) for x in le_score], label='Lexical Entry', linewidth=5.0, color='magenta')
        plt.plot( [float(x) for x in form_size], [float(x) for x in form_score], label='Form', linewidth=5.0, color='royalblue')
        if not (dictname == "FrFang"):
            plt.plot( [float(x) for x in gramGrp_size], [float(x) for x in gramGrp_score], label='GramGrp', linewidth=5.0, color='orange')
        plt.plot( [float(x) for x in sense_size], [float(x) for x in sense_score], label='Sense', linewidth=5.0, color='rosybrown')
        plt.plot( [float(x) for x in subsense_size], [float(x) for x in subsense_score], label='Sub-sense', linewidth=5.0, color='springgreen')

        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)

        plt.ylim((0,105))

        plt.xlabel('Page number', fontsize=16)
        plt.ylabel('F1-score (Macro-average)', fontsize=16)
        # plt.title(dictname+"'s Learning Curves", fontsize=16)
        plt.legend(fontsize=16)
        fig.savefig(f'figures/Curve_{dictname}.png', dpi=100)
        plt.close(fig)

arrDictModels = ["dictionary-segmentation", "dictionary-body-segmentation", "lexical-entry", "form", "gramGrp", "sense", "sub-sense"]
again = True
while again == True:
    dictionary = ask()
    get_curve_dictionary(arrDictModels, fk)
    print("0 :", dictionary[0])
    print("1 :>", dictionary[1])
    print("2 :>>", dictionary[2])
    print(type(dictionary[2]))
    print("3 :>>>", dictionary[3])
    print(type(dictionary[3]))

    print("Another one ? (Y/N)")
    x=input()
    if "n" in x or "N" in x:
        again = False
        break
    else:
            again = True


#print(type(dictionary[0]),"???")
#print(os.listdir(dictionary[1]/"dataset/"),"fökdhfikfnwlgkenhöoklfmg")