t = int(input())

# Process each scenario
for _ in range(t):
    r, u, l, d, k = map(int, input().split())

    mr = min(r, l)
    nr = max(r, l)
    mu = min(u, d)
    nu = max(u, d)

    if mr <= mu:
        com_km = min(mr, k)
        mr -= com_km
        k -= com_km
        nu += com_km

        if k > 0:
            com_km = min(mu, k)
            mu -= com_km
            k -= com_km
            nr += com_km

    else:
        com_km = min(mu, k)
        mu -= com_km
        k -= com_km
        nr += com_km

        if k > 0:
            com_km = min(mr, k)
            mr -= com_km
            k -= com_km
            nu += com_km

    if k > 0:
        kmn = min(nu, nr)
        knn = max(nu, nr)

        com_kmn = min(kmn, k)
        knn += com_kmn
        nu = knn
        kmn -= com_kmn
        nr = kmn

    print(int(((nr - mr) ** 2) + ((nu - mu) ** 2)))
