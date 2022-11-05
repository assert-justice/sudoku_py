# Given a board of width w and height h
# You have a piece at the top left corner
# This piece can only move one cell down OR right
# How many different routes can the piece take from the top left to the bottom right of the grid?

def solve(w, h):
    if w == 1 or h == 1:
        return 1
    return solve(w - 1, h) + solve(w, h - 1)

# ddrr
# drdr

def paths(w, h):
    if w == 1:
        return [(h-1) * 'd']
    if h == 1:
        return [(w-1) * 'r']
    routes = []
    for route in paths(w, h-1):
        routes.append('d' + route)
    for route in paths(w-1, h):
        routes.append('r' + route)
    return routes

print(paths(10,10))