#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    words1 = input("Good day, please, enter your first sentence:\n")
    words2 = input("\nVery well, now your second sentence:\n")
    symbols = set(words2).intersection(set(words1))
    print("\nAccording to our calculations, equal symbols are:", ','.join(symbols))
