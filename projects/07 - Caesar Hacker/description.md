# Caesar Hacker - Breaking Ancient Codes with Modern Speed

Welcome to the world of **cryptanalysis**! While the Caesar Cipher was once used to protect military secrets, today we can crack it in seconds using the power of computation. This **Caesar Hacker** demonstrates the fundamental weakness of simple substitution ciphers through automated brute-force attacks.

## What This Program Does

The Caesar Hacker is the perfect companion to the Caesar Cipher - it's designed to **break encrypted messages** when you don't know the key. Instead of manually trying different shift values, this program systematically tests every possible key and shows you all the potential decryptions.

### The Brute Force Approach

Since Caesar ciphers only have a limited number of possible keys (95 in this implementation), we can simply:

1. **Try Every Key**: Test all possible shift values from 0 to 94
2. **Decrypt with Each**: Apply each key to the encrypted message
3. **Display Results**: Show all possible decryptions for human analysis
4. **Find the Winner**: Look for the result that makes sense in your language

## How It Works

### The Algorithm
```python
for key in range(95):  # Try all possible keys
    decrypt_message_with_key(key)
    display_result()
```

### Character Set Coverage
Just like the Caesar Cipher, this hacker works with **95 characters**:
- **Letters**: A-Z, a-z (case-sensitive)
- **Numbers**: 0-9  
- **Punctuation**: .,!? and many more
- **Symbols**: #$%&'()*+-/<=>@[]^_`{|}~

### The Process
For each potential key, the program:
1. Takes each character in the encrypted message
2. Finds its position in the symbol set
3. Shifts it backward by the key amount: `(position - key) % 95`
4. Outputs the resulting character
5. Displays the complete attempted decryption

## Example: Cracking a Message

Let's say you intercepted this encrypted message: **"Vw>HvsFs/>?ooFHv>$wzCwMo>HvwG>Gwrs"**

The Caesar Hacker will output something like:

```
Key 0: Vw>HvsFs/>?ooFHv>$wzCwMo>HvwG>Gwrs
Key 1: Uv=GurEr.>=nnnEGu=#vzBvLn=GuvF=Fvqr  
Key 2: Tu<FtqDq-><mmmDFt<"uyAuKm<FtuE<Eupq
...
Key 13: Hello! Caesar Cipher Cracking This Code
...
Key 94: Xz@JzuGu1@AAqqHJz@&{|E{Oq@Jz{I@I{tu
```

**Bingo!** Key 13 reveals the readable message: **"Hello! Caesar Cipher Cracking This Code"**

## Why Brute Force Works Here

### Limited Key Space
- **Only 95 possibilities**: Unlike modern encryption with trillions of keys
- **Instant testing**: Each key takes milliseconds to test
- **Complete coverage**: Guaranteed to find the correct key
- **No special knowledge needed**: Just computational power

### Computational Advantage  
What might take hours to do by hand takes seconds on a computer:
- **Speed**: Test all 95 keys in under a second
- **Accuracy**: No human error in shift calculations  
- **Completeness**: Never miss a potential solution
- **Patience**: Computer doesn't get tired or bored