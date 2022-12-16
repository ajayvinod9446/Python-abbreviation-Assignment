import re
import sys

# CODE FOR CLEANING START step 1
myfile = open('trees.txt', 'r')

newfile = open('newTreeList.txt', 'w')
for line in myfile:
    string_without_apostrophe = line.replace("'", "")
    test_string = re.sub(r"[^a-zA-Z]+", ' ', string_without_apostrophe)
    newfile.write(test_string + '\n')
newfile.close()
# END

# CODE FOR CREATE LIST FORMAT OF VALUE.TXT FILE step 2
value = open('values.txt', 'r')
newvalues = dict()
for line in value:
    values = line.split()
    key = values[0]
    pair = values[1]
    if key not in newvalues:
        newvalues[key] = []
    newvalues[key] = pair
# END

# CODE FOR CREATING PERMUTATIONS step 3
trees = open('newTreeList.txt', 'r')
tree_list = list()
for x in trees:
    tree_list.append(x.replace("\n", ""))
import itertools

permutationList = dict()


def createPermutation(word):
    permutationList[word] = []
    perm = list(itertools.permutations(word, 3))
    for i in perm:
        per = ''.join(i)
        per_new = per.replace(" ", "")
        permutationList[word].append(per_new)


for i in tree_list:
    word = i.replace(" ", "")
    createPermutation(word)
# END
# AVOID DUPLICATE PERMUTATIONS FROM THE LIST step 4

orginalPemutation = dict()

for i in tree_list:
    word = i.replace(" ", "")
    orginalPemutation[word] = []
    for j in permutationList[word]:
        newper = j.upper()
        first_char_of_input = word[0]
        first_char_of_per = j[0]
        if first_char_of_input == first_char_of_per:
            orginalPemutation[word].append(newper)

# END

# code for take best result from the list step 5
result = dict()
def checkSequence(a, b):
    if len(b) == 0:
        return True
    if len(a) == 0:
        return False

    if (a[0] == b[0]):
        return checkSequence(a[1:], b[1:])
    else:
        return checkSequence(a[1:], b)

for i in tree_list:
    word = i.replace(" ", "")
    result[word] = []
    for i in orginalPemutation[word]:
        if __name__ == '__main__':
            s1 = word.upper()
            s2 = i
            if (checkSequence(s1, s2)):
                result[word].append(s2)
# end

# code for permutation with value step 6
total = 0
count_of_totoal = 0
keypair = ""
permutationWithValue = dict()
for i in tree_list:
    word = i.replace(" ", "")
    count: int = 0
    permutationWithValue[word] = []
    for j in result[word]:
        for k in j:
            split_result = len(i.split())
            if split_result == 1:
                if count > 0:
                    if count_of_totoal <= 3:
                        count_of_totoal += 1
                        value_of_k = int(newvalues[k])
                        total = total + value_of_k
                else:
                    if count_of_totoal <= 3:
                        count_of_totoal += 1
                        count += 1
            else:
                if count > 0:
                    var = i.split(" ")[1]
                    if j[1] == var[0] and j[1] == k:
                        if j[2] == var[0]:
                            if count_of_totoal <= 3:
                                count_of_totoal += 1
                                value_of_k = int(newvalues[k])
                                total = total + value_of_k
                    else:
                        if count_of_totoal <= 3:
                            count_of_totoal += 1
                            value_of_k = int(newvalues[k])
                            total = total + value_of_k
                else:
                    if count_of_totoal <= 3:
                        count_of_totoal += 1
                        count += 1
        for x, y in enumerate(word):
            for k in j:
                length = len(word)
                new_length = length - 1
                yUpper = y.upper()
                if yUpper == k:
                    if x == 1:
                        if count_of_totoal <= 3:
                            count_of_totoal += 1
                            total += 1
                    if x == 2:
                        if count_of_totoal <= 3:
                            count_of_totoal += 1
                            total += 2
                    if x >= 3:
                        if count_of_totoal <= 3:
                            count_of_totoal += 1
                            total += 3
                    if new_length == x:
                        if yUpper == 'E':
                            if count_of_totoal <= 3:
                                count_of_totoal += 1
                                total += 20
                    if new_length == x:
                        if yUpper == 'L' or yUpper == 'D':
                            if count_of_totoal <= 3:
                                count_of_totoal += 1
                                total += 5
        permutationWithValue[word].append(total)
        count = 0
        total = 0
        count_of_totoal = 0
# End

# code for find the correct abr for the index step 7
print(result)
print(permutationWithValue)
positions = dict()
repeated = dict()
for i in tree_list:
    word = i.replace(" ", "")
    small = min(permutationWithValue[word])
    positions[word] = []
    for index,val in enumerate(permutationWithValue[word]):
        if val == small:
            positions[word].append(index)

for word in tree_list:
    word = word.replace(" ", "")
    repeated[word] = []
    for a in positions[word]:
        repeated[word].append(result[word][a])
print(repeated)

# end

# code for delete duplicate value from the list step 8
temp = []
final_result = dict()
for word in tree_list:
    word = word.replace(" ", "")
    final_result[word] = []
    for x in repeated[word]:
        if x not in temp:
            temp.append(x)
            final_result[word].append(x)

# End

# code for write output to a file step 9
f = open('vinod_trees_abbrevs.txt','a')
count = 0
for word in tree_list:
    word = word.replace(" ", "")
    f.write(word)
    f.write('\n')
    for k in final_result[word]:
        if count <= len(final_result[word]):
            count +=1
            f.write(k)
            f.write('\t')
    f.write('\n')
    count =0
f.close()
# End