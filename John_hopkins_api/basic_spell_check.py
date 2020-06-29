import copy
import time
def fastLCS(S1,S2):
    if (S1,S2) in memo:
        return memo[(S1,S2)]
    elif S1 == "":
        memo[(S1,S2)] = len(S2)
        return len(S2)
    elif S2 == "":
        memo[(S1,S2)] = len(S1)
        return len(S1)
    elif S1[0] == S2[0]:
        answer = fastLCS(S1[1:],S2[1:])
        memo[(S1,S2)] = answer
        return answer
    else:
        chopS1 = fastLCS(S1[1:],S2)
        chopS2 = fastLCS(S1,S2[1:])
        chopboth = fastLCS(S1[1:],S2[1:])
        if len(S1) >= 2:
            first = copy.deepcopy(S1)
            first = first[1]+first[0] + first[2:]
            chopS1_first = fastLCS(first[1:],S2)
            chopS2_first = fastLCS(first,S2[1:])
            chopboth_first = fastLCS(first[1:],S2[1:])
        else:
            chopS1_first,chopS2_first,chopboth_first = 100,100,100
        if len(S2) >= 2:
            second = copy.deepcopy(S2)
            second = second[1] + second[0] + second[2:]
            chopS1_second = fastLCS(S1[1:],second)
            chopS2_second = fastLCS(S1,second[1:])
            chopboth_second = fastLCS(S1[1:],second[1:])
        else:
            chopS1_second,chopS2_second,chopboth_second = 100,100,100
        answer = 1 + min(chopS1,chopS2,chopboth,chopS1_first,chopS2_first,chopboth_first,chopS1_second,chopS2_second,chopboth_second)
        memo[(S1,S2)] = answer
        return answer
    return fastLCS(S1,S2)
def spell_check(my_dictionary,string):
    def distance(my_tuple):
        return my_tuple[1]
    global memo
    memo = {}
    distance_to_country = []
    for x in my_dictionary:
        distance_to_country.append([x,fastLCS(x.lower(),string.lower())])
    sorted_list = sorted(distance_to_country, key = distance)
#    print(sorted_list)
#    return sorted_list
    my_return = []
    for item in sorted_list[0:5]:
        my_return.append(item[0])
    return my_return
#mytime = time.time()
#print(spell_check(["hello","helol","ehlol"],"hello"))
#print(time.time()-mytime)
