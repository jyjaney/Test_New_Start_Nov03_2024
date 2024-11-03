from collections import Counter

def most_frequent(lst):
    most_common = Counter(lst).most_common(1)
    most_value = Counter(lst).values()
    return most_common[0][0]

lst = [3,4,2,12,12,10,54,1]
#print(most_frequent(lst))

def reverse_words(sentence):
    words = sentence.split()
    new_sentence = ''.join(word[::-1] for word in words[::-1])
    return new_sentence

sentence = "A good sheep!"
#print(reverse_words(sentence))


def are_anagrams(str1, str2):
    new_str1 = sorted(str1.replace(' ', '').lower())
    new_str2 = sorted(str2.replace(' ', '').lower())

    return new_str1 == new_str2

str1 = 'Listen'
str2 = 'Silent'
#print(are_anagrams(str1, str2))

def count_vowel(s):
    vowel = set('aeiouAEIOU')
    sum = 0
    for char in s:
        if char in vowel:
            sum+=1
    return sum

s = 'aaeeyct'
#print(count_vowel(s))

def even_num(numbers):
    res = []
    for num in numbers:
        if num % 2 == 0:
            res.append(num)
    return res

numbers = [1,2,3,4]
#print(even_num(numbers))


def group_components_by_temperature(components):

    group_result = {
        "low": [],
        "medium": [],
        "high" : []
    }

    for component in components:
        if component["status"] == "active":
            temperature = component["temperature"]
            if temperature < 30:
                group_result["low"].append(component["component"])
            elif temperature >= 30 and temperature<60:
                group_result["medium"].append(component["component"])
            elif temperature > 60:
                group_result["high"].append(component["component"])

    return group_result


components = [
    {"component": "CPU", "status": "active", "temperature": 65},
    {"component": "GPU", "status": "inactive", "temperature": 45},
    {"component": "RAM", "status": "active", "temperature": 25},
    {"component": "SSD", "status": "active", "temperature": 40},
    {"component": "Battery", "status": "active", "temperature": 75}
]

print(group_components_by_temperature(components))
