# prime-computer

A simple Python program that computes all prime numbers within a user-defined range.

## How it works

* Enter a lower and upper limit.
* The program computes every prime number within the selected range.
* To determine whether a number is prime, it checks for divisors other than **1** and the number itself.
* For better performance, the program:

  * Skips all even numbers (except **2**).
  * Checks only odd divisors.
  * Tests divisibility only up to the square root of each candidate number.
* After the computation is complete, the program automatically logs each run containing:

    * The complete list of prime numbers.
    * The total number of primes found.
    * The elapsed computation time.
    * The prime density within the selected range.

## Requirements

* Python 3.x
* No external libraries are required.

## Usage

1. Run the program.
2. Enter the lower and upper limits when prompted.
3. Wait for the computation to finish.
4. View the results in the generated log file (it is mentioned in the terminal).

Feel free to use, modify, or improve this project. Feedback and suggestions are always appreciated!
