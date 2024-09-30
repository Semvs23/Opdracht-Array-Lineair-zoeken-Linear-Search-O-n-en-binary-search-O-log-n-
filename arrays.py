import random
import time

# Lineair zoeken
def linear_search(array, target):
    for element in array:
        if element == target:
            return True
    return False

# Binair zoeken
def binary_search(array, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, low, mid - 1)
    else:
        return binary_search(array, target, mid + 1, high)

# Array van 10.000 willekeurige nummers (tussen 1 en 100000)
array = random.sample(range(1, 100001), 10000)

# Sorteer de array
array.sort()

# Zelf een target instellen
target = int(input("Voer het getal in dat je wilt zoeken: "))

# Lineair zoeken testen
start_time = time.time()
linear_search_result = linear_search(array, target)
linear_search_time = time.time() - start_time

# Binair zoeken testen
start_time = time.time()
binary_search_result = binary_search(array, target, 0, len(array) - 1)
binary_search_time = time.time() - start_time

# Resultaten printen
print(f"Lineair zoeken vond het target {target}: {linear_search_result} in {linear_search_time:.6f} seconden")
print(f"Binair zoeken vond het target {target}: {binary_search_result} in {binary_search_time:.6f} seconden")
