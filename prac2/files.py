out_file = open("name.txt", "w")
out_file.write(input("Enter your name: "))
out_file.close()

read_file = open("name.txt", "r")
name = read_file.readline()
print(f"Your name is {name}")
read_file.close()

read_file = open("numbers.txt", "r")
num1 = read_file.readline()
num2 = read_file.readline()
print(int(num2) + int(num1))
read_file.close()

read_file = open("numbers.txt", "r")
sum = 0
for line in read_file:
    sum += int(line)
print(sum)
read_file.close()
