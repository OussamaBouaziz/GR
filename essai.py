import os
import platform
from pathlib import Path

print("Please type the path to the Dictionary/ies you want to have analyzed ")
urpath = input()

def ask_me(urpath):

    print("Please enter the Path of the dictionary you want to evaluate")
    data_folderEEBD = Path("grobid-dictionaries_data/EEBD/evalWAPITI/eebd/")
    data_folderMxSp = Path("grobid-dictionaries_data/MxSp/evalWAPITI/Mix-Sp/")
    data_folderFangFr = Path("grobid-dictionaries_data/FangFr/evalWAPITI/Fang-Fr/")
    data_folderFrFang = Path("grobid-dictionaries_data/FrFang/evalWAPITI/FrFang/")
    data_folderDLF = Path("grobid-dictionaries_data/DLF/evalWAPITI/DLF/")

    subpaths = [data_folderEEBD, data_folderMxSp, data_folderFangFr, data_folderFrFang, data_folderDLF]

    subpath = ["grobid-dictionaries_data\EEBD\dataset", "grobid-dictionaries_data\MxSp\dataset",
                "grobid-dictionaries_data\FangFr\dataset", "grobid-dictionaries_data\FrFang\dataset",
                "grobid-dictionaries_data\DLF\dataset"]

    dict_dict = {
        "EEBD"  : subpaths[0],
        "MxSp"  : subpaths[1],
        "FangFr": subpaths[2],
        "FrFang": subpaths[3],
        "DLF"   : subpaths[4]
    }

    dict_path = {
        subpath[0]: subpaths[0],
        subpath[1]: subpaths[1],
        subpath[2]: subpaths[2],
        subpath[3]: subpaths[3],
        subpath[4]: subpaths[4]
    }

    eval_path = []

   # print('Platform System', platform.system())
    if platform.system() == 'Windows':
        dictpath = str(urpath).split('\\')
    else:
        dictpath = str(urpath).split('/')
        #print(dictpath)

    if os.path.lexists(urpath) == True:
        eval_path.append(dictpath)
        #print(eval_path)
        #print("+++++")
    else:
        print("The path you entered can not be found by the system. Please try again ! ")
        #print(urpath, "-----")

    n = len(dictpath)
    for i in range(n, -1, -1):

        if dictpath[n - 1] == "grobid-dictionaries_data":
            #or dictpath[n - 2] == "grobid-dictionaries_data".strip("\\"):
            print("You will find the evaluation of all dictionaries in the figures directory")
            # That is an array = problem - you have to modify the type - case (a dictionary might be helpful)
            eval_path = subpaths
            print(eval_path, "<<<<<")
            break

        else:
            if dictpath[i - 1] in dict_dict: #I have to figure out how to get the index from the search in dictionary
                print(dict_dict.get(dict_path[i - 1]))
                eval_path.append(dict_dict.get(dict_path[i - 1]))
                #print(type(dict_dict[dictpath[i - 1]]))
                #print(eval_path)
                break

            else:
                print("Write a whole Path to a dictionary !!!")
                break
    #print("Directory of the dictionary you want to evalute is :", eval_path )

    return eval_path

eval_path = ask_me(urpath)
print(eval_path)