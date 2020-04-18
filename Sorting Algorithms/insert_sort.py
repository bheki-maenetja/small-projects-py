from random import randint
import time

def insert_sort():
  start_time = time.time()
  my_list = [randint(0, 10000) for i in range(1000)]
  print(f"Here is your list: {my_list}")

  num_items = len(my_list)
  for pointer in range(1, num_items):
      ItemToBeInserted = my_list[pointer]
      CurrrentItem = pointer - 1
      while (my_list[CurrrentItem] > ItemToBeInserted) and (CurrrentItem > -1):
          my_list[CurrrentItem + 1] = my_list[CurrrentItem]
          CurrrentItem -= 1
      my_list[CurrrentItem + 1] = ItemToBeInserted
  end_time = time.time()
  print(f'Sorted List: {my_list}', f'\nRuntime: {(end_time - start_time) * 10 ** 3} ms')

def bubble_sort():
  start_time = time.time()
  numList = [randint(0, 10000) for i in range(1000)]
  print(f'Here is your list: {numList}')

  for i in range(0, len(numList) - 1):
    for j in range(0, len(numList) - 1):
      if numList[j] > numList[j + 1]:
        numList[j], numList[j + 1] = numList[j + 1], numList[j]
  end_time = time.time()
  print(f'Sorted List: {numList}', f'\nRuntime: {(end_time - start_time) * 10 ** 3} ms')
  
# bubble_sort()
# insert_sort()


