list1=[{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '5a', 'scores': [4,4,4,5,2]},
{'school_class': '6a', 'scores': [5,4,4,5,2]},
{'school_class': '7a', 'scores': [6,4,4,5,2]},
{'school_class': '8a', 'scores': [7,4,4,5,2]},
{'school_class': '9a', 'scores': [8,4,4,5,2]}
]

#print(list1[1])
#print(list1[2]['scores'])

total = []
for score in list1:
    total += score['scores'] #total = total + score['scores']

print(total)
print('Средний балл по всей школе: ', sum(total) / len(total))

for score in list1:
    print(score['school_class'], ':', sum(score['scores']) / len(score['scores']))
    