LOWER_BOUND = 284639
UPPER_BOUND = 748759

# This could be optimized, but I am behind
def check(pw):
    pw_list = [int(n) for n in str(pw)]
    has_double = False
    decreasing = False
    # For each digit up to the second to last
    # If there are two in a row, set the has_double flag to true
    # If any are decreasing, set the decreasing flag to false
    for i in range(0, len(pw_list) - 1):
        if pw_list[i] == pw_list[i + 1]:
            has_double = True
        if pw_list[i] > pw_list[i + 1]:
            decreasing = True
    return has_double and not decreasing

# Loop over the range and count the valid passwords
ct = 0
for i in range(LOWER_BOUND, UPPER_BOUND + 1):
    if check(i):
        ct += 1

print(ct)

