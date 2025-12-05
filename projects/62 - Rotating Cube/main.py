import math, time, sys

def rotate(x, y, z, ax, ay, az):
    dy = y * math.cos(ax) - z * math.sin(ax)
    dz = y * math.sin(ax) + z * math.cos(ax)
    y, z = dy, dz

    dx = x * math.cos(ay) + z * math.sin(ay)
    dz = z * math.cos(ay) - x * math.sin(ay)
    x, z = dx, dz

    dx = x * math.cos(az) - y * math.sin(az)
    dy = x * math.sin(az) + y * math.cos(az)
    x, y = dx, dy
    
    return x, y, z

def draw_line(buffer, x0, y0, x1, y1, width, height):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        if 0 <= x0 < width and 0 <= y0 < height:
            buffer[y0][x0] = '#'
        
        if x0 == x1 and y0 == y1:
            break
            
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def main():
    width, height = 80, 24
    scale_x = width // 4
    scale_y = height // 4
    
    vertices = [[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
                [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]]
    
    edges = [(0, 1), (1, 2), (2, 3), (3, 0),
             (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7)]

    ax, ay, az = 0, 0, 0

    try:
        while True:
            buffer = [[' ' for _ in range(width)] for _ in range(height)]
            points = []

            for v in vertices:
                rx, ry, rz = rotate(v[0], v[1], v[2], ax, ay, az)
                sx = int(rx * scale_x + width / 2)
                sy = int(ry * scale_y + height / 2)
                points.append((sx, sy))

            for edge in edges:
                p1, p2 = points[edge[0]], points[edge[1]]
                draw_line(buffer, p1[0], p1[1], p2[0], p2[1], width, height)

            print('\033[H', end='')
            for row in buffer:
                print(''.join(row))

            ax += 0.05
            ay += 0.03
            az += 0.01
            time.sleep(0.05)

    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
