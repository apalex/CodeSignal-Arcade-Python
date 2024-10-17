# What will be the value of res after the following
# is executed:
# xs = [()]
# res = [False] * 2
# if xs:
#   res[0] = True
# if xs[0]:
#   res[1] = True

xs = [()]
res = [False] * 2
if xs:
  res[0] = True
if xs[0]:
  res[1] = True

print(res)

# Output: [True, False]
