# it= iter([1,2,3,])
# print(next(it))
# print(it.__next__())
# print(it.__next__())
# print(next(it))

# it=([1,2,3,4,5])
# print(next(it))
# while True:
#     try:
#         no=next(it)
#         print(no)
#     except StopIteration:
#         break 

# class oddnumber:
#     def __init__(self, end_range):
#         self.start=-1
#         self.end=end_range 

#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start < self.end-1:
#             self.start+=2
#             return self.start 
#         else:
#             raise StopIteration
        
# countiter = oddnumber(10)
# while True:
#     try:

    
#         no = next(countiter)
#         print(no)
#     except StopIteration:
#         break

def count_up_to(max_value):
    current= 1
    while current<=max_value:
        yield current 
        current+=1

counter = count_up_to(10000)
for number in counter:
    print(number)