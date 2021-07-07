# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

print(float(3))
print(int(5.95))
print(12.5 / 4)
a = 12
b = 14
print(a * b)

# Only when convertion from float to int is something lost.  Everything after the decimal is lost and
# it doesn't round the number at all.