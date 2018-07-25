import os

file = open('./utf8-ZhuYin.map', 'r', encoding='utf8', newline='')
output = open('./ZhuYin-utf8.map', 'w', encoding='utf8', newline='')
zhuyin = "ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ"
index = [[] for _ in range(37)]
for line in file:
    content = line.split(' ')
    exist = [0 for _ in range(37)]
    for z in content[1].split('/'):
        exist[zhuyin.find(z[0])] = 1
    for i in range(37):
        if exist[i] == 1:
            index[i].append(content[0])

for i in range(37):
    indexstr = ""
    for z in index[i]:
        indexstr += z + " "
    output.write("{:s} {:s}\n".format(zhuyin[i], indexstr[:-1]))
    for z in index[i]:
        output.write("{:s} {:s}\n".format(z, z))
