# Caesar Cipher - Ancient Cryptography Made Simple

Step into the world of **cryptography** with one of history's most famous encryption techniques! The **Caesar Cipher**, named after Julius Caesar who used it to protect his military communications, is a simple yet effective method of encoding messages by shifting letters in the alphabet.

## What is a Caesar Cipher?

A Caesar Cipher is a **substitution cipher** where each character in your message is shifted by a fixed number of positions in a predetermined character set. It's like having a secret decoder ring - if you know the shift amount (the "key"), you can easily encrypt and decrypt messages.

## How This Program Works

This implementation goes beyond the basic alphabet-only Caesar cipher:

### Extended Character Set
Unlike traditional versions that only handle A-Z, this program encrypts **95 different characters**:
- **Letters**: A-Z and a-z (uppercase and lowercase)
- **Numbers**: 0-9
- **Punctuation**: All common symbols like .,!? #$%&'()*+-/<=>@[]^_`{|}~
- **Special Characters**: Quotes, backslashes, and more

### Encryption Process
1. **Choose Mode**: Encrypt a new message or decrypt an existing one
2. **Select Key**: Pick a shift value between 1 and 94
3. **Enter Message**: Type any text using the supported characters
4. **Get Result**: Receive your encrypted or decrypted message instantly

### The Math Behind It
For each character, the program:
1. Finds the character's position in the symbol set
2. **Encrypts**: `(position + key) % 95` → shifts forward
3. **Decrypts**: `(position - key) % 95` → shifts backward
4. Uses modulo arithmetic to "wrap around" when reaching the end

## Example Walkthrough

Let's encrypt the message **"Hello World!"** with a key of **13**:

```
Original:  H e l l o   W o r l d !
Positions: 7 30 37 37 40 26 22 40 43 37 29 2
+ Key 13:  20 43 50 50 53 39 35 53 56 50 42 15
Result:    U r y y z - b z } y s ?
```

**Encrypted message**: `"Uryyb-bz}ys?"`

To decrypt, we simply reverse the process using the same key!

## Try It Yourself

### Basic Example
```
Mode: (e)ncrypt
Key: 5
Message: "Meet me at midnight"
Result: "Rjjy rj fy rnistnlmy"
```

### Decrypt the Message
```
Mode: (d)ecrypt  
Key: 5
Message: "Rjjy rj fy rnistnlmy"
Result: "Meet me at midnight"
```

## Breaking the Code

Want to crack a Caesar cipher without knowing the key?  
[07 - Caesar Hacker](<../07 - Caesar Hacker>)

*Remember: Never use Caesar ciphers for actually sensitive information - they're easily broken. But for learning, games, and fun, they're perfect!*