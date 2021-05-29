s = [10, 12, 20]
f = [20, 19, 30]

map_f = {}
map_s = {}
for i in range(len(f)):
   map_f[i] = f[i]

for i in range(len(s)):
   map_s[i] = s[i]

# print(map_f)
sorted_f = []
new_s = []
for k,v in sorted(map_f.items(), key=lambda x:x[1]):
    sorted_f.append(v)
    new_s.append(map_s[k])

print(new_s,'\n',sorted_f)