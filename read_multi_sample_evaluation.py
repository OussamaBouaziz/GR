#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:43:51 2020

@author: Med
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from pathlib import Path

arrDictModels= ["dictionary-segmentation", "dictionary-body-segmentation", "lexical-entry", "sense", "sub-sense", "form", "gramGrp"]
arrFeatures= ["Unigram", "Engineered", "Bigram"]
modelLabels =[]

data_folderEEBD = Path("grobid-dictionaries_data/EEBD/evalWAPITI/Eebd/")
data_folderMxSp = Path("grobid-dictionaries_data/MxSp/evalWAPITI/Mix-Sp/")
data_folderFangFr = Path("grobid-dictionaries_data/FangFr/evalWAPITI/Fang-Fr/")
data_folderFrFang = Path("grobid-dictionaries_data/FrFang/evalWAPITI/FrFang/")
data_folderDLF = Path("grobid-dictionaries_data/DLF/evalWAPITI/DLF/")

font = {'weight' : 'normal',
        'size'   : 16}
matplotlib.rc('font', **font)

def generate_figure_per_feature (arrDictModel, kk):

    mx_ma='-1';
    eebd_ma='-1';
    fangfr_ma='-1';
    frfang_ma='-1';
    dlf_ma='-1';

    EEBDArray = []
    MxSpArray = []
    FangFrArray = []
    FrFangArray = []
    DLFArray = []

    fileName="Feature"+kk+"DataLevel4.txt"
    filePathMxSp =  data_folderMxSp/ arrDictModel / fileName
    filePathEEBD =  data_folderEEBD/ arrDictModel / fileName
    filePathFangFr =  data_folderFangFr/ arrDictModel / fileName
    filePathFrFang =  data_folderFrFang/ arrDictModel / fileName
    filePathDLF =  data_folderDLF/ arrDictModel / fileName
    arrPaths= [filePathEEBD, filePathMxSp, filePathFangFr, filePathFrFang, filePathDLF]
    # print(filePathDLF)
    for pp in arrPaths:
        # labels = {"lemma":"-1", "etym":"-1", "sense":"-1", "inflected":"-1", "note":"-1", "re":"-1", "usg":"-1", "xr":"-1","dictScrap":"-1"}
        if arrDictModel == "dictionary-segmentation":
            modelLabels = ["headnote", "body", "footnote"]
            labels = {"headnote":"-1", "body":"-1", "footnote":"-1"}

        if arrDictModel == "dictionary-body-segmentation":
            modelLabels = ["entry", "dictScrap" , "pc"]
            labels = {"entry":"-1", "dictScrap":"-1" , "pc":"-1"}

        if arrDictModel == "lexical-entry":
            modelLabels = ["lemma", "inflected", "etym", "sense", "note", "re", "usg", "xr", "dictScrap"]
            labels = {"lemma":"-1", "inflected":"-1", "etym":"-1", "sense":"-1", "note":"-1", "re":"-1", "usg":"-1", "xr":"-1", "dictScrap":"-1"}

        if arrDictModel == "form":
            modelLabels = ["gramGrp", "lbl", "orth", "part", "pron", "usg", "pc"]
            labels = {"gramGrp":"-1", "lbl":"-1", "orth":"-1", "part":"-1", "pron":"-1", "usg":"-1", "pc":"-1"}

        if arrDictModel == "gramGrp":
            modelLabels = ["gram", "lbl" , "note", "number", "pos", "pc"]
            labels = {"gram":"-1", "lbl":"-1" , "note":"-1", "number":"-1", "pos":"-1", "pc":"-1"}

        if arrDictModel == "sense":
            modelLabels = ["gramGrp", "num" , "subSense", "pc"]
            labels = {"gramGrp":"-1", "num":"-1", "subSense":"-1", "pc":"-1"}

        if arrDictModel == "sub-sense":
            modelLabels = ["def", "etym", "example", "gramGrp", "note", "num", "re", "translation", "usg", "xr", "pc"]
            labels = {"def":"-1", "etym":"-1", "example":"-1", "gramGrp":"-1", "note":"-1", "num":"-1", "re":"-1", "translation":"-1", "usg":"-1", "xr":"-1", "pc":"-1"}

        if (arrDictModel== "gramGrp"):
            if not (pp == filePathFrFang):
                with open(pp) as fp:
                    line = fp.readline()
                    cnt = 1
                    while line:
                        line=" ".join(line.split())
                        # print (str(line))
                        label=str(line).split(' ')[0]
                        if label.startswith('<') :
                            label=label.replace("<",'')
                            label=label.replace(">",'')
                            for key in labels:
                                if key==label:
                                    labels[key]=str(line).split(' ')[4]
                        if "(macro" in str(line).split(' '):
                            splitLine=str(line).split(' ')
                            print(splitLine)
                            if pp == filePathMxSp:
                                mx_ma=splitLine[len(splitLine)-2]
                                # print(mx_ma)
                            if pp == filePathEEBD:
                                eebd_ma=splitLine[len(splitLine)-2]
                            if pp == filePathFangFr:
                                fangfr_ma=splitLine[len(splitLine)-2]
                            if pp == filePathFrFang:
                                frfang_ma=splitLine[len(splitLine)-2]
                            if pp == filePathDLF:
                                dlf_ma=splitLine[len(splitLine)-2]

                        line = fp.readline()
        else:
            with open(pp) as fp:
                line = fp.readline()
                cnt = 1
                while line:
                    line=" ".join(line.split())
                    # print (str(line))
                    label=str(line).split(' ')[0]
                    if label.startswith('<') :
                        label=label.replace("<",'')
                        label=label.replace(">",'')
                        for key in labels:
                            if key==label:
                                labels[key]=str(line).split(' ')[4]
                    if "(macro" in str(line).split(' '):
                        splitLine=str(line).split(' ')

                        if pp == filePathMxSp:
                            mx_ma=splitLine[len(splitLine)-2]
                            # print(mx_ma)
                        if pp == filePathEEBD:
                            eebd_ma=splitLine[len(splitLine)-2]
                        if pp == filePathFangFr:
                            fangfr_ma=splitLine[len(splitLine)-2]
                        if pp == filePathFrFang:
                            frfang_ma=splitLine[len(splitLine)-2]
                        if pp == filePathDLF:
                            dlf_ma=splitLine[len(splitLine)-2]

                    line = fp.readline()


        if pp == filePathMxSp:
            getlabels(MxSpArray,labels)

        if pp == filePathEEBD:
            getlabels(EEBDArray,labels)

        if pp == filePathFangFr:
            getlabels(FangFrArray,labels)

        if pp == filePathFrFang:
            # if not (arrDictModel == "gramGrp"):
            getlabels(FrFangArray,labels)




        if pp == filePathDLF:
            getlabels(DLFArray,labels)

    #print(FrFangArray)
    MxSp = [float(x) for x in MxSpArray]
    EEBD = [ float(x) for x in EEBDArray ]
    FangFr = [ float(x) for x in FangFrArray ]
    FrFang = [ float(x) for x in FrFangArray ]
    DLF = [ float(x) for x in DLFArray ]

    N = len(modelLabels)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.15       # the width of the bars

    fig = plt.figure()
    fig.set_size_inches(20.5, 10.5,44)
    ax = fig.add_subplot(111)

    #MSD = [10,3,5,7,9,66,78,-1]
    rects1 = ax.bar(ind, MxSp, width, color='lightsalmon')

    #EEBD = [-1, 90, 80]
    rects2 = ax.bar(ind+width, EEBD, width, color='royalblue')


    #FangFrD = [-1, 90, 80]
    rects3 = ax.bar(ind+width*2, FangFr, width, color='khaki')


    #FrFangD = [-1, 90, 80]
    rects4 = ax.bar(ind+width*3, FrFang, width, color='mediumpurple')


    #DLF = [-1, 90, 80]
    rects5 = ax.bar(ind+width*4, DLF, width, color='lightseagreen')


    ax.set_ylabel('F1-Score '+'('+kk+')', size=22)
    ax.tick_params(axis="y", labelsize=22)
    ax.tick_params(axis="x", rotation=30)

    ax.set_xticks(ind+width*2)
    ax.set_xticklabels( (modelLabels) , size=21)
    #ax.legend(( rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], rects6[0]), ('DLF', 'EEBD', 'Basnage','MSD','FaFrD','FrFaD'), loc='center right', bbox_to_anchor=(1.3, 0.5), prop={'size': 18})

    ax.legend(( rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('MxSp ('+mx_ma+')', 'EEBD ('+eebd_ma+')','FangFr ('+fangfr_ma+')','FrFang ('+frfang_ma+')','DLF ('+dlf_ma+')'), loc='center left', bbox_to_anchor=(0.94, 0.4), prop={'size': 18}, title="Macro-average", title_fontsize="19")


    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    autolabel(rects4)
    autolabel(rects5)


    fig.savefig(f'figures/Histogram_{arrDictModel+kk}.png', dpi=100)
    plt.close(fig)

def generate_figure_per_model(model_name):
    for ff in arrFeatures:
        generate_figure_per_feature(model_name,ff)

def getlabels (destination_array, origin_array):
    for d in origin_array:
                destination_array.append(origin_array[d])




for m in arrDictModels:
    generate_figure_per_model(m)


    #plt.show()
