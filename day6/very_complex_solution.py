# source:
# https://topaz.github.io/paste/#XQAAAQDjAQAAAAAAAAAjiAOiE/kRLeQB1cGmc5ba9oeiZDAK3ORrcli5DD5BboZ1jqr429N1q9OOgeMhWSwEjvKeqkEJoTjK76YWOBg103DJKNiybNNa9ao3jbB8CTyxRuVVAQSrftODkASz3Is2rURbgtX6ZT8PbzZXxzrfgrOCuC13i2tO238z05Zh8yaB6anoyRkbEMV4r51Ry7UQkzVwdPu3TpylHgNOztdP4gKy5jAA7IcbNlwpESfQH5eBxHfEEpVeZYdrV8jXeDAl3qOc1Rehw+fvcJIslqioxX7GQy2cCOQNSqkDMsA9TCiYufbrLAAsAC4YSIsAPko4w+dl+FzbJtcSh9/bUp2uEYlWTEjMQyxvh2IhiNcxjK+lCrqK5MfnZq7VVyTUGm669dvQMvJAX7jE/9wSyX4=

G = {i+j*1j: c for i,r in enumerate(open('input06'))
               for j,c in enumerate(r.strip())}

start = min(p for p in G if G[p] == '^')

def walk(G):
    pos, dir, seen = start, -1, set()
    while pos in G and (pos,dir) not in seen:
        seen |= {(pos,dir)}
        if G.get(pos+dir) == "#":
            dir *= -1j
        else: pos += dir
    return {p for p,_ in seen}, (pos,dir) in seen

path = walk(G)[0]
print(len(path),
      sum(walk(G | {o: '#'})[1] for o in path))