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
        answer = 1 + min(chopS1,chopS2)
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
    my_return = []
    for item in sorted_list[0:5]:
        my_return.append(item[0])
    return my_return
