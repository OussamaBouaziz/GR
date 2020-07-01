arrPaths= ['data_folderEEBD', 'data_folderMxSp, data_folderFangFr',' data_folderFrFang', 'data_folderDLF']

def sieb(arrPaths):
    Table= ["EEBD","MxSp","FangFr","FrFang","DLF"]
    Paths= ["grobid-dictionaries_data/EEBD/evalWAPITI/eebd/","grobid-dictionaries_data/MxSp/evalWAPITI/Mix-Sp/","grobid-dictionaries_data/FangFr/evalWAPITI/Fang-Fr/","grobid-dictionaries_data/FrFang/evalWAPITI/FrFang/","grobid-dictionaries_data/DLF/evalWAPITI/DLF/"]
    print(Table)
    print("Combien de dictionnaires des 5 voulez-vous analyser?")
    n =int(input())
    if (n <5):
        print("Quels dictionnaires voulez-vous analyser ?")
        Antab=[]
        sarrPaths=[]
        for i in range(n):
            j=int(input())
            Antab.append(Table[j-1])
            sarrPaths.append(Paths[j-1])
        print("les dictionnaires qui seront analysés sont: ", Antab)
    elif n==5:  
        print("les dictionnaires qui seront analysés sont: ", Table)
        sarrPaths=Paths
    print(sarrPaths)
    return sarrPaths        

tab = sieb(arrPaths)
