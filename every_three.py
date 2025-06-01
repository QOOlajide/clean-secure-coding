#Here, my intention is to print every three nums once being provided with a start parameter. So long as the parameter is less no more than 100, I can return a list
#Let's think if this is the most efficient example

def every_three_nums(start):
  if start > 100:
    return []
  my_list = []
  for i in range(start, 101, 3):
    my_list.append(i)
  return my_list

#Uncomment the line below when your function is done
print(every_three_nums(91))
