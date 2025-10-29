"""
Fish Tank Aquarium Simulation
A beautiful ASCII art aquarium with moving fish, seaweed, and bubbles.
Uses the bext library for colorful terminal graphics.
"""

import bext
import random
import time
import sys

# Helper function to safely get colors
def safe_color(color_func):
    """Safely get color codes, return empty string if not supported"""
    try:
        result = color_func()
        return result if result is not None else ''
    except:
        return ''

# Colors for different elements
FISH_COLORS = [safe_color(lambda: bext.fg('yellow')), 
               safe_color(lambda: bext.fg('cyan')), 
               safe_color(lambda: bext.fg('magenta')), 
               safe_color(lambda: bext.fg('red'))]
SEAWEED_COLOR = safe_color(lambda: bext.fg('green'))
BUBBLE_COLOR = safe_color(lambda: bext.fg('white'))
WATER_COLOR = safe_color(lambda: bext.bg('blue'))

class Fish:
    def __init__(self, x, y, size='small', direction=1):
        self.x = x
        self.y = y
        self.size = size
        self.direction = direction  # 1 for right, -1 for left
        self.color = random.choice(FISH_COLORS)
        self.bubble_timer = random.randint(50, 150)  # Random bubble generation
        
    def get_sprite(self):
        if self.size == 'small':
            if self.direction == 1:  # Moving right
                return '><(((°>'
            else:  # Moving left
                return '<°)))><'
        else:  # big fish
            if self.direction == 1:  # Moving right
                return '><((((((°>'
            else:  # Moving left
                return '<°))))))><'
    
    def move(self, width, height):
        # Move horizontally
        speed = 1 if self.size == 'small' else 1
        new_x = self.x + self.direction * speed
        
        # Get sprite width for current direction
        sprite_width = len(self.get_sprite())
        
        # Check boundaries and change direction if needed
        if new_x <= 1:
            self.direction = 1
            self.x = 2
        elif new_x >= width - sprite_width - 1:
            self.direction = -1
            self.x = width - sprite_width - 2
        else:
            self.x = new_x
        
        # Slight vertical movement for more natural swimming
        if random.randint(1, 15) == 1:  # Less frequent vertical movement
            self.y += random.choice([-1, 0, 1])
            self.y = max(2, min(height - 3, self.y))
    
    def should_bubble(self):
        self.bubble_timer -= 1
        if self.bubble_timer <= 0:
            self.bubble_timer = random.randint(100, 200)
            return True
        return False

class Seaweed:
    def __init__(self, x, bottom_y, height):
        self.x = x
        self.bottom_y = bottom_y
        self.height = height
        self.sway_offset = 0
        self.sway_direction = random.choice([-1, 1])
        
    def get_sprite(self, segment):
        # Different seaweed segments for animation
        sway_chars = ['|', '/', '\\', '|']
        return sway_chars[segment % len(sway_chars)]
    
    def update_sway(self):
        self.sway_offset += self.sway_direction * 0.5
        if abs(self.sway_offset) > 2:
            self.sway_direction *= -1

class Bubble:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = random.choice(['o', 'O', '°'])
        
    def move(self):
        self.y -= 1
        # Slight horizontal drift
        if random.randint(1, 3) == 1:
            self.x += random.choice([-1, 0, 1])

class Aquarium:
    def __init__(self):
        self.width = bext.width()
        self.height = bext.height()
        self.fish_list = []
        self.seaweed_list = []
        self.bubbles = []
        self.previous_positions = {}  # Track previous positions to clear them
        
        # Create fish
        for _ in range(random.randint(3, 6)):
            x = random.randint(1, self.width - 10)
            y = random.randint(3, self.height - 4)
            size = random.choice(['small', 'small', 'big'])  # More small fish
            direction = random.choice([1, -1])
            self.fish_list.append(Fish(x, y, size, direction))
        
        # Create seaweed
        for _ in range(random.randint(4, 8)):
            x = random.randint(1, self.width - 2)
            height = random.randint(3, min(8, self.height - 5))
            self.seaweed_list.append(Seaweed(x, self.height - 2, height))
    
    def draw_border(self):
        border_color = safe_color(lambda: bext.fg('blue'))
        # Top border
        bext.goto(0, 0)
        print(border_color + '═' * self.width)
        
        # Bottom border
        bext.goto(0, self.height - 1)
        print(border_color + '═' * self.width)
        
        # Side borders
        for y in range(1, self.height - 1):
            bext.goto(0, y)
            print(border_color + '║')
            bext.goto(self.width - 1, y)
            print(border_color + '║')
    
    def draw_seaweed(self):
        for j, seaweed in enumerate(self.seaweed_list):
            # Clear previous seaweed positions
            seaweed_id = f"seaweed_{j}"
            if seaweed_id in self.previous_positions:
                old_positions = self.previous_positions[seaweed_id]
                for old_x, old_y in old_positions:
                    if 1 <= old_x < self.width - 1 and 1 <= old_y < self.height - 1:
                        bext.goto(old_x, old_y)
                        print(' ')
            
            seaweed.update_sway()
            current_positions = []
            
            for i in range(seaweed.height):
                y = seaweed.bottom_y - i
                x = seaweed.x + int(seaweed.sway_offset * (i / seaweed.height))
                x = max(1, min(self.width - 2, x))
                
                if 1 <= y < self.height - 1:
                    current_positions.append((x, y))
                    bext.goto(x, y)
                    print(SEAWEED_COLOR + seaweed.get_sprite(i))
            
            # Store current positions for next frame
            self.previous_positions[seaweed_id] = current_positions
    
    def clear_previous_positions(self):
        """Clear previous positions to reduce flickering"""
        for obj_id, (old_x, old_y, old_sprite) in self.previous_positions.items():
            # Clear old position by overwriting with spaces
            if 1 <= old_x < self.width - 1 and 1 <= old_y < self.height - 1:
                bext.goto(old_x, old_y)
                print(' ' * len(old_sprite))
    
    def draw_fish(self):
        # Clear previous fish positions
        for i, fish in enumerate(self.fish_list):
            fish_id = f"fish_{i}"
            if fish_id in self.previous_positions:
                old_x, old_y, old_sprite = self.previous_positions[fish_id]
                if 1 <= old_x < self.width - 1 and 1 <= old_y < self.height - 1:
                    bext.goto(old_x, old_y)
                    print(' ' * len(old_sprite))
        
        # Move and draw fish
        for i, fish in enumerate(self.fish_list):
            fish.move(self.width, self.height)
            sprite = fish.get_sprite()
            
            # Store current position for next frame clearing
            fish_id = f"fish_{i}"
            self.previous_positions[fish_id] = (int(fish.x), int(fish.y), sprite)
            
            # Draw fish
            bext.goto(int(fish.x), int(fish.y))
            print(fish.color + sprite)
            
            # Generate bubbles
            if fish.should_bubble() and random.randint(1, 8) == 1:
                bubble_x = int(fish.x + len(sprite) // 2)
                bubble_y = int(fish.y - 1)
                if bubble_y > 1:
                    self.bubbles.append(Bubble(bubble_x, bubble_y))
    
    def draw_bubbles(self):
        # Clear previous bubble positions and update bubbles
        bubbles_to_remove = []
        for i, bubble in enumerate(self.bubbles):
            bubble_id = f"bubble_{i}"
            
            # Clear previous position
            if bubble_id in self.previous_positions:
                old_x, old_y, _ = self.previous_positions[bubble_id]
                if 1 <= old_x < self.width - 1 and 1 <= old_y < self.height - 1:
                    bext.goto(old_x, old_y)
                    print(' ')
            
            # Move bubble
            bubble.move()
            
            # Check if bubble should be removed
            if bubble.y <= 1 or bubble.x <= 0 or bubble.x >= self.width - 1:
                bubbles_to_remove.append(bubble)
            else:
                # Store position for next frame
                self.previous_positions[bubble_id] = (bubble.x, bubble.y, bubble.char)
                
                # Draw bubble
                bext.goto(bubble.x, bubble.y)
                print(BUBBLE_COLOR + bubble.char)
        
        # Remove bubbles that went off screen
        for bubble in bubbles_to_remove:
            self.bubbles.remove(bubble)
    
    def run(self):
        bext.clear()
        bext.hide_cursor()
        
        try:
            print(safe_color(lambda: bext.fg('white')) + "Press Ctrl+C to exit...")
            time.sleep(1)
            
            # Initial draw - only clear once at the start
            bext.clear()
            self.draw_border()
            self.draw_seaweed()
            
            frame_count = 0
            while True:
                # Only redraw moving elements, not the entire screen
                self.draw_fish()
                self.draw_bubbles()
                
                # Redraw seaweed occasionally for swaying effect
                if frame_count % 10 == 0:
                    self.draw_seaweed()
                
                # Add some water effects (occasional ripples)
                if random.randint(1, 100) == 1:
                    x = random.randint(2, self.width - 3)
                    y = random.randint(2, 4)
                    bext.goto(x, y)
                    print(safe_color(lambda: bext.fg('cyan')) + '~')
                    # Clear the ripple after a moment
                    time.sleep(0.02)
                    bext.goto(x, y)
                    print(' ')
                
                frame_count += 1
                time.sleep(0.15)  # Slightly slower for smoother movement
                
        except KeyboardInterrupt:
            bext.clear()
            bext.show_cursor()
            print(safe_color(lambda: bext.fg('yellow')) + "\n🐠 Thanks for visiting the aquarium! 🐠")
            sys.exit()

def main():
    """Main function to run the aquarium simulation."""
    print(safe_color(lambda: bext.fg('cyan')) + "Initializing aquarium...")
    print(f"Terminal size: {bext.width()} x {bext.height()}")
    
    if bext.width() < 40 or bext.height() < 15:
        print(safe_color(lambda: bext.fg('red')) + "Terminal too small! Please resize to at least 40x15")
        return
    
    aquarium = Aquarium()
    aquarium.run()

if __name__ == '__main__':
    main()