#cau A
rat_1 = [1,2,3,4,5,6,7,8,9,10]
rat_2 = [10,9,8,7,6,5,4,3,2,1]

if rat_1[0] > rat_2[0]:
  print("Rat 1 weighed more than rat 2 on day 1.")
else:
  print("Rat 1 weighed less than rat 2 on day 1.")
#cau B

if rat_1[0] > rat_2[0] and rat_1[-1] > rat_2[-1]:
  print("Rat 1 remained heavier than Rat 2.")
else:
  print("Rat 2 became heavier than Rat 1.")
#cau C

if rat_1[0] > rat_2[0]:
  if rat_1[-1] > rat_2[-1]:
    print("Rat 1 remained heavier than Rat 2.")
  else:
    print("Rat 2 became heavier than Rat 1.")
else:
    print("Rat 2 became heavier than Rat 1.")