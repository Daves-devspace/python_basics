#dictionary
#list [],tuple(),dictionary {}

student = {"name":"jane sarah","id":1234,"age":21,"gender":"F"}
print(student["gender"])
print(student)

#add
student["weight"]=45
print(student)

#set --only one existence per item,unordered
people = {"jane","Bill","Daudi","Tom"}
print(people)
people.add("Kama")
print(people)
print(len(people))
people.discard('Bill')
print(people)