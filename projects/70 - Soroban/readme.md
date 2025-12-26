# Soroban

A simulation of the Japanese abacus (Soroban).

## How to Use

The abacus represents numbers using beads on rods.
-   **Heaven Beads (Top)**: Value 5. Up = 0, Down (touching beam) = 5.
-   **Earth Beads (Bottom)**: Value 1. Up (touching beam) = Count, Down = 0.

### Controls

Use the keyboard to move beads up and down for each column.
-   **Top Row (q-p)**: Increase value (Move Earth beads up or Heaven bead down).
-   **Bottom Row (a-;)**: Decrease value.

| Key | `q` | `w` | `e` | `r` | `t` | `y` | `u` | `i` | `o` | `p` |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **Pos** | 10⁹ | 10⁸ | 10⁷ | 10⁶ | 10⁵ | 10⁴ | 10³ | 10² | 10¹ | 10⁰ |
| **Key** | `a` | `s` | `d` | `f` | `g` | `h` | `j` | `k` | `l` | `;` |

You can also type a full number to set the abacus directly.

## Example

Displaying `1234567890`:

```
┌───────────────────────────────┐
│ O  O  O  O  │  │  │  │  │  O │
│ │  │  │  │  O  O  O  O  O  │ │
├───────────────────────────────┤
│ │  O  O  O  O  O  O  O  O  │ │
│ O  │  O  O  │  O  O  O  O  O │
│ O  O  │  O  O  │  O  O  O  O │
│ O  O  O  │  O  O  │  O  O  O │
│ O  O  O  O  O  O  O  │  O  O │
└───────────────────────────────┘
  1  2  3  4  5  6  7  8  9  0
```
