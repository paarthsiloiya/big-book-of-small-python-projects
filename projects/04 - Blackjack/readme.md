# Blackjack - Beat the Dealer at 21

Welcome to **Blackjack**, the classic casino card game where your goal is simple: get as close to 21 as possible without going over, and beat the dealer's hand. This terminal-based version features beautiful ASCII card graphics, realistic casino rules, and a betting system that lets you manage your bankroll.

## How to Play

1. **Place Your Bet**: Start with $400 and place bets between $2 and $1000.
2. **Get Your Cards**: You and the dealer each receive two cards. Your cards are face up, but one of the dealer's cards remains hidden.
3. **Make Your Move**: Choose to hit (take another card), stand (keep your current hand), or double down (double your bet and take exactly one more card).
4. **Beat the Dealer**: Get closer to 21 than the dealer without busting (going over 21).

## Card Values

- **Number cards (2-10)**: Face value
- **Face cards (J, Q, K)**: Worth 10 points each
- **Aces**: Worth 11 points, but automatically count as 1 if needed to prevent busting

## Game Features

### Visual Card Display
Cards are rendered with beautiful ASCII art that displays side by side:
```
┌─────────┐ ┌─────────┐
│A        │ │K        │
│         │ │         │
│    ♠    │ │    ♥    │
│         │ │         │
│        A│ │        K│
└─────────┘ └─────────┘
```

### Smart Ace Handling
The game automatically adjusts Ace values to prevent unnecessary busting. If you have an Ace counting as 11 and would bust, it automatically becomes worth 1 point.

### Realistic Casino Rules
- **Blackjack Bonus**: Natural 21 (Ace + 10-value card) pays 3:2 instead of 1:1
- **Dealer Rules**: Dealer must hit on 16 and stand on 17
- **Double Down**: Double your bet and receive exactly one more card
- **Multiple Decks**: Uses 6 decks shuffled together, just like real casinos

### Betting System
- Start with $400
- Minimum bet: $2
- Maximum bet: $1000 (or your current balance)
- Game ends when you can't afford the minimum bet

## Strategy Tips

- **Basic Strategy**: Hit if your hand is 11 or less (you can't bust)
- **Soft Hands**: Hands with Aces are "soft" - be more aggressive since Aces can change value
- **Double Down**: Best used on hands totaling 9, 10, or 11
- **Watch the Dealer**: If dealer shows a weak card (2-6), they're more likely to bust

## Example Game Flow

```
Current balance: $400
Enter your bet ($2-$1000): 50

Dealer's hand:
┌─────────┐ ┌─────────┐
│7        │ │?        │
│         │ │         │
│    ♦    │ │    ?    │
│         │ │         │
│        7│ │        ?│
└─────────┘ └─────────┘
Dealer's hand value: ?

Your hand:
┌─────────┐ ┌─────────┐
│10       │ │5        │
│         │ │         │
│    ♣    │ │    ♠    │
│         │ │         │
│       10│ │        5│
└─────────┘ └─────────┘
Your hand value: 15

Do you want to (h)it, (s)tand or (d)ouble down?
```