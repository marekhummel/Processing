window_size = 750
max_n = 1000  # max 300000
runtime = 3
plot_random = False

back_color = color(10)
one_color = color(0, 127, 255)
composite_color = back_color # color(255)
prime_color = color(255) # color(255, 0, 0)

updates_per_draw = max_n // 50
sz = window_size // (int(sqrt(max_n)) + 2)
n_info = []


def prime_sieve(n):
    ''' Sieve of Eratostenes up to n'''
    root = int(sqrt(n))
    primes = [True] * (n + 1)
    primes[0:2] = [False, False]
    for i in range(2, root + 1):
        if primes[i]:
            m = (n // i - i + 1)
            primes[i*i: n+1: i] = [False] * m

    return (i for i, p in enumerate(primes) if p)


def setup():
    global n_info

    size(window_size, window_size)
    background(back_color)

    # Get coordinates for each cell
    primes = set(prime_sieve(max_n))
    i, j = 0, 0
    steplen = 1
    step = 0
    inc = False
    dir = 0
    for n in range(1, max_n + 1):
        # Set info
        pred = n in primes if not plot_random else random(1) < float(len(primes)) / max_n
        n_info.append((n, i, j, pred))

        # Update coordinates depending on direction
        if dir == 0:
            i += 1
        elif dir == 90:
            j -= 1
        elif dir == 180:
            i -= 1
        elif dir == 270:
            j += 1

        # Increase step in current line of the sprial
        step += 1
        if step == steplen:
            # Line end, update direction and line length if needed
            if inc:  # Only update line length every two updates
                steplen += 1
            inc = not inc
            step = 0
            dir = (dir + 90) % 360

    # Set framerate to match runtime
    frame_rate(max_n // (runtime * updates_per_draw))


def draw():
    # Draw one in center
    translate(width / 2, height / 2)

    for _ in range(updates_per_draw):
        # Abort if last n has been drawn
        if not n_info:
            no_loop()
            return

        # Fetch current n
        n, i, j, is_prime = n_info.pop(0)
        x, y = i * sz, j * sz
        used_color = prime_color if is_prime else (one_color if n == 1 else composite_color)

        if (sz // 2 > 1):
            fill(used_color)
            no_stroke()
            circle(x, y, sz // 2)
        else:
            noFill()
            stroke(used_color)
            point(x, y)

        # textAlign(CENTER, CENTER)
        # fill(back_color)
        # noStroke()
        # text(n, x, y)
