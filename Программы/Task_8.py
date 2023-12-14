#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    print("Good day! Please, choose language (ru - Русский, eng - English).")
    language = input("If you need both of them, print anything else - ")
    if language == "ru":
        letters = {"о", "е", "ё", "а", "и", "у", "я", "ы", "ю", "я"}
        words = input("\nВеликолепно, теперь введите предложение: ")
        print("\nСогласно нашим подсчётам, количество гласных:")
    elif language == "eng":
        letters = {"e", "a", "o", "i", "u", "y"}
        words = input("\nGreat, now, please, enter your sentence: ")
        print("\nAccording to our calculations, amount of vowels is: ")
    else:
        letters = {"о", "е", "ё", "а", "и", "у", "я", "ы", "ю", "я",
                   "e", "a", "o", "i", "u", "y"}
        words = input("\nGreat, now, please, enter your sentence: ")
        print("\nAccording to our calculations, amount of vowels is: ")
    amount = sum(1 for letter in words.lower() if letter in letters)
    print(amount)
