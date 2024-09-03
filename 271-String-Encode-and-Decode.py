def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "&" + s
    return res


def decode(ss):
    decode_ls = []
    i = 0
    while i < len(ss):
        length = int(ss[i])
        start = i + 1 + len(str(length))
        end = start + length
        decode_ls.append(ss[start:end])
        i = end
    return decode_ls


def encode1(strs):
    res = ""
    for s in strs:
        res += s + "0xC1"
    return res


def decode1(ss):
    res = ss.split("0xC1")
    res.pop(-1)
    return res


ls = ["neet", "code", ":", "you"]
print(encode(ls))
print(decode(encode(ls)))

print(encode1(ls))
print(decode1(encode1(ls)))
