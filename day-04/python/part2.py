LOWER_BOUND = 284639
UPPER_BOUND = 748759

def check(pw):
    # split into a list of ints
    pw_list = [int(n) for n in str(pw)]

    # initialize the digit counters and the accumulator
    curr_digit = -1
    curr_digit_ct = 0
    two_consecutive = False

    for i in range(0, len(pw_list) - 1):
        # If it's ever decreasing, bail out early
        if pw_list[i] > pw_list[i+1]:
            return False
        # If it's not the previous digit, reinitialize the count
        if pw_list[i] != curr_digit:
            # If there were two in a row before this, save that in the accumulator
            if curr_digit_ct == 2:
                two_consecutive = True
            # Save the current digit and reset the count to 1
            curr_digit = pw_list[i]
            curr_digit_ct = 1
        # If the next one matches, increment the accumulator by 1
        if pw_list[i] == pw_list[i + 1]:
            curr_digit_ct += 1
    # Handle the case of exactly two in a row at the end
    if curr_digit_ct == 2:
        two_consecutive = True
    return two_consecutive

# Loop over the range and count the valid passwords
ct = 0
for i in range(LOWER_BOUND, UPPER_BOUND + 1):
    if check(i):
        ct += 1

print(ct)
