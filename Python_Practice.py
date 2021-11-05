#Import CSV
import csv
dir(csv)

counties_dict = {'Arapahoe':422829,'Denver': 463353,'Jefferson': 432438}
county = []
voters = []

print(counties_dict)
counties_dict["Jefferson"] + 1
print(counties_dict)
counties_dict['Alameda'] = 25550
print(counties_dict)
print(len(counties_dict))
items = counties_dict.items()
print(items)

#Retrieve the keys from counties_dict
count_k = counties_dict.keys()

#Appened count_k keys to counties_k list and print to test
county.append(count_k)
print(county)


print("---------------------------------")
voting_data = []


voting_data.append({"county":"El Paso", "registered_voters": 461149})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Arapahoe", "registered_voters": 463353})

print(voting_data)
print(voting_data[0].get("registered_voters"))

for i in range(len(county)):
    print(county[i])

