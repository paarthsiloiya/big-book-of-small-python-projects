import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_currency(amount):
    return f"${amount:,}"

def get_player_numbers():
    while True:
        print('🎯 Enter 5 different numbers from 1 to 69 (space-separated):')
        print('   Example: 5 17 23 42 50')
        response = input('> ').strip()

        if response.lower() == 'quick' or response.lower() == 'q':
            numbers = random.sample(range(1, 70), 5)
            print(f'🎲 Quick pick: {" ".join(map(str, sorted(numbers)))}')
            return sorted(numbers)

        try:
            numbers = list(map(int, response.split()))
            
            if len(numbers) != 5:
                print('❌ Please enter exactly 5 numbers.')
                continue
            
            if not all(1 <= num <= 69 for num in numbers):
                print('❌ All numbers must be between 1 and 69.')
                continue
            
            if len(set(numbers)) != 5:
                print('❌ All numbers must be different.')
                continue
            
            return sorted(numbers)
            
        except ValueError:
            print('❌ Please enter valid numbers only.')

def get_powerball():
    while True:
        print('\n⚡ Enter the Powerball number (1-26):')
        print('   Type "quick" or "q" for random selection')
        response = input('> ').strip()

        if response.lower() == 'quick' or response.lower() == 'q':
            powerball = random.randint(1, 26)
            print(f'🎲 Quick pick Powerball: {powerball}')
            return powerball

        try:
            powerball = int(response)
            if 1 <= powerball <= 26:
                return powerball
            else:
                print('❌ Powerball must be between 1 and 26.')
        except ValueError:
            print('❌ Please enter a valid number.')

def get_play_count():
    while True:
        print('\n🎮 How many times do you want to play?')
        print('   Enter number (1-10,000,000) or "auto" for continuous play:')
        response = input('> ').strip().lower()

        if response == 'auto':
            return 'auto'

        try:
            plays = int(response)
            if 1 <= plays <= 10000000:
                return plays
            else:
                print('❌ Please enter a number between 1 and 10,000,000.')
        except ValueError:
            print('❌ Please enter a valid number.')

def calculate_winnings(matched_numbers, matched_powerball):
    prizes = {
        (5, True): 1586000000,
        (5, False): 1000000,
        (4, True): 50000,
        (4, False): 100,
        (3, True): 100,
        (3, False): 7,
        (2, True): 7,
        (1, True): 4,
        (0, True): 4
    }
    return prizes.get((matched_numbers, matched_powerball), 0)

def display_stats(wins_by_prize, total_plays, total_spent, total_won):
    print("\n" + "="*60)
    print("🏆 LOTTERY STATISTICS")
    print("="*60)
    
    if any(wins_by_prize.values()):
        print("Prize Breakdown:")
        prize_names = {
            1586000000: "💰 JACKPOT",
            1000000: "🥇 $1 Million", 
            50000: "🥈 $50,000",
            100: "🥉 $100",
            7: "🎫 $7",
            4: "🍀 $4"
        }
        
        for prize, count in sorted(wins_by_prize.items(), reverse=True):
            if count > 0:
                print(f"   {prize_names.get(prize, f'${prize:,}')}: {count:,} times")
    else:
        print("💸 No prizes won")
    
    print(f"\n📊 Games Played: {total_plays:,}")
    print(f"💳 Total Spent: {format_currency(total_spent)}")
    print(f"💰 Total Won: {format_currency(total_won)}")
    print(f"📉 Net Loss: {format_currency(total_spent - total_won)}")
    
    if total_plays > 0:
        win_rate = (sum(wins_by_prize.values()) / total_plays) * 100
        print(f"🎯 Win Rate: {win_rate:.4f}%")
        
        odds_info = [
            ("Jackpot", "1 in 292,201,338"),
            ("Any Prize", "1 in 24.9")
        ]
        print(f"\n🎲 Odds Information:")
        for prize, odds in odds_info:
            print(f"   {prize}: {odds}")

def run_simulation(player_numbers, player_powerball, num_plays):
    wins_by_prize = {}
    total_won = 0
    jackpot_won = False
    
    if num_plays == 'auto':
        print("\n🚀 Starting automatic play... Press Ctrl+C to stop")
        plays_done = 0
        
        try:
            while True:
                plays_done += 1
                winning_numbers = sorted(random.sample(range(1, 70), 5))
                winning_powerball = random.randint(1, 26)
                
                matched_numbers = len(set(player_numbers) & set(winning_numbers))
                matched_powerball = (player_powerball == winning_powerball)
                
                prize = calculate_winnings(matched_numbers, matched_powerball)
                
                if prize > 0:
                    wins_by_prize[prize] = wins_by_prize.get(prize, 0) + 1
                    total_won += prize
                    
                    print(f"\n🎉 WIN #{plays_done:,}! Prize: {format_currency(prize)}")
                    print(f"   Numbers: {' '.join(map(str, winning_numbers))} | PB: {winning_powerball}")
                    print(f"   Matched: {matched_numbers} numbers + PB: {matched_powerball}")
                    
                    if prize >= 1586000000:
                        print("🎊 JACKPOT! Stopping simulation...")
                        jackpot_won = True
                        break
                
                if plays_done % 100000 == 0:
                    print(f"📈 Played {plays_done:,} times... Total won: {format_currency(total_won)}")
                    
        except KeyboardInterrupt:
            print(f"\n⏹️ Simulation stopped after {plays_done:,} plays")
        
        return wins_by_prize, plays_done, total_won * 2, total_won, jackpot_won
    
    else:
        print(f"\n🎰 Running {num_plays:,} simulations...")
        
        for i in range(num_plays):
            winning_numbers = sorted(random.sample(range(1, 70), 5))
            winning_powerball = random.randint(1, 26)
            
            matched_numbers = len(set(player_numbers) & set(winning_numbers))
            matched_powerball = (player_powerball == winning_powerball)
            
            prize = calculate_winnings(matched_numbers, matched_powerball)
            
            if prize > 0:
                wins_by_prize[prize] = wins_by_prize.get(prize, 0) + 1
                total_won += prize
                
                if prize >= 1586000000:
                    print(f"\n🎊 JACKPOT WON on draw #{i+1}!")
                    jackpot_won = True
                    break
                elif prize >= 50000:
                    print(f"\n🎉 Big win on draw #{i+1}! Prize: {format_currency(prize)}")
            
            if (i + 1) % 50000 == 0:
                print(f"   Progress: {i+1:,}/{num_plays:,} ({((i+1)/num_plays)*100:.1f}%)")
        
        return wins_by_prize, num_plays, num_plays * 2, total_won, jackpot_won

def main():
    print('🎰 POWERBALL LOTTERY SIMULATOR 🎰')
    print('='*50)
    print('💡 Tips: Type "quick" or "q" for random number selection')
    print(f'💰 Jackpot: {format_currency(1586000000)}')
    print(f'🎫 Ticket Cost: $2 each')
    print(f'📊 Odds of winning jackpot: 1 in 292,201,338\n')

    while True:
        player_numbers = get_player_numbers()
        player_powerball = get_powerball()
        num_plays = get_play_count()
        
        print(f"\n🎯 Your Numbers: {' '.join(map(str, player_numbers))}")
        print(f"⚡ Your Powerball: {player_powerball}")
        
        if num_plays == 'auto':
            cost_msg = "Automatic play (unlimited budget)"
        else:
            total_cost = num_plays * 2
            cost_msg = f"{num_plays:,} plays costing {format_currency(total_cost)}"
        
        print(f"🎮 Playing: {cost_msg}")
        
        input("\n🚀 Press Enter to start the lottery simulation...")
        
        wins_by_prize, actual_plays, total_spent, total_won, won_jackpot = run_simulation(
            player_numbers, player_powerball, num_plays
        )
        
        display_stats(wins_by_prize, actual_plays, total_spent, total_won)
        
        if won_jackpot:
            print(f"\n🎊 CONGRATULATIONS! You won the {format_currency(1586000000)} jackpot!")
            print("💫 In real life, you'd be a billionaire!")
        else:
            loss = total_spent - total_won
            print(f"\n💸 You lost {format_currency(loss)} in this simulation.")
            print("🎭 At least it's not real money!")
        
        play_again = input("\n🔄 Play again? (y/n): ").strip().lower()
        if play_again not in ['y', 'yes']:
            break
        
        clear_screen()
    
    print("\n🎪 Thanks for playing the Powerball Lottery Simulator!")
    print("💡 Remember: The house always wins in real gambling!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Remember to gamble responsibly!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please restart the program.")