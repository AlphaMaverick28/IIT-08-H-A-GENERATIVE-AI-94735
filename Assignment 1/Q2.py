
data = input("Enter numbers (comma-separated): ").strip()


nums = []
for part in data.split(","):
    part = part.strip()
    if part:
        try:
            nums.append(int(part))
        except ValueError:
            print(f"Warning: '{part}' is not an integer and will be ignored.")

even_count = sum(1 for n in nums if n % 2 == 0)
odd_count  = sum(1 for n in nums if n % 2 != 0)

print(f"Total numbers read: {len(nums)}")
print(f"Even: {even_count}")
print(f"Odd: {odd_count}")
