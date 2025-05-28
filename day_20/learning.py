# import copy 
# l1=[[1,2,3],[1,3,4],[7,8,7]]
# shallow_copied_l1= copy.copy(l1)

# shallow_copied_l1[0][0]=100

# print("original list:", l1)
# print("shallow copied list:", shallow_copied_l1)

#dictionary
# d1={"name":"ram", "age":18, "gender":"male"}
# print(d1.name())

# a={"fruit":["mango","banana"], "flower":["rose","lotus"]}
# b={('india,usa'):'countires', ('new delhi, new york'):'capital'}
# print(a)
# print(b)
# d1={"banana":"fruit", "rose":"flower","mango":"fruit"}
# d2={"fruit":"banana", "flower":"rose", "fruit":"mango"}
# print(d1)
# print(d2)

#another method to define dictionary
# sport_player={
#     "name":"Sachin ",
#     "age":34,
#     "sport":"cricket"
# }
# print(sport_player)
# student_info=dict(name="alice", age=32, major="computer science")
# print(student_info)

# student_info={
#     "name":"alice",
#     "age":21,
#     "major":"computer science"
# }

# name=student_info["name"]
# print("name:", name)

# age= student_info.get("age") #accessing age
# print("age:",age)

#modification of list
# student_info={
#     "name":"alice",
#     "age":21,
#     "major":"computer science"
# }

# student_info["age"]=34


# student_info["graduation_year"]= 2023
# print("the medified dictionary is:", student_info)

#iterating dictionary
# student_info={
#     "name":"alice",
#     "age":21,
#     "major":"computer science"
# }

# for key in student_info:
#     print("key:",key, student_info[key])

# for value in student_info.keys():
#     print("values",value)
# for key, value in student_info.items():
#     print("key:value", key, value )

# seq= ("name", "age", "sex")
# dict= dict.fromkeys(seq)

# value= 10 
# dict= dict.fromkeys(seq, value )
# print("new dictionary: %s" % str(dict))

# the_key={"b",'c','d'}
# value=[5]
# constan=dict.fromkeys(the_key, value )
# print(constan)

animal= "lion"
value= 'king'
print(value)
d=dict.fromkeys(animal, value)
print(d)
print(type(str(d)))

print(len(d))
# p=[1,2,3]
# dict.setdefault(p,defult="we") #need to be explore