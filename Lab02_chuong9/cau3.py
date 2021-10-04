whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
more_whales = []
for item in whales:
 more_whales.append(item + 1)
print(more_whales)
#cach 2
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
for index, value in enumerate(whales):
 whales[index] = value+1
print(whales)