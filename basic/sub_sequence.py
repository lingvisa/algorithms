"""
l1 = [1, 2, 3, 4]

l2 = [2, 1]      # fails
l3 = [1, 2, 4]   # succeeds
l4 = [2, 3]      # succeeds
l5 = [2, 3, 1]   # fails
l6 = [1,2,3,4,5] # fails

Judge whether l2 matches l1:
For each element e in l2, e must be in l1 too;
and for any two sequential elements e1 and e2, if e1 appears before e2, then e1 must also appear before e2 in l1.
"""

def sub_match_1(l1, l2):
    i = iter(l1)
    return all(e in i for e in l2)

def sub_match_2(l1, l2):
    i = iter(l1)
    for e in l2:
        try:
            while e != next(i):
                pass
            print(f"{e} matched")
        except StopIteration:
            return False
    return True

# test
l1 = [1, 2, 3, 4]
l2 = [2, 1]      # fails
l3 = [1, 2, 4]   # succeeds
l4 = [2, 3]      # succeeds
l5 = [2, 3, 1]   # fails
l6 = [1,2,3,4,5] # fails

answer = [False, True, True, False, False]

for idx, l in enumerate([l2, l3, l4, l5, l6]):
    assert (sub_match_1(l1, l) == answer[idx])
print ('Test sub_match_1 successful!')

for idx, l in enumerate([l2, l3, l4, l5, l6]):
    assert (sub_match_2(l1, l) == answer[idx])
print ('Test sub_match_2 successful!')

"""
l1 = [3, 1, 4, 1, 5, 9]
l2 = [{2, 3}, {1, 5, 2}, {9}]

=> l1 matches l1 == True, because:
     {2, 3} matches 3
     {1, 5, 2} matches 1 (or 5)
     {9} matches 9
     
Here, l2 can be thought of conceptually expanded to different possibilities by taking one element from each set:
l2_exp = [[2, 1, 9], [2, 5, 9], [2, 2, 9], [3, 1, 9], [3, 5, 9], [3, 2, 9]]
which means as long as one of those six possible lists represented by l2 matches l1, we have a successful match. Since [3, 1, 9] matches l1 , the whole l2 matches.

Return the matched sub-sequence
"""

def sub_match_3(l1, l2):
    it1 = iter(l1)
    # assume each pool from l2 does have a match in l1, and catch the exception:
    try:
        return [next(x for x in it1 if x in pool) for pool in l2]
    except StopIteration:
        # return nothing
        pass

def sub_match_4(l1, l2):
    matched = []
    it1 = iter(l1)
    for pool in l2:
        for x in it1:
            if x in pool:
                matched.append(x)
                break
        else:
            return
    return matched

def sub_match_5(l1, l2):
    matched = []
    it1 = iter(l1)
    # not matched.append(x): always return True, which is a trick to store the matched element into the list
    if all(any(x in pool and not matched.append(x) for x in it1) for pool in l2):
        return matched

    # return nothing

# test
funcs = [sub_match_3, sub_match_4, sub_match_5]

for func in funcs:

    l1 = [1, 2, 3, 4]
    l2 = [{2, 1}, {1, 3}]
    print(func(l1,l2)) # True

    l1 = [1, 2, 3, 4]
    l2 = [{2, 1}, {1, 3}, {3, 4}]
    print(func(l1,l2)) # True

    l1 = [1, 2, 4, 3]
    l2 = [{2, 1}, {1, 3}, {3, 4}]
    print(func(l1,l2)) # False

    print(f'{func} test done.')