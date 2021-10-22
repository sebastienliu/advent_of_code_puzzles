def extract_numbers(file):
    """
    Convert the numbers from the input file to a list
    """
    input_file = open(file, "r")
    numbers_list = [int(line.strip()) for line in input_file]
    numbers_list.sort()
    return numbers_list


def find_two_sums(numbers_list, target):
    left, right = 0, len(numbers_list) - 1
    sums = 0
    while left != right:
        sums = numbers_list[left] + numbers_list[right]
        if sums > target:
            right -= 1
        elif sums < target:
            left += 1
        else:
            print(f"Number 1: {numbers_list[left]}, Number 2: {numbers_list[right]}")
            print(numbers_list[left] * numbers_list[right])
            return True
    return False


def find_three_sums(numbers_list, target):
    """
    Instead of using two pointer solution, we can two loops,
    one is to loop through the list, the second starts from i+1 to the end of the list
    Store the numbers in a hash and use sum - number1 - number2 = number3 is in the hash
    Then return the triplet
    """
    for i in range(len(numbers_list)):
        current_sum = target - numbers_list[i]
        s = set()
        for j in range(i + 1, len(numbers_list)):
            if (current_sum - numbers_list[j]) in s:
                third = current_sum - numbers_list[j]
                print(f"Number 1: {numbers_list[i]}, Number 2: {numbers_list[j]}, Number 3: {third}")
                print(numbers_list[i] * numbers_list[j] * third)
                return True
            s.add(numbers_list[j])
    return False



def main():
    target = 2020
    file = "input.txt"
    numbers_list = extract_numbers(file)
    find_two_sums(numbers_list, target)
    find_three_sums(numbers_list, target)


if __name__ == "__main__":
    main()
