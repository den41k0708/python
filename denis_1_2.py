import re
text = 'asd, rdf fsduh: asd, fs rdf'

def split_text(text):
    words = re.findall(r"[\w']+", text)
    return words

def delete_same(words):
    new_list = []
    for item in set(words):
        new_list.append(item)
    return new_list

list = split_text(text)
print(list)
new_list = delete_same(list)
print(new_list)