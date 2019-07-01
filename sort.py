def compare_versions(v1, v2):
    a1 = v1.split('.')
    a2 = v2.split('.')
    shortest_ver = min(len(a1), len(a2))
    result = False
    not_eq = False
    for k in range(shortest_ver):
        if int(a1[k]) < int(a2[k]):
            result = True
            not_eq = True
            break
        elif int(a1[k]) > int(a2[k]):
            not_eq = True
            break
    if not not_eq:
        if len(a1) < len(a2):
            result = True
    return result


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if compare_versions(arr[j], pivot):
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr


def bubble_sort(arr):
    for j1 in range(0, len(arr)):
        for j2 in range(0, len(arr)):
            if compare_versions(arr[j1], arr[j2]):
                arr[j1], arr[j2] = arr[j2], arr[j1]
    return arr


lines = [
    "2.0",
    "2.1",
    "2.2",
    "2.10",
    "3.1",
    "1.0",
    "2.3",
    "1.0.1",
    "2.4",
    "3.0",
    "2.5",
    "2.6",
    "4.0",
    "2.7",
    "1.1",
    "2.8",
    "4.1",
    "5.0",
    "2.9",
]

n = len(lines)
# sorted_arr = bubble_sort(lines)
sorted_arr = quick_sort(lines, 0, n - 1)
print("Sorted array is:")
for jj in range(n):
    print("%s" % sorted_arr[jj]),
