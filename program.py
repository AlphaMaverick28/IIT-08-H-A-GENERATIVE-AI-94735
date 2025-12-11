numbers = []

while True:
    num = input("Enter a number (or type 'done' to finish): ")

    if num.lower() == "done":
        break
    
    numbers.append(float(num))

if len(numbers) > 0:
    avg = sum(numbers) / len(numbers)
    print("Average =", avg)
else:
    print("No numbers entered.")
