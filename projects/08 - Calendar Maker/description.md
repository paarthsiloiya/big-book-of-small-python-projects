# Calendar Maker - Generate Beautiful ASCII Calendars

Transform any month and year into a **beautifully formatted ASCII calendar**! This Calendar Maker creates professional-looking monthly calendars using elegant Unicode box-drawing characters, perfect for terminal displays, text files, or anywhere you need a clean, printable calendar format.

## What This Program Does

The Calendar Maker generates **visually appealing monthly calendars** with:

- **Clean Grid Layout**: Professional box-drawing borders using Unicode characters
- **Proper Date Alignment**: Dates correctly positioned according to weekday
- **Any Month/Year**: Generate calendars for past, present, or future dates
- **Terminal-Friendly**: Designed to look perfect in any terminal or text editor
- **Accurate Calculations**: Handles leap years, month lengths, and weekday positioning automatically

### Professional Formatting
- **Centered Headers**: Month and year prominently displayed
- **Day Labels**: Full weekday names abbreviated elegantly  
- **Consistent Spacing**: Each date cell perfectly aligned
- **Zero-Padded Dates**: Single digits shown as "01", "02", etc.
- **Proper Borders**: Top, middle, and bottom borders styled appropriately

### Key Algorithms

#### Weekday Calculation
```python
first_weekday = (curr_date.weekday() + 1) % 7
```
Converts Python's weekday system to calendar layout (Sunday = 0)

#### Month Length Detection
```python
days_in_month = (next_month_first_day - timedelta(days=1)).day
```
Cleverly calculates days in any month by finding the last day

#### Border Logic
The program intelligently chooses different Unicode characters:
- **Top border**: `┌─┬─┐` (corners and tees)
- **Middle borders**: `├─┼─┤` (crosses and tees)  
- **Bottom border**: `└─┴─┘` (corners and joins)

## Example Output

**Input**: `10 2025` (October 2025)

```
                                  OCTOBER 2025
 SUNDAY   MONDAY   TUESDAY  WEDNESDAY THURSDAY  FRIDAY   SATURDAY 
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│          │          │          │    01    │    02    │    03    │    04    │
│          │          │          │          │          │          │          │
│          │          │          │          │          │          │          │
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│    05    │    06    │    07    │    08    │    09    │    10    │    11    │
│          │          │          │          │          │          │          │
│          │          │          │          │          │          │          │
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│    12    │    13    │    14    │    15    │    16    │    17    │    18    │
│          │          │          │          │          │          │          │
│          │          │          │          │          │          │          │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```