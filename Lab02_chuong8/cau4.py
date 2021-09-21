ids = [4353, 2314, 2956, 3382, 9362, 3900]
def list_ids():
    print(ids)
print('DS: ',ids)
# cau A
print('Câu A')
ids.remove(3382)
list_ids()
# cau B
print('Câu B')
ids.index(9362)
list_ids()
# cau C
print('Câu C')
ids.insert(ids.index(9362) + 1, 4499)
list_ids()
# cau D
print('Câu D')
ids = ids + [5566, 1830]
list_ids()