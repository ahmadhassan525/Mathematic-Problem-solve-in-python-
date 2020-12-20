number = int(input("How many numbers !!!"))

total_number = 0

for i in range(0,number):
    numbers =  float(input("Enter the Number"))

    total_number = total_number + numbers

average =  total_number / number

print(f"Average number of {average}")   