# Diamonds - ASCII Art Generator

Welcome to **Diamonds**, a simple ASCII art generator that creates beautiful diamond shapes in your terminal. Choose between outlined or filled diamonds in any size you want!

## How to Use

When you run the program, you'll see a command prompt where you can create different diamond patterns:

1. **Outline Diamond**: Type `outline <size>` to create a hollow diamond (e.g., `outline 5`)
2. **Filled Diamond**: Type `filled <size>` to create a solid diamond (e.g., `filled 5`)
3. **Quit**: Type `quit` to exit the program

The size determines how many rows make up the top half of the diamond.

## Diamond Types

### Outline Diamond

An outline diamond shows just the border, creating a hollow shape:

**Example: `outline 4`**
```
   /\
  /  \
 /    \
/      \
\      /
 \    /
  \  /
   \/
```

**Example: `outline 7`**
```
      /\
     /  \
    /    \
   /      \
  /        \
 /          \
/            \
\            /
 \          /
  \        /
   \      /
    \    /
     \  /
      \/
```

### Filled Diamond

A filled diamond is completely solid, using slashes to create a dense pattern:

**Example: `filled 4`**
```
   /\
  //\\
 ///\\\
////\\\\
\\\\////
 \\\///
  \\//
   \/
```

**Example: `filled 6`**
```
     /\
    //\\
   ///\\\
  ////\\\\
 /////\\\\\
//////\\\\\\
\\\\\\//////
 \\\\\/////
  \\\\////
   \\\///
    \\//
     \/
```