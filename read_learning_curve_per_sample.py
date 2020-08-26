# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from matplotlib import pyplot as plt
import platform
from pathlib import Path

arrDictModels= ["dictionary-segmentation", "dictionary-body-segmentation", "lexical-entry", "form", "gramGrp", "sense", "sub-sense"]

#OB: assigning a path (of type path) to each of the variables.
dict_folderEEBD = Path("grobid-dictionaries_data/EEBD/dataset/")
dict_folderMxSp = Path("grobid-dictionaries_data/MxSp/dataset/")
dict_folderFangFr = Path("grobid-dictionaries_data/FangFr/dataset/")
dict_folderFrFang = Path("grobid-dictionaries_data/FrFang/dataset/")
dict_folderDLF = Path("grobid-dictionaries_data/DLF/dataset/")

# batch_folderDLF = Path("/Users/med/Google Drive/experimentDisseration/BasicEnglish2020/dataset/")

# data_folderDLF = Path("/Users/med/Google Drive/experimentDisseration/BasicEnglish2020/evalWAPITI/Eebd/")

data_folderEEBD = Path("grobid-dictionaries_data/EEBD/evalWAPITI/eebd/")

#OB: depending on strings existing in model_name the ff variable will take the next string in order to
# get to the feature (completing the path).
def get_root_from_table(table):
    root_path=""
    for element in table:
        if element == "evalWAPITI":
            break
        else:
            if not (element ==""):
                root_path += element +"/"

    return root_path
def ask():
    print("write the path")
    urpath = input()
    dict_path1 = str(urpath).split('\\')
    print(dict_path1)
    print(type(dict_path1))
    index = dict_path1.index("grobid-dictionaries_data")
    pointeur = dict_path1[index + 1]
    dict_name1 = dict_path1[index + 1]
    for i in range(index):
        index = dict_path1.index("grobid-dictionaries_data")
        # print(index)
        dict_path1.remove(dict_path1[index - 1])


    dict_root1 = Path(get_root_from_table(dict_path1))
    completion = {
        "EEBD": "EEBD",
        "FangFr": "Fang-Fr",
        "MxSp": "Mix-Sp",
        "FrFang": "FrFang",
        "DLF": "DLF"
    }
    comp = completion.get(pointeur)
    #print(completion)
    #comp_name = completion[dict_path1[index + 1]]
    #print(comp_name)
    print("The path ", dict_path1)
    #print("The root ", dict_root1)
    #print("The name", dict_name1)
    return dict_path1, dict_root1, dict_name1, comp
dictionary=ask()
print(dictionary[3],"completion ")


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

#OB: Replaced the function,
#OB: takes an array and returns a string.
#OB: The path,or root, initialized as a null string, is being constituted after
# each iteration. It will later (function: getarraysfromdict) constitute a part of the path leading to the batch



# OB: Replaced function above this one.
def getarraysfromdict(dict_path, dictModel,dict_name,kk):
    sizearray=[0]
    scorearray=[0]
    #print("Please enter the Path of the dictionary you want to evaluate")
    #urpath = input()



    #if platform.system() == 'Windows':
     #   dict_path1= str(urpath).split('\\')
    #else:
     #   dict_path1= str(urpath).split('/')


    #OB: changing the type of an array of strings into pathlib.WindowsPath
    #OB: These are relative paths
    dict_root = Path(get_root_from_table(dictionary[0]))
    print("dict path ", dictionary[0])
    print("dict root ", dictionary[1])

    print(get_root_from_table(dictionary[0]),"+++++++++")
    #OB: C'est une variable clé 1 !
    # OB: Alors dict_path doit être retirée de cette boucle et doit être eingegeben as input().
    # OB: dictpath probably won't be needed !
    for i in range(1,5):
        filepath = dictionary[1]/ "dataset" / dictModel/ "corpus/batches"/str(i)/"size.txt"
        fileName="Feature"+kk+"DataLevel"+str(i)+".txt"
        filepathData = dictionary[1]/ "evalWAPITI" / dictionary[3] /dictModel/ str(fileName)
        print ("sizepath ", filepath)
        print ("datapath ", filepathData)
        #fill in the batche size array incrementally
        #OB: well this [fp, open(), readline()] is new to me  !
        with open(filepath) as fp:
            line = fp.readline()
            previous=sizearray[i - 1]
            sizearray.append(int(previous) + int(str(line).split(' ')[0]))
            print ('size',sizearray)
            #OB: I guess this is a part from the output: the table where the batch sizes are recorded.
            #OB: This is a modified function.
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

#OB: So if the Output of a function is a plot we don't need return ?
def get_curve_dictionary (arrModels,fk):
    data_folderEEBD = Path("grobid-dictionaries_data/EEBD/evalWAPITI/eebd/")
    data_folderMxSp = Path("grobid-dictionaries_data/MxSp/evalWAPITI/Mix-Sp/")
    data_folderFangFr = Path("grobid-dictionaries_data/FangFr/evalWAPITI/Fang-Fr/")
    data_folderFrFang = Path("grobid-dictionaries_data/FrFang/evalWAPITI/FrFang/")
    data_folderDLF = Path("grobid-dictionaries_data/DLF/evalWAPITI/DLF/")

    arrPaths= [data_folderEEBD, data_folderMxSp, data_folderFangFr, data_folderFrFang, data_folderDLF]

    for dict_path in arrPaths:
        if platform.system() == 'Windows':
            dictpatharray = str(dict_path).split('\\')
        else:
            dictpatharray = str(dict_path).split('/')

        dictname = dictionary[2]
        print("****",dictname,"****")
        for dictModel in arrModels:
            if dictModel== "dictionary-segmentation":
                fk=get_feature_for_model(dictModel, dictname, fk)
                ds_size, ds_score = getarraysfromdict(dictpatharray, dictModel, dictname, fk)

            if dictModel== "dictionary-body-segmentation":
                dbs_size, dbs_score = getarraysfromdict(dictpatharray, dictModel,dictname, fk)

            if dictModel== "lexical-entry":
                le_size, le_score = getarraysfromdict(dictpatharray, dictModel, dictname, fk)

            if dictModel== "form":
                form_size, form_score = getarraysfromdict(dictpatharray, dictModel, dictname, fk)

            if dictModel== "gramGrp":
                if not (dictname == "FrFang"):
                    gramGrp_size, gramGrp_score = getarraysfromdict(dictpatharray, dictModel, dictname, fk)
                # print("skip")

            if dictModel== "sense":
                sense_size, sense_score = getarraysfromdict(dictpatharray, dictModel, dictname, fk)

            if dictModel== "sub-sense":
                subsense_size, subsense_score = getarraysfromdict(dictpatharray, dictModel, dictname, fk)



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


get_curve_dictionary(arrDictModels,fk)

# dictnamearray = str(data_folderEEBD).split('/')
# print(dictnamearray)
# print(get_root_from_table(dictnamearray))
#save check
