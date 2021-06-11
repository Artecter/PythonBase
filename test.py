data = ["Раз", "Два", "Три"]
print(data)
s = ','.join(data)
print(s)
filename = "test.csv"

with open(filename, 'w', encoding='utf-8') as file:
    for i in data:
        file.write(str(i))
