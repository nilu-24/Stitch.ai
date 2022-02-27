

# hashmap stores condtion : names

first = {
    "A" : "Junaid",
    "B" : "Junaid",
    "C" : "Junaid"
}

second = {
    "A" : "Fardin",
    "C" : "Fardin",
    "L" : "Fardin"
}

third = {
    "M" : "Alauddin",
    "N" : "Alauddin",
    "C" : "Alauddin"
}


all_maps = [first,second,third] #storing the hashmaps in an array

common_users = []

for i in range(len(all_maps)):
    for key in first: #first is the main users hashtable
        if key in all_maps[i]:
            common_users.append(list(all_maps[i].items())[0][1])

common_users = list(set(common_users))

common_users.remove("Junaid")

print(common_users)




