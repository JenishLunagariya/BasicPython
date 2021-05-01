# program compare inputed key with keys in database and answer the value if any,otherwise shows
# wrong key message
def dic(key):
    dic1 = {
        'car': 'tesla',
        'bike': 'ktm',
        'plane': 'honda',
    }
    if key in dic1.keys():
        return dic1[key]
    else:
        return 'key is unavailable in dictionary'

key=str(input('input you key:'))
print(dic(key))