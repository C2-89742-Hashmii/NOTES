#############################################################################################

# tup1=(1,2,3,4)
# tup2=(8)
# print(f"The Type of tup is :{type(tup1)}")
# print(f"The Type of tup is :{type(tup2)}")
#list 

# def fun1():
#     num=[1,20,30,40,0]
#     print(num)
#     for item in num:
#         print(item ,end=" ")
    
# fun1()

############################################ While Loop For list###################################

# list=[]
# flag=True

# while flag==True:
#     a=input()
#     if a=='y':
#         flag=False
#     else:
#         list.append(a)
# print(list)


###############################################lambda#############################################


# a=lambda n:n*2
# print(a(8))

#############################################################################################

# a=(input())
# list=a.split(",")
# print(list)

################################################     MAP     #############################################
# list1=[1,2,3,4,5]
# result=list(map(lambda n:n*2,list1))
# print(result)
 
##################################################   tuple unpacking   ########################################################


# tup = 10, 200,300 ,400
# *n1,b2, n3=10, 200,300 ,400
# n1.append(30)
# print(n1)
# # print(n2)
# # print(n3)
# print(type(n1))
################# SQAURED ELEMENT OF LIST BY MAP METHOD##########################



# list1=[1,2,3,4,5]
# result=list(map(lambda n:n**2,list1))
# print(f"list={list1}")
# print (f"Squared list is :{result}")



################################################   TEMP FRON C TO F BY MAP ################################################


# def fun1():
#     #temp in celcius
#     temp=[29,28,38,52,35]
#     #cnvrt in farthnt
#     res=list(map(lambda t : 32+ (t*(9/5)),temp))
#     print(res)

# fun1()
#####################################################     FILTER      #################################################################


# num=[1,2,3,4,5,6,8]
# res=list(filter(lambda n: n%2==0 , num))
# print(res)

#####################################################    CUBE OF ODD IN LIST BY FILTER      #################################################################

# nums=[ 1,2,3,4,5,6,7,]   # always excute the filter first 
# even=(filter(lambda n : n%2!=0,nums))
# Res= list(map(lambda n : n**3 , even))
# print(Res)



##################################################### LIST COMPRIHENTION   ################################################################

# nums=[ 1,2,3,4,5,6,7,]

# square=[number **2 for number in nums]
# print(square)
##################################################### LIST COMPRIHENTION   ##############################################################   
# nums=[ 1,2,3,4,5,6,7,]

# square=[number **3 for number in nums]
# print(square)

##################################################### LIST COMPRIHENTION   ##############################################################

