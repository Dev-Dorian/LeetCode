def groupAnagrams(strs):
    hashmap = {}

    for st in strs:
        key = ''.join(sorted(st))
        if key not in hashmap:
            hashmap[key] = [st]
        else:
            hashmap[key] += [st]
    return hashmap.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
