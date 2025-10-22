# Bitmap Message - Turn Text into ASCII Shapes

The **Bitmap Message** program takes any text you enter and "prints" it into the shape of a bitmap image. The bitmap is made of characters where spaces represent holes and any other character represents filled areas. Your message is repeated across the filled areas, creating a fun text-based picture.

## What This Program Does

- Prompts you for a message (any text).
- Reads a built-in ASCII bitmap (a multi-line string).
- For each non-space character in the bitmap, it prints the next character of your message (looping when it reaches the end).
- For each space in the bitmap, it prints a space (leaving the hole).

The result is a piece of ASCII art where your message forms the visible shape.

## How It Works (At a Glance)

1. Store a multi-line bitmap string (for example, a world map outline).
2. Ask the user for a message. If the message is empty, the program exits.
3. Iterate over each line and character in the bitmap.
4. If the current character is a space, print a space. Otherwise, print the next character of the message, wrapping around when needed.

This simple mapping of message characters onto the bitmap makes it easy to swap in different shapes or messages.

## Small Example

Given this tiny bitmap shape:

```
	**  
 **** 
******
 **** 
	**  
```

and the message `HELLO`, the output would repeat `HELLO` over each `*` while keeping spaces intact:

```
	HE  
 LLOH 
ELLOHE
 LLOH 
	EL  
```

## Try It

1. Run the program.
2. When prompted, type a message (e.g., your name, a quote, or emojis!).
3. See your text rendered in the ASCII shape.

You can customize the bitmap by editing the built-in multi-line string—swap the shape for your own design (keep spaces where you want holes).

## Ideas to Explore

- Swap in different bitmaps (hearts, logos, initials, etc.).
- Randomize the starting position in the message for varied results.
- Add color in the terminal (if supported) for more flair.
- Read the message from a file or command-line argument.
- Export the result to a text file.

Turn any shape into a playful text poster with just a few lines of Python!

