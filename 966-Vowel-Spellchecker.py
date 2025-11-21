def spellchecker(wordlist, queries):
    perfect = set()
    cap = {}
    vow = {}

    for w in wordlist:
        perfect.add(w)

        l = w.lower()
        if not l in cap:
            cap[l] = w

        p = "".join('*' if c in 'aeiou' else c for c in l)
        if not p in vow:
            vow[p] = w

    res = []
    for q in queries:
        if q in perfect:
            res.append(q)
            continue

        l = q.lower()
        if l in cap:
            res.append(cap[l])
            continue

        p = "".join('*' if c in 'aeiou' else c for c in l)
        if p in vow:
            res.append(vow[p])
            continue
        res.append('')
    return res


wordlist = ["yellow"]
queries = ["YellOw", "yollow", "yeellow"]

print(spellchecker(wordlist, queries))


words = ["DoRiAn"]


def returnWords():
    for j in words:
        dd = j.lower()
    return dd


print(returnWords())
