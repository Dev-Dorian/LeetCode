from collections import defaultdict


def numMatchingSubseq(s, words):
    def is_subsequence(word, s):
        it = iter(s)
        return all(char in it for char in word)

    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1

    count = 0
    for word, freq in word_count.items():
        if is_subsequence(word, s):
            count += freq
    return count


def numMatchingSubseq_1(s, words):
    lookup = defaultdict(list)
    output = 0

    for i, c in enumerate(s):
        lookup[c].append(i)

    def bs(lst, i):
        left, right = 0, len(lst)
        while left < right:
            mid = (left + right) // 2
            if i < lst[mid]:
                right = mid
            else:
                left = mid + 1
        return left

    for w in words:
        prev = -1
        found = True
        for c in w:
            tmp = bs(lookup[c], prev)
            if tmp == len(lookup[c]):
                found = False
                break
            else:
                prev = lookup[c][tmp]
        if found:
            output += 1
    return output


def numMatchingSubseq_verbose(s, words):
    # 1. Pre-procesamiento
    lookup = defaultdict(list)
    for i, c in enumerate(s):
        lookup[c].append(i)

    print(f"--- PRE-PROCESAMIENTO ---")
    print(f"Cadena original: '{s}'")
    print(f"Mapa de posiciones (lookup): {dict(lookup)}\n")

    def bs(lst, i):
        left, right = 0, len(lst)
        while left < right:
            mid = (left + right) // 2
            if i < lst[mid]:
                right = mid
            else:
                left = mid + 1
        return left

    output = 0
    for w in words:
        print(f"🔍 Evaluando palabra: '{w}'")
        prev = -1
        found = True

        for char in w:
            if char not in lookup:
                print(
                    f"   ❌ La letra '{char}' ni siquiera existe en la cadena original.")
                found = False
                break

            # Buscar el siguiente índice disponible
            idx_en_lista = bs(lookup[char], prev)

            if idx_en_lista == len(lookup[char]):
                print(f"   ❌ No hay más '{char}' después del índice {prev}.")
                found = False
                break
            else:
                nuevo_indice = lookup[char][idx_en_lista]
                print(
                    f"   ✅ Letra '{char}' encontrada! Saltando del índice {prev} al {nuevo_indice}")
                prev = nuevo_indice

        if found:
            print(f"⭐ ¡Palabra '{w}' es una subsecuencia!")
            output += 1
        print("-" * 30)

    return output


# Prueba
s = "abacaba"
words = ["aaa", "abc", "ax"]
total = numMatchingSubseq_verbose(s, words)
print(f"\nRESULTADO FINAL: {total} palabras encontradas.")

s = "abcde"
words = ["a", "bb", "acd", "ace"]

print(numMatchingSubseq(s, words))
print(numMatchingSubseq_1(s, words))
print(numMatchingSubseq_verbose(s, words))
