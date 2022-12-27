from dataset import data

filename = input()

# ----- Write your code here -----
def find_file(data, filename):
    id = []
    for i in data:
        if i['is_file'] == True:
            if i['name'] == filename:
                id.append(i['id'])
        else:
            id += find_file(i['children'], filename)
    return id

print(find_file(data, filename))
