import random

def generate_random_numbers():
    print("=== Advanced Random Number Generator ===")
    
    # Ask for min and max values
    while True:
        try:
            min_val = float(input("Enter minimum value: "))
            max_val = float(input("Enter maximum value: "))
            if max_val < min_val:
                print("Maximum must be greater than minimum. Try again.")
                continue
            break
        except ValueError:
            print("Please enter valid numbers.")

    # Ask for count
    while True:
        try:
            count = int(input("How many numbers do you want to generate? "))
            if count <= 0:
                print("Number of values must be greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Ask for type: integer or float
    while True:
        num_type = input("Type of numbers? Enter 'int' or 'float': ").strip().lower()
        if num_type not in ['int', 'float']:
            print("Please enter 'int' or 'float'.")
        else:
            break

    # Generate numbers
    numbers = []
    for _ in range(count):
        if num_type == 'int':
            numbers.append(random.randint(int(min_val), int(max_val)))
        else:
            numbers.append(round(random.uniform(min_val, max_val), 4))  # 4 decimal places

    # Show results
    print("\nGenerated numbers:")
    print(numbers)

if __name__ == "__main__":
    generate_random_numbers()
