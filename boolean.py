# tuples, sets and dic always false when empty

done = False

print(type(done) == bool)

if done:
  print("Work is done!")
else:
  print("Work is not done!")
  
  
book_1_read = True
book_2_read = False

#any() if any of iterable has True then it returns true
read_any_book = any([book_1_read, book_2_read])

#all() if all of iterable has True then it returns true
read_any_1_book = all([book_1_read, book_2_read])

print(read_any_book)