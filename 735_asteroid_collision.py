# 735. Asteroid Collision
def asteroid_collision(asteroids):
    stack = []
    
    i = 0
    while i < len(asteroids):
        if len(stack) == 0 or stack[-1] < 0 or asteroids[i] > 0:
            stack.append(asteroids[i])
        else:
            result = abs(stack[-1]) - abs(asteroids[i])
            if result <= 0:
                stack.pop()
            if result < 0:
                i -= 1
        i += 1
    return stack

assert(asteroid_collision([-1, 3, 2, -3]) == [-1]) 
assert(asteroid_collision([5, 10, -5]) == [5,10])
assert(asteroid_collision([8, -8]) == [])        
assert(asteroid_collision([-2,-2,1,-2]) == [-2,-2,-2])