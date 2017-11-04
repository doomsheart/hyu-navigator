import csv
import json
from collections import OrderedDict


# group_data = OrderedDict()
group_data = []
f = open(r"C:\Users\JoonhoWohn\Documents\Dev\hyu-navigator\node_coordinates_add_pro.csv", 'r', encoding= 'UTF-8', newline='')
rdr = csv.reader(f)
for i in rdr:
    info = OrderedDict()
    info["name"] = i[3]
    info['id'] = i[0]
    info['let'] = i[1]
    info['long'] = i[2]
    info['type'] = i[4]
    group_data.append(info)
    # print(i)
print(json.dumps(group_data, ensure_ascii=False, indent="\t"))
# with open('data_file.json', 'w', encoding='utf-8') as make_file:
#     json.dump(group_data, make_file, ensure_ascii=False, indent="\t")
# print(group_data)