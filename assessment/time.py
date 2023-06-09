# Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

# Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

# Example 1:

# Input: arr = [1,2,3,4]
# Output: "23:41"
# Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
# Example 2:

# Input: arr = [5,5,5,5]
# Output: ""
# Explanation: There are no valid 24-hour times as "55:55" is not valid.


def solution(array):
    value=2359
    aaa=-1
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i==j or j==k or i==k: continue
                time=array[i]*1000+array[j]*100+array[k]*10+array[6-i-j-k]
                if time<2359:
                    aaa=max(aaa,time)
    if aaa==-1:
        return aaa
    return f'{aaa//100}:{aaa%100}'
