D = dict()
#open file
name = raw_input("Enter file name")
if len(name) < 1 : name = 'lyrics.txt'
hand = open(name)
hand = hand.read()
listy2 = list()
#Label word occurances
hand = hand.split()
for i in hand:
    D[i] = D.get(i, 0) + 1
#sort and print
for k, v in D.items():
    listy2.append((v, k))
listy2.sort(reverse=True)
print("Top 5 most common words are")
for k, v in listy2[:4]:
    print(v)