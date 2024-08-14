def binary_search(data, target):
  guess = 0
  right = len(data) - 1

  while guess <= right:
    mid = (guess + right) // 2 # find mid index

    if data[mid] == target:
      return mid
    elif data[mid] < target:
      guess = mid + 1
    else:
      right = mid - 1
  return -1

data = [1,2,3,5,7,11,13,17,19,23,27,29,31]
target = 23

result = binary_search(data, target)

guess = input("Guess: ")

if result != -1:
  print(f"Target {target} ditemukan pada indeks {result}")
else:
  print(f"Target {target} tidak ditemukan")
