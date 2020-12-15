import json

# var = ''
# response= open('meal.json')
# for line in response:
#     var = var + line

# print(var)
# with open('meal.json', 'r') as myfile:
#     response=json.load(myfile.read())

# print(response)
# response_info = json.load(response)
# print(response)


# with open('meal.json', 'r') as f:
#     distros_dict = json.load(f)

# for distro in distros_dict:
#     print(distro['Name']) 


# f = open('meal.json')
# # print(f.read())
# r = f.read()

# # # print(r[0])
# json_file = json.loads(r.decode("utf-8"))

# print(json_file)

with open("meal.json") as json_file:
    data = json.load(json_file)
print(data[:1]) 

