datas = []
datas.append([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]])
datas.append([[45, 12],[55,21],[19, -2],[104, 20]])
datas.append([[16, 23],[73,1],[56, 20],[1, -1]])

def openOrSenior(data):
    member_category = []
    for (age, handicap) in data:
        if age >= 55 and handicap > 7:
            member_category.append("Senior")
        else:
            member_category.append("Open")
    return member_category

for data in datas:
    print(openOrSenior(data))

# -----------------------------------------------------------
# 1st try

#def openOrSenior(data):
#    member_category = []
#    for member in data:
#        if member[0] >= 55 and member[1] > 7:
#            member_category.append("Senior")
#        else:
#            member_category.append("Open")
#    return member_category
