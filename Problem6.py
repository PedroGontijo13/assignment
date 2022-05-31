#Write a Python function which receives 3 lists as its input parameters
#  and combines the lists and remove repeated numbers from the combined
#  list and return the combined list. For instance, if the input is [1,2,3,4,2,3]
#  and [3,4,6,7] and [-1,0,23,4] the result is [1,2,3,4,6,7,-1,0,23]

def combineListWithNoDublicate(list1,list2,list3):
  combineList = list(set(list1+list2+list3))
  print(str(combineList))

combineListWithNoDublicate([1,2,3,4,2,3],[3,4,6,7],[-1,0,23,4])
