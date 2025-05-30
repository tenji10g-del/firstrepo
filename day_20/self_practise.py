# #accessing element in dictionary
# Farmer= {"name":"Raju","age":23,"country":"NEPAL "}
# name=Farmer["name"]
# print(name)

# country=Farmer.get("country")
# print(country)

# #modifying dictionary
# student={"name":"Ritik",  "class":8, "gender":"male"}

# print("original dictonary:",student)
# student["class"]=9
# student["address"]="Kathmandu"
# print("modified dictionary:",student)

# #removing element from dictionary 
# Farmer= {"name":"Raju","age":23,"country":"NEPAL "}
# Farmer.pop("name")
# print(Farmer)

#methods in dictionary
# Farmer= {"name":"Raju","age":23,"country":"NEPAL "}
# Farmer.clear()
# print(Farmer)

Farmer={1:"nima", 2:"ram", 3:"sita"}
Farmer[1]="Dawa"
farmer_shallow_copy= Farmer.copy()
print("shallow copy before editing:",farmer_shallow_copy)
farmer_shallow_copy[5]="pukar"
print("Shallow copy ager editing:", farmer_shallow_copy)

