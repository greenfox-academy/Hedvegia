# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"

try:
    my_file = open("my-file.txt", "w")
    my_file.close()
except:
    print("Unable to write file: my-file.txt")
