file = open('document.txt', encoding='utf8')

sent = file.read()

noPeriods = sent.replace(".", "")
sent_list = noPeriods.split()

lone = []
for i in sent_list:
    if i not in lone:
        lone.append(i)

lone.sort()

val = []
for j in range(len(lone)):
    val.append(sent_list.count(lone[j]))

dict_sent = {}
for k in range(len(lone)):
    dict_sent [lone[k]] = val[k]

dict_sort = sorted(dict_sent, key=dict_sent.get, reverse=True)[:5]

print("\r")
for l in range(len(dict_sort)):
    print(str(dict_sort[l]) + ": " + str(dict_sent[dict_sort[l]]))