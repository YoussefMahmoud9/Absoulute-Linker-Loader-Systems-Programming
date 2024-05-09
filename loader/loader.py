import re
import pandas as pd
from operator import *
from pandasgui import show
import numpy as np


def addhex(a, b):
    res = hex(add(int(a, 16), int(b, 16)))
    ###print(hex(int(res[2:],16)))
    return hex(int(res[2:], 16))[2:].zfill(6).upper()


def subhex(a, b):
    print("here2", a, b)
    res = hex(sub(int(a, 16), int(b, 16)))
    ##print(res)
    return res


def unique(list1):

    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def funrow(row, start):
    index = subhex(row, start)
    index = int(index, 16) / 16
    return int(index)


def absolute(string1):
    df = pd.read_csv(string1, ".")
    df.columns = ["1", "2", "3", "4"]
    # df = pd.DataFrame(columns=df_cols)
    print(df)

    addresses = []
    start = df.iloc[0, 2]
    lenght = df.iloc[0, 3]
    end = addhex(start, lenght)
    # print(end)
    # print(start)
    # print(lenght)

    sum = start
    # max1=start+length
    # min1=start

    # for i in range (1,len(df)):
    #   if((df.iloc[i,0]) == 'H' ):
    #      start = hex(df.iloc[i,2])
    #     length = hex(df.iloc[i,3])
    #    max2=start+length
    #   if(max2>max1):
    #   max1=max2

    # for i in range (1,len(df)):
    #    if((df.iloc[i,0]) == 'H' ):
    #       start = hex(df.iloc[i,2])
    #      min2=start
    #     if(min2<min1):
    #     min1=min2
    addresses.append(hex(int(start, 16))[2:].zfill(6))
    while hex(int(sum, 16)) < hex(int(end, 16)):
        sum = addhex(sum, "10")
        if sum[-1] != "0":
            newsum = re.sub(r".$", "0", sum)
            sum = newsum
        # print(sum)
        addresses.append(sum[2:].zfill(6))

    # print(addresses)
    address = pd.DataFrame(addresses)
    address.columns = ["Addresses"]
    address.set_index("Addresses", inplace = True)

    # address.assign( zero = lambda adresses : address*1 )
    address["0"] = "x"
    address["1"] = "x"
    address["2"] = "x"
    address["3"] = "x"
    address["4"] = "x"
    address["5"] = "x"
    address["6"] = "x"
    address["7"] = "x"
    address["8"] = "x"
    address["9"] = "x"
    address["A"] = "x"
    address["B"] = "x"
    address["C"] = "x"
    address["D"] = "x"
    address["E"] = "x"
    address["F"] = "x"
    # address['0']=address['0'].replace(['5'],'by')

    # address.columns=['0':[''],'1':[''],'2':[''],'3':[''],'4':[''],'5':[''],'6':[''],'7':[''],'8':[''],'9':[''],'A':[''],'B':[''],'C':[''],'D':[''],'E':[''],'F':['']]

    addresses1 = []
    temp = []
    lenaddress = []
    startoft = []

    for i in range(0, len(df) - 1):

        if (df.iloc[i, 0]) == "T":
            Tstart = df.iloc[i, 1]
            startoft.append(Tstart)
            Tlenght = df.iloc[i, 2]
            Tend = addhex(Tstart, Tlenght)
            print(Tend)
            lenaddress.append(Tend)
        # line=df.iloc[i,3]
        # n=2
        # temp=temp+[line[i:i+n] for i in range(0, len(line), n)]

    x = 0
    flag = 0
    print(lenaddress)
    startoft.append(Tend)
    print(startoft)
    print(Tend)
    # print(subhex(lenaddress[0],startoft[1]))

    temp1 = []

    for i in range(0, len(df)):

        if (df.iloc[i, 0]) == "T":  # line[9:]

            # print('flag=0')
            line = df.iloc[i, 3]
            n = 2
            temp1 = [line[i : i + n] for i in range(0, len(line), n)]
            temp1.insert(0, df.iloc[i, 1])
            column = temp1[0][-1]
            row = temp1[0][:-1] + "0"
            print(row + " : " + column)

            for i in range(1, len(temp1)):

                if int(column, 16) < 15:
                    address.loc[row, column] = temp1[i]
                    column = hex(int(column, 16) + 1)[2:].upper()

                else:
                    address.loc[row, column] = temp1[i]
                    column = "0"
                    row = hex(int(row, 16) + 16)[2:].zfill(6)

    dfff = address.head(10)
    dfff2 = address.tail(10)

    #     print(dfff )
    #     dfff2.columns = [''] * len(dfff2.columns)
    #     print(dfff2)
    print(address)
    show(address)


def extable(string1):
    list = []

    var = open(string1, "r")
    for x in var:
        list += [x.split("^")]

        ###print(x)
    df = pd.read_csv(string1, "^")
    ###print(list)

    prog = []
    name = []
    lenght = []
    Laddress = []
    flag = 0
    extable = []
    start = "403F"

    for i in range(0, len(list)):
        if list[i][0] == "H":
            extable += [[list[i][1], start, list[i][3][:-1]]]
            start = addhex(start, list[i][3][:-1])

        if list[i][0] == "D":
            j = 1
            while j < len(list[i]):
                if list[i][j + 1][-1] == "\n":
                    extable += [[list[i][j], list[i][j + 1][:-1]]]
                else:
                    extable += [[list[i][j], list[i][j + 1]]]
                j = j + 2

    # ##print(extable)

    exttable = pd.DataFrame()
    exttable["CSET"] = "X"
    exttable["SYMBOL_NAME"] = "X"
    exttable["ADDERS"] = "X"
    exttable["LENGHT"] = "X"
    for i in range(len(extable)):
        if len(extable[i]) == 3:
            exttable.loc[i, "CSET"] = extable[i][0]
            exttable.loc[i, "ADDERS"] = extable[i][1]
            exttable.loc[i, "LENGHT"] = extable[i][2]
        else:
            exttable.loc[i, "SYMBOL_NAME"] = extable[i][0]
            exttable.loc[i, "ADDERS"] = extable[i][1]

    exttable.fillna("X")
    ##print(exttable)
    exttable.to_csv("Ext_sym_Table.txt", "\t", index=False)
    marks_list = exttable["ADDERS"].tolist()

    # show the list
    ##print(marks_list)

    start1 = exttable.iloc[0, 2]
    start2 = re.sub(r".$", "0", start1)
    ###print(start)
    #    df1=pd.DataFrame(list)
    #   ##print(df1)

    df1 = pd.read_csv(string1, "^")
    df1.columns = ["1", "2", "3", "4", "5"]
    progname = ""
    Hname = []

    for i in range(len(df1)):
        if (df1.iloc[i, 0]) == "H":
            progname = df1.iloc[i, 1]
            Hname.append(progname)

    ##print(progname)
    ##print(Hname)
    counter = 0
    Listname = []

    for i in range(1, len(Hname)):
        for x in range(1, len(df1)):
            if df1.iloc[x, 1] == Hname[i]:
                y = x + 3
                while df1.iloc[y, 0] == "T":
                    counter = counter + 1
                    y = y + 1
                if counter == 1:
                    Listname.append(Hname[i])
                else:
                    for z in range(0, counter - 1):
                        Listname.append(Hname[i])
    ##print(Listname)
    liststart = []
    ##print(len(exttable))

    for i in range(0, len(Listname)):
        ##print(Listname[i])
        for x in range(0, len(exttable)):

            if Listname[i] == exttable.iloc[x, 0]:
                liststart.append(exttable.iloc[x, 2])

    ##print(liststart)

    for i in range(len(exttable)):
        if exttable.iloc[i, 0] == progname:
            end = addhex(exttable.iloc[i, 2], exttable.iloc[i, 3])
    exttable.fillna("x")
    ###print(end)
    addresses = []
    sum = start2
    ##print(liststart)

    addresses.append(hex(int(start2, 16))[2:].zfill(6))
    while hex(int(sum, 16)) < hex(int(end, 16)):
        sum = addhex(sum, "10")
        if sum[-1] != "0":
            newsum = re.sub(r".$", "0", sum)
            sum = newsum
        ###print(sum)
        addresses.append(sum[2:].zfill(6))

    ###print(addresses)
    address = pd.DataFrame(addresses)
    address.columns = ["Addresses"]
    address.set_index("Addresses", inplace=True)
    address["0"] = "x"
    address["1"] = "x"
    address["2"] = "x"
    address["3"] = "x"
    address["4"] = "x"
    address["5"] = "x"
    address["6"] = "x"
    address["7"] = "x"
    address["8"] = "x"
    address["9"] = "x"
    address["A"] = "x"
    address["B"] = "x"
    address["C"] = "x"
    address["D"] = "x"
    address["E"] = "x"
    address["F"] = "x"
    ###print(address)
    temp1 = []
    flag = 0
    y = 0
    ytest = 0

    source = open("sicxe.txt", "r")
    lines = source.read()
    for line in lines:
        if line[0] == "T":
            ytest = ytest + 1
        if line[0] == "E":
            break
    ##print("ytest =" + str(ytest))

    x = 0
    for i in range(0, len(df1)):

        if (df1.iloc[i, 0]) == "T":  # line[9:]

            ###print('flag=0')
            line = df1.iloc[i, 3]
            n = 2
            temp1 = [line[i : i + n] for i in range(0, len(line), n)]
            temp1.insert(0, df1.iloc[i, 1])
            if y < 2:
                temp1[0] = addhex(temp1[0], start1)  #
                y = y + 1

            else:

                # print(temp1[0])
                # print(liststart[x])
                temp1[0] = addhex(temp1[0], liststart[x])
                x = x + 1  #

            column = temp1[0][-1]
            row = temp1[0][:-1] + "0"
            ###print(row + " : " + column)
            print(temp1)

        for i in range(1, len(temp1)):

            if int(column, 16) < 15:
                address.loc[row, column] = temp1[i]
                column = hex(int(column, 16) + 1)[2:].upper()

            else:
                address.loc[row, column] = temp1[i]
                column = "0"
                row = hex(int(row, 16) + 16)[2:].zfill(6).upper()

    liststart.insert(0, start1)
    print(Hname)

    Mstartadress = unique(liststart)
    print(Mstartadress)
    # print(df1)
    y = 0
    for i in range(len(df1)):

        if df1.iloc[i, 0] == "M":
            print(df1.iloc[i, 1])
            new = addhex(df1.iloc[i, 1], Mstartadress[y])
            print(new)
            df1.loc[i:i, "2"] = new

        elif df1.iloc[i, 0] == "E":
            y = y + 1
    symtable = {}
    src = open("Ext_sym_Table.txt", "r")
    lines = src.read()
    # for line in lines :
    #     temp=line.strip().split('\t')
    #     print(temp)

    symtable = pd.read_csv("Ext_sym_Table.txt", "\t")
    symtable = symtable[["CSET", "SYMBOL_NAME", "ADDERS"]] = symtable[
        ["CSET", "SYMBOL_NAME", "ADDERS"]
    ].fillna("x")

    symtable["new"] = (
        symtable["CSET"].astype(str)
        + " "
        + symtable["SYMBOL_NAME"].astype(str)
        + " "
        + symtable["ADDERS"]
    )
    symtable["new"]

    print(symtable["new"])

    start3 = start1[0 : len(start1) - 1] + "0"

    print(start3)

    print(df1)
    print(symtable)
    print(address)

    for i in range(len(df1)):
        if df1.iloc[i, 0] == "M":
            newadd = df1.iloc[i, 1]
            column = newadd[-1]
            row = newadd[:-1] + "0"
            oldrow = row
            oldcol = column
            # print(row + " : " + column)
            bits = ""

            row1 = funrow(row, start3)

            for x in range(3):
                # print(column)
                # print(row1)
                # colcopy = column
                colcopy = address.columns.get_loc(column[-1])
                # print("test : " + address.iloc[int(row1), int(column)])
                bits += address.iloc[int(row1), int(colcopy)]
                # print("---")
                # print(bits)

                column = addhex(str(column), "1")
                if column == "15":
                    column = "0"
                    row = addhex(str(row), "10")
            sameaddress = "0"
            for z in range(len(symtable)):
                if df1.iloc[i, 2][3:] == symtable.iloc[z, 0].split()[0:][0]:
                    sameaddress = symtable.iloc[z, 2]

                    # print("same address before")
                    # print(sameaddress)
                    # print( df1.iloc[i,2][3:])
                    # print(symtable.iloc[z,0].split()[0:][0])
                elif df1.iloc[i, 2][3:] == symtable.iloc[z, 1].split()[0:][0]:
                    sameaddress = symtable.iloc[z, 2]
                    # print("same address after")
                    # print(sameaddress)
                    # print( df1.iloc[i,2][3:])
                    # print(symtable.iloc[z,1].split()[0:][0])
            # print('op sign')
            # print(df1.iloc[i,2][2])

            if df1.iloc[i, 2][1] == "5":
                char1 = bits[0]
                bits = bits[1:]

                if df1.iloc[i, 2][2] == "+":
                    # print(" addr" + sameaddress)
                    bits = addhex(bits, sameaddress)

                elif df1.iloc[i, 2][2] == "-":
                    bits = subhex(bits, sameaddress)

                bits = bits[-5:]
                bits = char1 + bits
                # print("after modification" + bits)
            else:
                if df1.iloc[i, 2][2] == "+":
                    bits = addhex(bits, sameaddress)

                elif df1.iloc[i, 2][2] == "-":
                    bits = subhex(bits, sameaddress)
                # print("after modification" + bits)

            line = bits
            n = 2
            bits1 = [line[i : i + n] for i in range(0, len(line), n)]

            temp4 = 0
            print(bits1)

            column = column[5]
            # print(column)
            row1 = funrow(oldrow, start3)
            for i in range(3):
                # print(oldrow + " : " + oldcol)

                if int(oldcol, 16) < 15:
                    address.iloc[int(row1), int(oldcol, 16)] = bits1[i]
                    oldcol = hex(int(oldcol, 16) + 1)[2:].upper()

                else:
                    address.iloc[int(row1), int(oldcol, 16)] = bits1[i]
                    oldcol = "0"
                    row1 = row1 + 1
                temp4 = temp4 + 2

    print(bits)

    # dfff = address.head(10)
    # dfff2 = address.tail(10)
    print(address)
    show(address)

    # print(dfff )


#     dfff2.columns = [''] * len(dfff2.columns)
# print(dfff2)


# address.set_index('Addresses')
# print(address[address['Addresses']=='4020'].index.values)
# print(address.iloc['4020'.index,0])


#  if(flag == 0):
#     flag=1
#     Laddress.append(start)
#  else:
#      newstart=addhex(df.iloc[i,3]+start)
#      start=newstart
#      Laddress.append(newstart)

#####################################################################################3
def Loader(string1):
    list = []

    var = open(string1, "r")
    for x in var:
        list += [x.split("^")]

        ###print(x)
    # df=pd.read_csv(string1,'^')
    ##print(list)
    df = pd.DataFrame(list)

    ###print(df)

    addresses = []
    start = df.iloc[0, 2]
    lenght = df.iloc[0, 3]
    end = addhex(start, lenght)
    ###print(end)
    ###print(start)
    ###print(lenght)

    sum = start

    addresses.append(hex(int(start, 16))[2:].zfill(6))
    while hex(int(sum, 16)) < hex(int(end, 16)):
        sum = addhex(sum, "10")
        if sum[-1] != "0":
            newsum = re.sub(r".$", "0", sum)
            sum = newsum
        ###print(sum)
        addresses.append(sum[2:].zfill(6))

    ###print(addresses)
    address = pd.DataFrame(addresses)
    address.columns = ["Addresses"]
    address.set_index("Addresses", inplace=True)

    # address.assign( zero = lambda adresses : address*1 )
    address["0"] = "x"
    address["1"] = "x"
    address["2"] = "x"
    address["3"] = "x"
    address["4"] = "x"
    address["5"] = "x"
    address["6"] = "x"
    address["7"] = "x"
    address["8"] = "x"
    address["9"] = "x"
    address["A"] = "x"
    address["B"] = "x"
    address["C"] = "x"
    address["D"] = "x"
    address["E"] = "x"
    address["F"] = "x"
    # address['0']=address['0'].replace(['5'],'by')

    # address.columns=['0':[''],'1':[''],'2':[''],'3':[''],'4':[''],'5':[''],'6':[''],'7':[''],'8':[''],'9':[''],'A':[''],'B':[''],'C':[''],'D':[''],'E':[''],'F':['']]

    addresses1 = []
    temp = []
    lenaddress = []
    startoft = []

    for i in range(0, len(df) - 1):

        if (df.iloc[i, 0]) == "T":
            Tstart = df.iloc[i, 1]
            startoft.append(Tstart)
            Tlenght = df.iloc[i, 2]
            Tend = addhex(Tstart, Tlenght)
            # ##print(Tend)
            lenaddress.append(Tend)
        # line=df.iloc[i,3]
        # n=2
        # temp=temp+[line[i:i+n] for i in range(0, len(line), n)]

    x = 0
    flag = 0
    ###print(lenaddress)
    startoft.append(Tend)
    ###print(startoft)
    ###print(Tend)
    ###print(subhex(lenaddress[0],startoft[1]))

    temp1 = []

    for i in range(0, len(df)):

        if (df.iloc[i, 0]) == "T":  # line[9:]

            ###print('flag=0')
            line = df.iloc[i, 3]
            n = 2
            temp1 = [line[i : i + n] for i in range(0, len(line), n)]
            temp1.insert(0, df.iloc[i, 1])
            column = temp1[0][-1]
            row = temp1[0][:-1] + "0"
            ###print(row + " : " + column)

            for i in range(1, len(temp1)):

                if int(column, 16) < 15:
                    address.loc[row, column] = temp1[i]
                    column = hex(int(column, 16) + 1)[2:].upper()

                else:
                    address.loc[row, column] = temp1[i]
                    column = "0"
                    row = hex(int(row, 16) + 16)[2:].zfill(6)


def main():
    # CALLING FUN AND SENDING ARG

    program = input("Press 1 for SIC, or press 2 for SICXE: ")
    if program == "1":
        absolute("sic.txt")
    elif program == "2":
        extable("sicxe.txt")
    else:
        print("There was an error with your selection, please try again")
    #   absolute('sic.txt')
    #   extable('sicxe.txt')
    # Loader('sicxe.txt')


if __name__ == "__main__":
    main()
