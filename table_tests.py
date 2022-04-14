#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import table as tb

# %% Tests des méthodes put, __str__, empty_table, length(héritage)
t = tb.Table()
print("t.empty_table() :", t.empty_table())
t.put("zero", 0)
t.put("un", 1)
t.put("deux", 2)
print("t :", t)
print("t.length() :", t.length(), "t.empty_table() :", t.empty_table())

# %% Tests des méthodes keys, values
t = tb.Table()
t.put("zero", 0)
t.put("un", 1)
t.put("deux", 2)
print("t :", t)
print("t.print_keys() :", t.print_keys())
print("t.print_values() :", t.print_values())

# %% Tests de la méthode get_elt
t = tb.Table()
t.put("zero", 0)
t.put("un", 1)
t.put("deux", 2)
print("t :", t)
print("t.get_elt('un'):", t.get_elt('un'))
print("t.get_elt('deux'):", t.get_elt('deux'))
print("t.get_elt('zero'):", t.get_elt('zero'))

# %% Tests de la méthode remove
t = tb.Table()
t.put("zero", 0)
t.put("un", 1)
t.put("deux", 2)
print("t :", t)
print("t.remove('un'):", t.remove('un')," --> t :", t)
print("t.remove('trois'):", t.remove('trois')," --> t :", t)