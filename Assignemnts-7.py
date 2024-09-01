def is_prime(num):
  """Checks if a number is prime."""
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def main():
  name = input("What's your name? ")
  print(f"Hello, {name}! Let's explore your favorite numbers.")

  numbers = []
  for i in range(3):
    number = int(input(f"Enter your {i+1} favorite number: "))
    numbers.append(number)

  even_odd_numbers = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

  print("\nLet's see what your numbers can do!")
  for num in numbers:
    print(f"{num} squared is {num * num}.")

  sum_of_numbers = sum(numbers)
  print(f"\nThe sum of your numbers is {sum_of_numbers}. That's a great number!")

  if is_prime(sum_of_numbers):
    print(f"And guess what? {sum_of_numbers} is a prime number! Lucky you!")
  else:
    print(f"Unfortunately, {sum_of_numbers} is not a prime number. But it's still a cool number.")

if __name__ == "__main__":
  main()