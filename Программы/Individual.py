#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"b", "c", "h", "i", "j"}
    b = {"e", "h", "i", "s", "w"}
    c = {"a", "b", "j", "k", "l", "m"}
    d = {"a", "h", "i", "w", "x"}
    # intersiction = и; union = или; difference = разность.
    x = (a.difference(c).intersection(u.difference(b)))
    y = (a.intersection(u.difference(b))).union(c.difference(d))
    print(f"Good day!\nSet x = {x}\nAnd set y = {y}")
