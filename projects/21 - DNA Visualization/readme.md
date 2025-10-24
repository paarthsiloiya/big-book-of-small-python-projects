# DNA Visualization - Animated Double Helix Display

Watch the elegant beauty of **DNA's double helix structure** come to life in your terminal! This mesmerizing animation recreates the iconic twisted ladder shape of DNA, complete with color-coded base pairs that continuously scroll and rotate to show the famous helical structure that contains the blueprint of life.

## What This Program Does

This educational animation brings molecular biology to your terminal with:

- **Animated Double Helix**: Scrolling DNA structure showing the characteristic twisted ladder shape
- **Color-Coded Bases**: Each nucleotide base (A, T, C, G) displayed in distinct colors
- **Base Pair Accuracy**: Follows Watson-Crick base pairing rules (A-T and C-G pairs)
- **Smooth Scrolling**: Continuous vertical movement creates the illusion of DNA rotation
- **Educational Value**: Perfect for learning about DNA structure and base pairing
- **Infinite Loop**: Seamless animation that runs continuously until stopped

## Visual Design

The DNA double helix is represented using ASCII art with a distinctive twisted pattern:

```
        #T---A#
         #C-G#
          #-#
         #C-G#
        #T---A#
       #C-----G#
      #C-------G#
      #A-------T#
       #G-----C#
        #C---G#
         #A-T#
          #-#
         #T-A#
        #G---C#
       #T-----A#
      #G-------C#
      #G-------C#
       #C-----G#
        #C---G#
         #G-C#
```


### Color-Coded Nucleotides

Each DNA base is displayed in its own distinctive color:
- **A (Adenine)**: `RED` - Represents purines
- **T (Thymine)**: `GREEN` - Represents pyrimidines  
- **C (Cytosine)**: `YELLOW` - Represents pyrimidines
- **G (Guanine)**: `BLUE` - Represents purines

### Base Pairing Rules

The animation follows strict biological accuracy:
- **A pairs with T**: Adenine always bonds with Thymine (2 hydrogen bonds)
- **C pairs with G**: Cytosine always bonds with Guanine (3 hydrogen bonds)
- **Random Selection**: Each frame randomly chooses valid base pairs
- **Complementary Strands**: Shows how the two DNA strands are complementary

### Base Pair Generation
```python
pairing = random.choice([('A', 'T'), ('T', 'A'), ('C', 'G'), ('G', 'C')])
# Always generates valid Watson-Crick base pairs
```

## How to Run

Launch the DNA double helix animation:

```bash
python main.py
```

The program will:
1. Display instructions and prepare the terminal
2. Clear the screen and hide the cursor for clean viewing
3. Begin the infinite DNA helix animation
4. Continue until you press `Ctrl+C` to exit
