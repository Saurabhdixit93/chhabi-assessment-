# 1. answer ---------------


def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        min_idx = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_idx]:

                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
  
# Example usage

input_list = [5, 416, 54, 21, 6135, 15, 741]

sorted_list = selection_sort(input_list)

print(sorted_list)

# output
[5, 15, 21, 54, 416, 741, 6135]


# 2. answer ---------------

def get_file_type(extension_type_str, filenames):

    extension_type_pairs = extension_type_str.split(";")

    extension_type_dict = {}

    # Create a dictionary of extension-type pairs

    for pair in extension_type_pairs:

        extension, file_type = pair.split(",")

        extension_type_dict[extension] = file_type

    file_type_dict = {}
    
    # Determine file types for each filename
    for filename in filenames:
        file_extension = filename.split(".")[-1]

        if file_extension in extension_type_dict:
            file_type = extension_type_dict[file_extension]
        else:
            file_type = "unknown"

        file_type_dict[filename] = file_type

    return file_type_dict
  
  # Example usage

extension_type_str = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"

filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]

file_type_dict = get_file_type(extension_type_str, filenames)

print(file_type_dict)
  
# output 

{
  "abc.jpg": "image",
  "xyz.xls": "spreadsheet",
  "text.csv": "unknown",
  "123": "unknown"
}

  
# 3. answer ---------------
    
def sort_list_of_dicts(list_of_dicts, sort_key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[sort_key])
    return sorted_list


# Example usage
list_of_dicts = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_list_by_fruit = sort_list_of_dicts(list_of_dicts, "fruit")
print(sorted_list_by_fruit)

sorted_list_by_color = sort_list_of_dicts(list_of_dicts, "color")
print(sorted_list_by_color)

# output 
[    {"fruit": "apple", "color": "red"},    {"fruit": "banana", "color": "yellow"},    {"fruit": "blueberry", "color": "blue"},    {"fruit": "orange", "color": "orange"}]

[    {"fruit": "blueberry", "color": "blue"},    {"fruit": "orange", "color": "orange"},    {"fruit": "apple", "color": "red"},    {"fruit": "banana", "color": "yellow"}]

# 4. answer ---------------

def switch_key_value(dictionary):
    return {value: key for key, value in dictionary.items()}

# Example usage
input_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

result_dict = switch_key_value(input_dict)
print(result_dict)

# output 
{
    "value1": "key1",
    "value2": "key2",
    "value3": "key3",
    "value4": "key4",
    "value5": "key5"
}


# 5. answer --------------

def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    uncommon_elements = list(set(list1) ^ set(list2))
    return common_elements, uncommon_elements


# Example usage
mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]

common, uncommon = compare_lists(mainstream, must_watch)
print("Common elements:", common)
print("Uncommon elements:", uncommon)

# output 
Common elements: ['One Piece', 'Attack On Titan']
Uncommon elements: ['Sword Art Online', 'Full Metal Alchemist', 'Dragon Ball Z', 'The Devil is a Part Timer!', 'Code Geass', 'Death Note', 'One Punch Man', "Bleach", "Stein's Gate"]

  
 # 6. answer ---------------

def get_every_other_sublist(lst, start_idx, end_idx):
    sublist = lst[start_idx:end_idx+1]
    every_other_sublist = sublist[1::2]
    return every_other_sublist


# Example usage
input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = get_every_other_sublist(input_list, start_index, end_index)
print(result)

# output
[5, 11, 17, 23]


# 7. answer ---------------

from functools import reduce

number = 5
factorial = reduce(lambda x, y: x * y, range(1, number+1))

print(factorial)

# output 
120


# 8. answer ---------------

from functools import reduce

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i*i for i in A1}
A6 = [[i, i*i] for i in A1]
A7 = reduce(lambda x, y: x + y, [10, 23, -45, 33])
A8 = list(map(lambda x: x*2, [1, 2, 3, 4]))
A9 = list(filter(lambda x: len(x) > 3, ["I", "want", "to", "learn", "python"]))

print(A0)
print(list(A1))
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)
print(A7)
print(A8)
print(A9)


# output 

{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
[[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
21
[2, 4, 6, 8]
['want', 'learn', 'python']



# 9. answer ---------------

from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    date_format = '%y-%m-%d'
    date1 = datetime.strptime(from_date, date_format)
    date2 = datetime.strptime(to_date, date_format)
    delta = date2 - date1
    if delta < timedelta(days=difference):
        return True
    else:
        return False

# Example usage
from_date = '21-05-01'
to_date = '21-05-10'
difference = 10

result = check_date_difference(from_date, to_date, difference)
print(result)


# output 
True

# 10. answer ---------------

from datetime import datetime, timedelta

def calculate_previous_date(date, n):
    date_format = '%y-%m-%d'
    given_date = datetime.strptime(date, date_format)
    previous_date = given_date - timedelta(days=n)
    previous_date_str = previous_date.strftime(date_format)
    return previous_date_str

# Example usage
date = '16-12-10'
n = 11

result = calculate_previous_date(date, n)
print(result)

# output 

16-11-29


# 11. answer ---------------


def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3, [3, 2, 1])
f(3)


# output 

[0, 1]
[3, 2, 1, 0, 1, 4]
[0, 1, 0, 1, 4]



# _------------- complete ---------_





























