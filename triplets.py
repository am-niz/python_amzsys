def triplets(n):
    triplets = []
    for a in range(1, n):
        for b in range(a, n):
            c = a + b
            if c < n:
                triplets.append((a,b,c))
            else:
                break
    print(triplets)

triplets(5)