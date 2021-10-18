def least(dic):
  min = 999999999
  for key, value in dic.items():
    if value < min:
      min = value
      str1 = key
    else:
      continue
  for key, value in dic.items():
    if key == str1:
      print(key)
nguyentu = {'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.80}
print(least(nguyentu))