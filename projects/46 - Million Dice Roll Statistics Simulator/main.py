import random
import sys
import math
import os
from collections import Counter

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    clear_screen()
    print('🎲 ' + '=' * 70 + ' 🎲')
    print('|' + ' ' * 75 + '|')
    print('|' + ' 🎯 DICE ROLL STATISTICAL ANALYZER 🎯 '.center(73) + '|')
    print('|' + ' ' * 75 + '|')
    print('|' + '   Comprehensive statistical analysis of dice rolls    '.center(75) + '|')
    print('|' + '   with frequency, probability, and distribution data   '.center(75) + '|')
    print('|' + ' ' * 75 + '|')
    print('🎲 ' + '=' * 70 + ' 🎲')
    print()

def get_parameters():
    while True:
        try:
            print('🎲 Enter dice parameters:')
            sides = int(input('Number of sides per die (e.g., 6 for standard die): '))
            if sides < 2:
                print('❌ Dice must have at least 2 sides!')
                continue
                
            num_dice = int(input('Number of dice to roll simultaneously: '))
            if num_dice < 1:
                print('❌ Must roll at least 1 die!')
                continue
                
            num_rolls = input('Number of roll iterations (default 1000000): ').strip()
            if num_rolls == '':
                num_rolls = 1000000
            else:
                num_rolls = int(num_rolls)
                if num_rolls < 1000:
                    print('❌ Need at least 1000 rolls for meaningful statistics!')
                    continue
            
            return sides, num_dice, num_rolls
        except ValueError:
            print('❌ Please enter valid numbers only!')

def calculate_expected_stats(sides, num_dice):
    min_sum = num_dice
    max_sum = num_dice * sides
    expected_mean = num_dice * (sides + 1) / 2
    expected_variance = num_dice * (sides * sides - 1) / 12
    expected_std = math.sqrt(expected_variance)
    
    return min_sum, max_sum, expected_mean, expected_variance, expected_std

def perform_rolls(sides, num_dice, num_rolls):
    results = []
    print(f'\n🎯 Rolling {num_dice}d{sides} dice {num_rolls:,} times...')
    
    progress_interval = num_rolls // 20
    for i in range(num_rolls):
        if i % progress_interval == 0:
            progress = (i / num_rolls) * 100
            print(f'Progress: {progress:.0f}% ({i:,}/{num_rolls:,})', end='\r')
        
        roll_sum = sum(random.randint(1, sides) for _ in range(num_dice))
        results.append(roll_sum)
    
    print(f'Progress: 100% ({num_rolls:,}/{num_rolls:,}) ✅')
    return results

def calculate_statistics(results):
    n = len(results)
    mean = sum(results) / n
    variance = sum((x - mean) ** 2 for x in results) / n
    std_dev = math.sqrt(variance)
    
    sorted_results = sorted(results)
    median = sorted_results[n // 2] if n % 2 == 1 else (sorted_results[n // 2 - 1] + sorted_results[n // 2]) / 2
    
    q1_index = n // 4
    q3_index = 3 * n // 4
    q1 = sorted_results[q1_index]
    q3 = sorted_results[q3_index]
    iqr = q3 - q1
    
    mode_count = Counter(results)
    mode_value = mode_count.most_common(1)[0][0]
    mode_frequency = mode_count.most_common(1)[0][1]
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode_value,
        'mode_freq': mode_frequency,
        'std_dev': std_dev,
        'variance': variance,
        'q1': q1,
        'q3': q3,
        'iqr': iqr,
        'min': min(results),
        'max': max(results)
    }

def display_basic_stats(stats, expected_stats, num_rolls):
    print('\n📊 BASIC STATISTICS')
    print('=' * 50)
    print(f'Sample Size:        {num_rolls:,}')
    print(f'Minimum Roll:       {stats["min"]:>8}')
    print(f'Maximum Roll:       {stats["max"]:>8}')
    print(f'Mean (Average):     {stats["mean"]:>8.3f}  (Expected: {expected_stats[2]:.3f})')
    print(f'Median:             {stats["median"]:>8.3f}')
    print(f'Mode:               {stats["mode"]:>8}  (Frequency: {stats["mode_freq"]:,})')
    print(f'Standard Deviation: {stats["std_dev"]:>8.3f}  (Expected: {expected_stats[4]:.3f})')
    print(f'Variance:           {stats["variance"]:>8.3f}  (Expected: {expected_stats[3]:.3f})')
    print(f'Q1 (25th percentile): {stats["q1"]:>6}')
    print(f'Q3 (75th percentile): {stats["q3"]:>6}')
    print(f'IQR (Interquartile): {stats["iqr"]:>7}')

def display_frequency_analysis(results, min_sum, max_sum, num_rolls):
    print('\n📈 FREQUENCY ANALYSIS')
    print('=' * 70)
    
    frequency_count = Counter(results)
    
    print(f'{"Sum":<4} {"Frequency":<10} {"Percentage":<12} {"Expected %":<12} {"Histogram"}')
    print('-' * 70)
    
    for value in range(min_sum, max_sum + 1):
        freq = frequency_count.get(value, 0)
        percentage = (freq / num_rolls) * 100
        
        expected_freq = calculate_expected_frequency(value, min_sum, max_sum, num_rolls)
        expected_percentage = (expected_freq / num_rolls) * 100
        
        bar_length = int(percentage * 2)
        histogram = '█' * bar_length
        
        print(f'{value:<4} {freq:<10} {percentage:<12.3f} {expected_percentage:<12.3f} {histogram}')

def calculate_expected_frequency(sum_value, min_sum, max_sum, num_rolls):
    num_dice = 1
    sides = max_sum - min_sum + 1
    
    if sum_value < min_sum or sum_value > max_sum:
        return 0
    
    ways = count_ways_to_sum(sum_value, num_dice, sides)
    total_ways = sides ** num_dice
    return (ways / total_ways) * num_rolls

def count_ways_to_sum(target, num_dice, sides):
    if num_dice == 1:
        return 1 if 1 <= target <= sides else 0
    
    ways = 0
    for dice_value in range(1, sides + 1):
        ways += count_ways_to_sum(target - dice_value, num_dice - 1, sides)
    return ways

def display_distribution_analysis(results, expected_stats):
    print('\n📊 DISTRIBUTION ANALYSIS')
    print('=' * 50)
    
    mean = expected_stats[2]
    std_dev = expected_stats[4]
    
    within_1_std = sum(1 for x in results if abs(x - mean) <= std_dev)
    within_2_std = sum(1 for x in results if abs(x - mean) <= 2 * std_dev)
    within_3_std = sum(1 for x in results if abs(x - mean) <= 3 * std_dev)
    
    total = len(results)
    
    print(f'Within 1σ: {within_1_std:>8} ({within_1_std/total*100:>6.2f}%) Expected: ~68.27%')
    print(f'Within 2σ: {within_2_std:>8} ({within_2_std/total*100:>6.2f}%) Expected: ~95.45%')
    print(f'Within 3σ: {within_3_std:>8} ({within_3_std/total*100:>6.2f}%) Expected: ~99.73%')

def display_chi_square_test(results, min_sum, max_sum, num_rolls):
    print('\n🔬 CHI-SQUARE GOODNESS OF FIT TEST')
    print('=' * 50)
    
    observed = Counter(results)
    expected_per_outcome = num_rolls / (max_sum - min_sum + 1)
    
    chi_square = 0
    degrees_freedom = max_sum - min_sum
    
    for value in range(min_sum, max_sum + 1):
        obs_freq = observed.get(value, 0)
        exp_freq = expected_per_outcome
        chi_square += ((obs_freq - exp_freq) ** 2) / exp_freq
    
    print(f'Chi-square statistic: {chi_square:.6f}')
    print(f'Degrees of freedom:   {degrees_freedom}')
    
    critical_values = {0.05: 'p < 0.05', 0.01: 'p < 0.01', 0.001: 'p < 0.001'}
    print('\nInterpretation:')
    if chi_square < degrees_freedom:
        print('✅ Results appear to follow expected uniform distribution')
    else:
        print('⚠️  Results may deviate from expected uniform distribution')

def display_extreme_analysis(results):
    print('\n🎯 EXTREME VALUES ANALYSIS')
    print('=' * 50)
    
    counter = Counter(results)
    most_common = counter.most_common(5)
    least_common = counter.most_common()[:-6:-1]
    
    print('Most Frequent Results:')
    for i, (value, freq) in enumerate(most_common, 1):
        print(f'{i}. Sum {value}: {freq:,} times ({freq/len(results)*100:.3f}%)')
    
    print('\nLeast Frequent Results:')
    for i, (value, freq) in enumerate(least_common, 1):
        print(f'{i}. Sum {value}: {freq:,} times ({freq/len(results)*100:.3f}%)')

def save_results_to_file(sides, num_dice, num_rolls, results, stats, expected_stats):
    filename = f'dice_analysis_{num_dice}d{sides}_{num_rolls}rolls.txt'
    
    try:
        with open(filename, 'w') as f:
            f.write(f'DICE ROLL STATISTICAL ANALYSIS REPORT\n')
            f.write(f'{"="*50}\n')
            f.write(f'Configuration: {num_dice}d{sides}, {num_rolls:,} rolls\n')
            f.write(f'Generated on: {__import__("datetime").datetime.now()}\n\n')
            
            f.write(f'BASIC STATISTICS:\n')
            f.write(f'Mean: {stats["mean"]:.6f} (Expected: {expected_stats[2]:.6f})\n')
            f.write(f'Standard Deviation: {stats["std_dev"]:.6f} (Expected: {expected_stats[4]:.6f})\n')
            f.write(f'Variance: {stats["variance"]:.6f} (Expected: {expected_stats[3]:.6f})\n')
            f.write(f'Median: {stats["median"]:.3f}\n')
            f.write(f'Mode: {stats["mode"]} (Frequency: {stats["mode_freq"]})\n\n')
            
            f.write('RAW DATA:\n')
            for i, result in enumerate(results):
                f.write(f'{result}')
                if (i + 1) % 20 == 0:
                    f.write('\n')
                else:
                    f.write(' ')
        
        print(f'\n💾 Results saved to: {filename}')
        
    except Exception as e:
        print(f'\n❌ Error saving file: {e}')

def main():
    display_welcome()
    
    sides, num_dice, num_rolls = get_parameters()
    expected_stats = calculate_expected_stats(sides, num_dice)
    min_sum, max_sum = expected_stats[0], expected_stats[1]
    
    print(f'\n🎲 Configuration: {num_dice}d{sides} ({num_rolls:,} rolls)')
    print(f'📏 Possible sums: {min_sum} to {max_sum}')
    
    results = perform_rolls(sides, num_dice, num_rolls)
    stats = calculate_statistics(results)
    
    clear_screen()
    print('🎲 ' + '=' * 50 + ' 🎲')
    print(f'   DICE ANALYSIS RESULTS: {num_dice}d{sides}')
    print('🎲 ' + '=' * 50 + ' 🎲')
    
    display_basic_stats(stats, expected_stats, num_rolls)
    display_frequency_analysis(results, min_sum, max_sum, num_rolls)
    display_distribution_analysis(results, expected_stats)
    display_chi_square_test(results, min_sum, max_sum, num_rolls)
    display_extreme_analysis(results)
    
    print('\n' + '=' * 70)
    
    while True:
        choice = input('\nSave results to file? (y/n): ').lower().strip()
        if choice in ['y', 'yes']:
            save_results_to_file(sides, num_dice, num_rolls, results, stats, expected_stats)
            break
        elif choice in ['n', 'no']:
            break
        else:
            print('Please enter y or n.')
    
    print('\n🎯 Analysis complete! Thanks for using Dice Statistics Analyzer! 🎯')

if __name__ == '__main__':
    main()