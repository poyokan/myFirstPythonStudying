"""
python3
Kazuma Matsunaga
2021-10-14
"""

import numpy as np
import pandas as pd
import os

def ope_1time(ndarray_odd) :
    """return ndarray"""
    array_1time = 3*ndarray_odd + 1

    array1 = np.where(array_1time % 2 == 0, array_1time/2, array_1time)

    while np.all(array1 % 2 == 1) == False :
        array1 = np.where(array1 % 2 == 0, array1/2, array1)
    return array1

def make_df(array_odd):
    """return DataFrame"""
    return pd.DataFrame(np.vstack([array_odd,ope_1time(array_odd)]).T)

def save_df_to_excel(df):
    print("Excelファイルに保存します")
    filename = input("ファイル名入力(拡張子無しで。)\n>>") + ".xlsx"

    if os.path.isfile(filename) == True:

        anser = input("同じファイル名が存在してますね。上書きしますか?(y/n)\n>>")

        if anser == "y":
            df.to_excel(filename,index=False,header=["操作前","操作後"])
            print("Excelファイルを作りました")
        
        else :
            pass
    
    else :
        df.to_excel(filename,index=False,header=["操作前","操作後"])
        print("Excelファイルを作りました")



def test():

    arr1 = np.arange(1,10,2)
    print("arr1:",arr1)

    arr2 = ope_1time(arr1)
    print("arr2:",arr2)

    return_array = np.vstack([arr1,arr2]).T
    print(return_array)

    df = pd.DataFrame(return_array)
    print(df)

    filename = input("filename?\n>>") + ".xlsx"
    df.to_excel(filename,index=False,header=False)


def main():

    array = np.arange(1,10002,2)

    df = make_df(array)

    save_df_to_excel(df)

    print("end")



if __name__ =="__main__":

    #test()
    main()