#Write your function here
def more_frequent_item(my_list, item1, item2):
  iterative = 0
  iterative2 = 0
  for i in range(len(my_list)):
    if my_list[i] == item1:
      iterative += 1
    if my_list[i] == item2:
      iterative2 += 1
  if iterative >= iterative2:
    return item1
  return item2
#Remember, Python allows you to save plenty lines of code!
#Can simply use the count method, as it will literally inform you of the occurences
# my_list.count(item1) >= my.list.count(item2) return item 1
#return item 2
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
