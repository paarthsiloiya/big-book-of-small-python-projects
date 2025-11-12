# Dice Roll Statistical Analyzer 🎲

A comprehensive statistical analysis tool for dice rolling simulations with detailed mathematical insights and probability theory applications.

## Features Overview

### 🎯 **Core Functionality**
- **Customizable dice configuration**: Any number of sides (2+) and multiple dice
- **Large-scale simulation**: Default 1,000,000 rolls for statistically significant results  
- **Real-time progress tracking** with percentage completion display
- **Export capabilities** to save detailed analysis reports

### 📊 **Statistical Analysis Components**

#### Basic Descriptive Statistics
- **Mean, Median, Mode** with expected vs actual comparisons
- **Standard Deviation and Variance** calculations
- **Quartiles (Q1, Q3) and Interquartile Range**
- **Min/Max values** and range analysis

#### Frequency Distribution Analysis  
- **Complete frequency table** for all possible sum outcomes
- **Percentage distributions** with visual histogram bars
- **Expected vs Observed frequencies** comparison
- **Graphical representation** using ASCII bar charts

#### Advanced Statistical Tests
- **Chi-Square Goodness of Fit Test** to verify randomness
- **Normal Distribution Analysis** with 1σ, 2σ, 3σ boundaries
- **Extreme Value Analysis** showing most/least frequent outcomes
- **Probability Theory Validation** against theoretical expectations

### 🧮 **Mathematical Foundations**

#### Probability Calculations
- **Expected mean**: `n × (sides + 1) / 2` where n = number of dice
- **Expected variance**: `n × (sides² - 1) / 12`
- **Standard deviation**: `√variance`
- **Theoretical frequency distributions** for comparison

#### Statistical Significance
- **Large sample sizes** ensure Central Limit Theorem application
- **Confidence intervals** and probability bounds
- **Distribution convergence** analysis toward normal distribution
- **Randomness quality assessment** through chi-square testing

## Usage Examples

### Basic Usage
```bash
python main.py
# Enter: 6 sides, 2 dice, 1000000 rolls
# Analyzes 2d6 distribution (sums 2-12)
```

### Advanced Configurations  
```bash
# Analyze d20 system (20-sided die)
Sides: 20, Dice: 1, Rolls: 1000000

# Analyze 3d6 character stats 
Sides: 6, Dice: 3, Rolls: 1000000

# Analyze percentile dice (d100)
Sides: 100, Dice: 1, Rolls: 1000000
```

## Output Analysis Sections

1. **Basic Statistics**: Mean, median, mode, standard deviation
2. **Frequency Analysis**: Complete distribution table with histograms  
3. **Distribution Analysis**: Normal distribution compliance testing
4. **Chi-Square Test**: Statistical significance of randomness
5. **Extreme Values**: Most and least frequent outcomes analysis
6. **File Export**: Detailed report generation for further analysis

## Applications

- **Game Design**: Balancing dice mechanics and probability curves
- **Mathematics Education**: Demonstrating probability theory and statistics
- **Quality Assurance**: Testing random number generator fairness
- **Research**: Large-scale probability simulation and analysis

Perfect for statisticians, game designers, educators, and anyone interested in probability theory!