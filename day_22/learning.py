# fo= open("happy.txt","wb")
# print("name of the file:", fo.name)

# fid=fo.fileno()
# print("file discriptor:", fid)
# print(fo.tell())
# fo.close()

# #converting into json
# import json 
# data= {"name":"alice", "age":30, "city":"kathmandu"}
# json_string=json.dumps(data)
# print(json_string)

#desirializing json
import json 
json_string={"name":"Tenji","age":30,}
python_obj=json.loads(json_string)
print(python_obj)

import json 
with open("data.json", "r"):

