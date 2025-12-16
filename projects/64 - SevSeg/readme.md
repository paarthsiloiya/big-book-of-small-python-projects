# SevSeg - Seven Segment Display

A simple Python module to render numbers and hexadecimal characters in a seven-segment display style. This is an improved version supporting 0-9, A-F, decimal points, and negative signs.

## Usage

You can run the program directly to test it:

```bash
python main.py
```

Or import it into your own projects:

```python
import main
print(main.get_sev_seg_str('A1.5'))
```

## Features

-   Supports digits `0-9`
-   Supports Hex characters `A-F` (and `b`, `d`)
-   Supports decimal points `.` and negative signs `-`
-   Zero padding support

### Example Output

Input: `42`

```text
      __ 
|__|  __|
   | |__ 
```

Input: `Ab`

```text
 __       
|__| |__  
|  | |__| 
```
