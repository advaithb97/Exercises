set_1 = set(["a", "b", "c"]) 
set_2 = set(["c", "d", "e"])
forward = set_1 - set_2
backward = set_2 - set_1
result = forward | backward