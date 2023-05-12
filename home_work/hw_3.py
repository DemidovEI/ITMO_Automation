def max_number(a, b):
    return max(a,b)


def diff_135(a, b):
    return 'Yes' if abs(a - b) == 135 else 'No'


def season(a):
    if a <= 2 and a == 12:
        return 'winter'
    elif 3 <= a  <= 5:
        return 'spring'
    elif 6 <= a <= 8:
        return 'summer'
    else:
        return 'autumn'


def nums_10(x, y, z):
    return 'Yes' if x > 10 and y > 10 and z > 10 else 'No'


def coun_positive(nums):
    count = 0
    for i in nums:
        if i > 0:
            count += 1
    return count


def day_of_life(years, month):
    days = (years * 12 + month) * 29
    return days
