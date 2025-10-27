import random, sys, time

while True:
    print("Get ready to draw! Press Enter as soon as you see 'DRAW!'")
    input("Press Enter to start...")
    time.sleep(random.random() * 3 + 1)
    print("DRAW!")
    start_time = time.perf_counter()
    input("")
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    
    if elapsed_time < 0.01:
        print("You drew before DRAW\n")
        continue
    elif elapsed_time < 0.07:
        print(f"You took {elapsed_time:.2f} seconds!")
        print("Too fast! Are you cheating? Let's try again.\n")
        continue
    elif elapsed_time > 0.4:
        print(f"You took {elapsed_time:.2f} seconds!")
        print("Too slow! Let's try again.\n")
        continue
    else:
        print(f"You took {elapsed_time:.2f} seconds!")
        print("Nice job! Let's try again.\n")   
    
    cont = input("Do you want to play again? (y/n): ").strip().lower()
    if cont != 'y':
        break
    
print("Thanks for playing! Goodbye.")