# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

# Forgot cylinder formulas.  surface area = 2pi(r)(h+r)
# volume = pi(r^2)h

radius = 3.14
height = 5

surface = 2 * 3.14159 * radius * (height + radius)
volume = 3.14159 * (radius ** 2) * height

print("the area of the surface is: " + str(surface))
print("the volume of the cylinder is: " + str(volume))