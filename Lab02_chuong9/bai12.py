num_list=[1, 2, 3, -3, 6, -1, -3, 1]
def remove_neg(num_list):
  index = 0
  while index < len(num_list):
    if num_list[index] < 0:
      del num_list[index]
    else:
      index += 1
print(remove_neg(num_list))