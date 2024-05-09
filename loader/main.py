# import re
# import pandas as pd
# from operator import*
# from pandasgui import show

# from linker_loader import extable




# def addhex(a,b):
#     res = hex(int(a, 16) + int(b, 16))
#     #print(hex(int(res[2:],16)))
#     return hex(int(res[2:],16))  

# def subhex(a,b):
#     res = hex(sub(int(a, 16) ,int(b, 16)))
#     print(res)
#     return res  


# def absolute(string1):
#     df=pd.read_csv(string1,'.')
#     df.columns = ['1', '2' , '3', '4']
#     #df = pd.DataFrame(columns=df_cols)
#     print(df)

#     addresses=[]
#     start =df.iloc[0,2]
#     lenght=df.iloc[0,3]
#     end =addhex(start,lenght)
#     #print(end)
#     #print(start)
#     #print(lenght)
                    
#     sum=start
#             #max1=start+length
#             #min1=start

#             #for i in range (1,len(df)):
#             #   if((df.iloc[i,0]) == 'H' ):
#             #      start = hex(df.iloc[i,2])
#             #     length = hex(df.iloc[i,3])
#                 #    max2=start+length
#                 #   if(max2>max1):
#                 #   max1=max2 
                    
#         # for i in range (1,len(df)):
#             #    if((df.iloc[i,0]) == 'H' ):
#             #       start = hex(df.iloc[i,2])
#             #      min2=start
#             #     if(min2<min1):
#                 #     min1=min2 
#     addresses.append(hex(int(start,16))[2:].zfill(6))               
#     while (hex(int(sum,16)) < hex(int(end,16))):
#         sum=addhex(sum,"10")
#         if(sum[-1] != "0"):
#                 newsum=re.sub(r".$", '0', sum)
#                 sum=newsum
#         #print(sum)
#         addresses.append(sum[2:].zfill(6))

#     #print(addresses)
#     address=pd.DataFrame(addresses)
#     address.columns=['Addresses']
#     address.set_index("Addresses", inplace = True)

#     #address.assign( zero = lambda adresses : address*1 )
#     address['0']='x'
#     address['1']='x'
#     address['2']='x'
#     address['3']='x'
#     address['4']='x'
#     address['5']='x'
#     address['6']='x'
#     address['7']='x'
#     address['8']='x'
#     address['9']='x'
#     address['A']='x'
#     address['B']='x'
#     address['C']='x'
#     address['D']='x'
#     address['E']='x'
#     address['F']='x'
#     #address['0']=address['0'].replace(['5'],'by')
   
    
    
    


#     #address.columns=['0':[''],'1':[''],'2':[''],'3':[''],'4':[''],'5':[''],'6':[''],'7':[''],'8':[''],'9':[''],'A':[''],'B':[''],'C':[''],'D':[''],'E':[''],'F':['']]
    




   
#     addresses1=[]
#     temp=[]
#     lenaddress=[]
#     startoft=[]

#     for i in range (0,len(df)-1):
        
        


#         if((df.iloc[i,0]) == 'T' ):
#             Tstart=df.iloc[i,1]
#             startoft.append(Tstart)
#             Tlenght=df.iloc[i,2]
#             Tend=addhex(Tstart,Tlenght)
#             print(Tend)
#             lenaddress.append(Tend)
#            # line=df.iloc[i,3]
#             #n=2
#             #temp=temp+[line[i:i+n] for i in range(0, len(line), n)]
              

    
#     x=0
#     flag=0
#     print(lenaddress)
#     startoft.append(Tend)
#     print(startoft)
#     print(Tend)
#     #print(subhex(lenaddress[0],startoft[1]))

#     temp1=[]

#     for i in range (0,len(df)):

#         if((df.iloc[i,0]) == 'T' ): #line[9:]

#         #print('flag=0')
#            line=df.iloc[i,3]
#            n=2
#            temp1=[line[i:i+n] for i in range(0, len(line), n)]
#            temp1.insert(0,df.iloc[i,1])
#            column = temp1[0][-1]
#            row = temp1[0][:-1] + "0"
#            print(row + " : " + column) 

#            for i in range(1, len(temp1)):

#             if(int(column, 16) < 15):
#                   address.loc[row, column] = temp1[i]
#                   column = hex(int(column, 16) + 1)[2:].upper()

#             else:
#                   address.loc[row, column] = temp1[i]
#                   column = "0"
#                   row = hex(int(row, 16) + 16)[2:].zfill(6)
            


#     dfff=address.head(10)
#     dfff2=address.tail(10)
    
# #     print(dfff )
# #     dfff2.columns = [''] * len(dfff2.columns)
# #     print(dfff2)
#     print(address)
#     show(address)

# #     line=df.iloc[1,3]
# #     n=2
# #     temp1=[line[i:i+n] for i in range(0, len(line), n)]
# #     temp=temp+temp1  

# #     for i in range (2,len(df)-1):

# #         if((df.iloc[i,0]) == 'T' ):
# #             for i in range (2,len(df)-1):
            
# #                  for v in range(1,len(startoft)):
# #                         if(subhex(startoft[v],lenaddress[v-1]) == hex(int('0',16))):
# #                               print('flag=0')
# #                               line=df.iloc[i,3]

# #                               n=2
# #                               temp1=[line[ii:ii+n] for ii in range(0, len(line), n)]
# #                               temp=temp+temp1
                              
                              
# #                         else:
# #                               print('flag=1')
# #                               #x=hex(int(lenaddress[v-1],16))[2:]
# #                         # print(x)
# #                               #y=hex(int(startoft[v],16))[2:]
# #                               #print(y)
# #                               z=0
                              
# #                               while(hex(int(startoft[v],16))[2:] > hex(int(addhex(hex(int(lenaddress[v-1],16))[2:],str(z)),16))[2:]):      
# #                                           flag=1
# #                                           #x=hex(int(addhex(hex(int(lenaddress[v-1],16))[2:],str(z)),16))

# #                                           #print(hex(int(startoft[v],16))[2:])
# #                                           #print(hex(int(addhex(hex(int(lenaddress[v-1],16))[2:],str(z)),16))[2:])
# #                                           #print('-----------------------------------------------------')
# #                                           temp.append('x')
# #                                           z=z+1
# #                                     #append zero
                              
                              

                          
                         


   
# #    # print(temp)

# #     for i in range (0,len(address)):
            

            
                

# #       for j in range(0,16):
            
# #             if(x<len(temp)):
                  
                  
# #                   if(j==0):
                         
# #                        address.loc[i:i , '0']=temp[x]
# #                        #print(address)
                       
                       
                         
# #                   elif(j==1):
                         
# #                       address.loc[i:i , '1']=temp[x]
# #                       #print(address)
                      
# #                   elif(j==2):
# #                        address.loc[i:i , '2']=temp[x] 
# #                        #print(address)
                       
# #                   elif(j==3):
# #                        address.loc[i: i, '3']=temp[x]
# #                        #print(address)
                       
# #                   elif(j==4):
# #                        address.loc[i:i, '4']=temp[x]
# #                        #print(address)
                       
# #                   elif(j==5):
# #                         address.loc[i:i, '5']=temp[x]
# #                         #print(address)
                        
# #                   elif(j==6):
# #                         address.loc[i:i, '6']=temp[x]
# #                         #print(address)
                        
# #                   elif(j==7):
# #                         address.loc[i:i, '7']=temp[x]
# #                         #print(address)
                        
# #                   elif(j==8):
# #                         address.loc[i:i, '8']=temp[x]
# #                         #print(address)
                        
# #                   elif(j==9):
# #                         address.loc[i:i, '9']=temp[x]
# #                         #print(address)
                        
# #                   elif(j==10):
# #                         address.loc[i:i, 'A']=temp[x]
# #                         #print(address)
                        
# #                   elif(j==11):
# #                        address.loc[i:i, 'B']=temp[x]
# #                        #print(address)
                       
# #                   elif(j==12):
# #                         address.loc[i:i, 'C']=temp[x]
# #                         #print(address)
                        
# #                   elif(j==13):
# #                         address.loc[i:i, 'D']=temp[x]
# #                         #print(address)
                        
# #                   elif(j==14):
# #                         address.loc[i:i, 'E']=temp[x]
# #                         #print(address)
                        
# #                   elif(j==15):
# #                         address.loc[i:i, 'F']=temp[x]
# #                         #print(address) 
# #             x=x+1           
                           
# #             #print("---------------------------------------")
# #             #print(addresses1)
            

# #                    # df.append(df.iloc[[i][j]],[temp[x]],ignore_index=True,)

                    


# #             #    if((df.iloc[i+1,0]) == 'T' ):
# #             #    nxtTstart=hex(df.iloc[i+1,1])
# #             # if(nxtTstart - (Tstart+Tlenght) != 0):
# #                     #add X in memormy
                 
                    
                


# #     #line = '1234567890'
# #     #>>> n = 2
# #     #>>> [line[i:i+n] for i in range(0, len(line), n)]
# #      #print("---------------------------------------")
# #       #print("---------------------------------------")
# #    # address.loc[0:1 , '0']='gg'
# #     #pd.set_option('display.max_row', )
    
# #     print(len(temp))
    
# # ################################################################################################
# # # #########################################################33
# # # #####################################3
# # # 
# # # 
# # #    

    









# def main():
#       #CALLING FUN AND SENDING ARG
#       #absolute('sic.txt')
#      # extable('sicxe.txt') 
   
    
  
# if __name__=="__main__":
#     main()
