#!/usr/bin/env python3

def kmp_preprocess(needle: str):
    """Вычисляет функцию префикса для needle."""
    m = len(needle)
    b = [-1] * m
    i = 0
    j = -1
    while i < m:
        while j >= 0 and needle[i] != needle[j]:
            j = b[j]
        i += 1
        j += 1
        if i < m:
            b[i] = j
    return b


def kmp(hive: str, needle: str) -> int:
    """
    Ищет needle в hive.

    b - куда сдвинуть текущее положение
        в needle, если не совпала буква
    """
    b = kmp_preprocess(needle)
    i = 0                       # hive
    j = 0                       # needle
    n = len(hive)
    m = len(needle)
    while i < n:
        while j >= 0 and hive[i] != needle[j]:
            j = b[j]
        i += 1
        j += 1
        if j == m:
            return i-j
    return -1


for s in ["abcd", "aaab", "abacabad"]:
    print(s, " -> ", kmp_preprocess(s))

for s,t in [("abc", "abdabca"),
            ("aab", "aaaaaaaaaaaaaab"),
            ("abacabad", "abababacabacabad")]:
    print(s, " ", t, ": ", kmp(t, s))
