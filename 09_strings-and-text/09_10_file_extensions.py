# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

print(file_1.endswith(".pdf"))
print(file_2.endswith(".pdf"))
print(file_3.endswith(".pdf"))
print(file_4.endswith(".pdf"))

#for x in range(1, 5):
#    print(("file_" + str(x)).endswith(".pdf"))
#    print(x)
# I get that this check the string called file_x instead of the variable, but I don't know how to do that yet.