str = input()
new_str = ''
new_item = ''

for item in str:
    if item == item.upper():
        new_item = item.lower()
    else:
        new_item = item.upper()
    
    new_str += new_item

print(new_str)