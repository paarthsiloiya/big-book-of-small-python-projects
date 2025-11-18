import math
import sys
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    
    return [i for i in range(2, limit + 1) if sieve[i]]

def format_number(num):
    return f"{num:,}"

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def check_single_number():
    while True:
        print("🔍 Enter a number to check if it's prime:")
        response = input("> ").strip()
        
        if response.lower() in ['quit', 'exit', 'q']:
            return
        
        try:
            num = int(response)
            if num < 0:
                print("❌ Please enter a positive number.")
                continue
            
            start_time = time.time()
            result = is_prime(num)
            end_time = time.time()
            
            if result:
                print(f"✅ {format_number(num)} is PRIME!")
            else:
                print(f"❌ {format_number(num)} is NOT prime.")
            
            print(f"⏱️  Calculation time: {end_time - start_time:.6f} seconds")
            
            if num > 1:
                factors = []
                temp = num
                d = 2
                while d * d <= temp:
                    while temp % d == 0:
                        factors.append(d)
                        temp //= d
                    d += 1
                if temp > 1:
                    factors.append(temp)
                
                if not result and factors:
                    print(f"🔢 Prime factors: {' × '.join(map(str, factors))}")
            
            input("\n📖 Press Enter to continue...")
            
        except ValueError:
            print("❌ Please enter a valid number.")

def find_range_primes():
    while True:
        print("🎯 Find primes in a range:")
        print("Enter start number:")
        start_input = input("> ").strip()
        
        if start_input.lower() in ['quit', 'exit', 'q']:
            return
        
        print("Enter end number:")
        end_input = input("> ").strip()
        
        if end_input.lower() in ['quit', 'exit', 'q']:
            return
        
        try:
            start = int(start_input)
            end = int(end_input)
            
            if start < 0 or end < 0:
                print("❌ Please enter positive numbers.")
                continue
            
            if start > end:
                start, end = end, start
                print(f"🔄 Swapped range: {format_number(start)} to {format_number(end)}")
            
            range_size = end - start + 1
            if range_size > 1000000:
                print(f"⚠️  Large range ({format_number(range_size)} numbers). This may take time.")
                confirm = input("Continue? (y/n): ").lower()
                if confirm != 'y':
                    continue
            
            print(f"\n🔍 Finding primes from {format_number(start)} to {format_number(end)}...")
            start_time = time.time()
            
            if end <= 1000000 and start <= 2:
                primes = sieve_of_eratosthenes(min(end, 1000000))
                primes = [p for p in primes if p >= start]
            else:
                primes = find_primes_in_range(start, end)
            
            end_time = time.time()
            
            print(f"\n📊 Found {len(primes)} primes in {end_time - start_time:.3f} seconds")
            
            if len(primes) <= 100:
                print(f"\n🔢 Primes found:")
                for i, prime in enumerate(primes):
                    if i % 10 == 0 and i > 0:
                        print()
                    print(f"{prime:8,}", end=" ")
                print()
            else:
                print(f"\n🔢 First 10: {', '.join(map(str, primes[:10]))}")
                print(f"🔢 Last 10: {', '.join(map(str, primes[-10:]))}")
            
            if primes:
                largest = primes[-1]
                print(f"\n🏆 Largest prime in range: {format_number(largest)}")
                
                save = input("\n💾 Save results to file? (y/n): ").lower()
                if save == 'y':
                    filename = f"primes_{start}_to_{end}.txt"
                    with open(filename, 'w') as f:
                        f.write(f"Prime numbers from {start} to {end}\n")
                        f.write(f"Total count: {len(primes)}\n\n")
                        for prime in primes:
                            f.write(f"{prime}\n")
                    print(f"✅ Saved to {filename}")
            
            input("\n📖 Press Enter to continue...")
            break
            
        except ValueError:
            print("❌ Please enter valid numbers.")

def continuous_search():
    while True:
        print("🚀 Continuous prime search:")
        print("Enter starting number:")
        response = input("> ").strip()
        
        if response.lower() in ['quit', 'exit', 'q']:
            return
        
        try:
            start_num = int(response)
            if start_num < 0:
                print("❌ Please enter a positive number.")
                continue
            
            print("\nEnter search limit (optional, press Enter for unlimited):")
            limit_input = input("> ").strip()
            
            limit = None
            if limit_input:
                try:
                    limit = int(limit_input)
                    if limit <= start_num:
                        print("❌ Limit must be greater than start number.")
                        continue
                except ValueError:
                    print("❌ Invalid limit. Proceeding with unlimited search.")
            
            print(f"\n🔍 Searching for primes starting from {format_number(start_num)}")
            if limit:
                print(f"📊 Up to {format_number(limit)}")
            print("⏹️  Press Ctrl+C to stop\n")
            
            input("📖 Press Enter to begin...")
            print()
            
            num = start_num
            count = 0
            start_time = time.time()
            
            try:
                while True:
                    if limit and num > limit:
                        break
                    
                    if is_prime(num):
                        count += 1
                        elapsed = time.time() - start_time
                        rate = count / elapsed if elapsed > 0 else 0
                        
                        print(f"{format_number(num):>15} | #{count:>6} | {rate:>6.1f}/sec | {elapsed:>8.1f}s")
                        
                        if count % 100 == 0:
                            time.sleep(0.1)
                    
                    num += 1
            
            except KeyboardInterrupt:
                elapsed = time.time() - start_time
                print(f"\n\n⏹️  Search stopped!")
                print(f"📊 Found {count} primes in {elapsed:.1f} seconds")
                print(f"🏁 Last number checked: {format_number(num)}")
            
            input("\n📖 Press Enter to continue...")
            break
            
        except ValueError:
            print("❌ Please enter a valid number.")

def display_menu():
    print("🔢 PRIME NUMBER EXPLORER 🔢")
    print("=" * 40)
    print("1. Check if number is prime")
    print("2. Find primes in range")
    print("3. Continuous prime search")
    print("4. Prime number facts")
    print("5. Clear screen")
    print("0. Quit")
    print("-" * 40)

def show_prime_facts():
    facts = [
        "🔸 2 is the only even prime number",
        "🔸 All primes > 2 are odd numbers",
        "🔸 There are infinitely many prime numbers",
        "🔸 The largest known prime has over 24 million digits",
        "🔸 Prime gaps can be arbitrarily large",
        "🔸 Twin primes are primes that differ by 2 (like 11,13)",
        "🔸 The prime number theorem describes prime distribution",
        "🔸 Mersenne primes: 2^n - 1 where n is prime",
        "🔸 RSA encryption relies on large prime numbers",
        "🔸 The Goldbach conjecture: every even number > 2 is sum of two primes"
    ]
    
    print("\n📚 PRIME NUMBER FACTS")
    print("=" * 50)
    for fact in facts:
        print(fact)
    print("=" * 50)

def main():
    try:
        while True:
            display_menu()
            choice = input("🔍 Enter choice: ").strip()
            
            if choice == '0' or choice.lower() == 'quit':
                print("\n🔢 Thanks for exploring prime numbers!")
                break
            
            elif choice == '1':
                check_single_number()
            
            elif choice == '2':
                find_range_primes()
            
            elif choice == '3':
                continuous_search()
            
            elif choice == '4':
                show_prime_facts()
                input("\n📖 Press Enter to continue...")
            
            elif choice == '5':
                clear_screen()
            
            else:
                print("❌ Invalid choice. Please try again.")
                input("📖 Press Enter to continue...")
    
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == '__main__':
    main()