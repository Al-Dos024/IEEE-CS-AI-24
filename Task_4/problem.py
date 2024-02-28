# takes list from user separated by commas
def get_numbers():
    while True:
        try:
            num_list = input("Enter a list of numbers separated by commas: ").strip()
            numbers = [int(x) for x in num_list.split(",")]
            return numbers
        except ValueError:
            print("Please enter a valid list of numbers.")


def find_min(numbers):
    # didnt found the number
    if not numbers:
        return None
    # found? , we set initial value the 1st number in list
    # to compare with the other if found lower we set it as min
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


def find_max(numbers):
    if not numbers:
        return None
    # same as min
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def find_mean(numbers):
    if not numbers:
        return None
    # total value / the length of list
    total = sum(numbers)
    return total / len(numbers)

# the number that repeat the most
def find_mode(numbers):
    if not numbers:
        return None
    # i made a set to count every number in the numbers
    # not list because list needs to be ordered
    count = {}
    # we use indexing postion to count the number
    # ex : we have list [1,2,2,5,5,5] it should be like 
    # count = {1: 1, 2: 2, 5: 3}
    for num in numbers:
        if num in count:
            count[num] += 1
        # if no num in list make a one
        else:
            count[num] = 1
    max_count = max(count.values())
    mode = [num for num, count in count.items() if count == max_count]
    return mode

# the number that in the middel
def find_median(numbers):
    if not numbers:
        return None
    # to get the median it should be sorted first
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    # if it was even
    if length % 2 == 0:
        return (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2
    # if it was odd
    else:
        return sorted_numbers[length // 2]


def find_range(numbers):
    if not numbers:
        return None
    # the diff between max num and min 
    return find_max(numbers) - find_min(numbers)


def find_variance(numbers):
    if not numbers:
        return None
    mean = find_mean(numbers)
    # the formaltion how to get it
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers)-1)
    return variance


def find_STD(numbers):
    if not numbers:
        return None
    # just add the square root to it
    return find_variance(numbers) ** 0.5


def find_Quariles(numbers):
    if not numbers:
        return None
    # need to be sorted
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    # 25%
    Q1 = find_median(sorted_numbers[:length // 2])
    # 50%
    Q2 = find_median(sorted_numbers)
    # 75%
    Q3 = find_median(sorted_numbers[(length + 1) // 2:])
    return Q1, Q2, Q3

# find the outliers
def find_IQR(numbers):
    Q1, _, Q3 = find_Quariles(numbers)
    return Q3 - Q1

# all the fun i test the output in video Example , was true :)
if __name__ == "__main__":
    numbers = get_numbers()
    print("Min:", find_min(numbers))
    print("Max:", find_max(numbers))
    print("Mean:", find_mean(numbers))
    print("Mode:", find_mode(numbers))
    print("Median:", find_median(numbers))
    print("Range:", find_range(numbers))
    print("Variance:", find_variance(numbers))
    print("Standard Deviation:", find_STD(numbers))
    print("Quartiles:", find_Quariles(numbers))
    print("Interquartile Range (IQR):", find_IQR(numbers))
