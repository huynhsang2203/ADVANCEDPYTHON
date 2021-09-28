result = [[1, 2, 3], [4, 5, 6]]
def mystery_function(values):
    for sublist in values:
        result.append([sublist[0]])
    for i in sublist[1:]:
        result[-1].insert(0, i)
        return result
mystery_function(result)