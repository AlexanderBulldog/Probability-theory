def rook_combinations (k):
    good_combinations = 1
    all_combinations = 1
    combos = 64
    for _ in range (1, k+1):
        all_combinations *= combos
        combos -= 1

    combos = 81
    step_variations = 17
    for _ in range (1, k+1):
        good_combinations *= combos - step_variations
        combos -= step_variations
        step_variations -= 2
    return (good_combinations/all_combinations)


k = 4
print (rook_combinations(k))