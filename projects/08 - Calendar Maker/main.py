import datetime

DAYS = ("SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY")
MONTHS = (
    "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE",
    "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"
)

def renderCalendar(month, year):
    BLANK_LINE = "│          " * 7 + "│\n"
    cal = ""
    cal += " " * 34 + f"{MONTHS[month - 1]} {year}\n"
    cal += "".join([f"{day:.^11.3}" for day in DAYS]) + "\n"

    curr_date = datetime.date(year, month, 1)

    first_weekday = (curr_date.weekday() + 1) % 7
    days_in_month = (datetime.date(year + (month // 12), (month % 12) + 1, 1) - datetime.timedelta(days=1)).day

    day_counter = 1
    week_count = 0
    
    while day_counter <= days_in_month:
        # Top border
        if week_count == 0:
            # First week - use top tees and corners
            cal += "┌──────────" + "┬──────────" * 6 + "┐\n"
        else:
            # Subsequent weeks - use crosses and tees
            cal += "├──────────" + "┼──────────" * 6 + "┤\n"
        
        for line in range(3):
            if line == 0:
                cal += BLANK_LINE
            elif line == 1:
                week_line = "│"
                for wd in range(7):
                    if (day_counter == 1 and wd < first_weekday) or day_counter > days_in_month:
                        week_line += "          │"
                    else:
                        week_line += f"    {day_counter:02d}    │"
                        day_counter += 1
                cal += week_line + "\n"
            elif line == 2:
                cal += BLANK_LINE
        
        # Check if this is the last week
        if day_counter > days_in_month:
            # Last week - use bottom tees and corners
            cal += "└──────────" + "┴──────────" * 6 + "┘\n"
        
        week_count += 1
    
    return cal


while True:
    user_input = input("Enter a date (MM YYYY) or 'q' to quit: ")
    if user_input.lower() == 'q':
        break

    try:
        month, year = map(int, user_input.split())
        break
    except ValueError:
        print("Invalid date format. Please enter the date as MM YYYY.")
        continue

print(renderCalendar(month, year))