def checksum(fs):
    filesystem, mem_length = fs
    n = len(filesystem)
    k = n - 1
    check = 0
    filled = 0
    for i in range(n):

        if i >= mem_length:
            break
        if filesystem[i] == ".":
            while filesystem[k] == ".":
                k -= 1
            check += i * filesystem[k]
            k -= 1
            filled += 1
        else:
            check += i * filesystem[i]
    return check
            
            

def generate_layout(disk_map):
    n = len(disk_map)
    
    filesystem = []
    ID = 0
    for i in range(n):
        if i % 2 == 0:
            block = [ID] * disk_map[i]
            if i != n-1:
                block += ["."] * disk_map[i+1]
            ID += 1
            filesystem += block

    mem_length = len(filesystem) - sum([disk_map[i] for i in range(n) if i % 2])
    return (filesystem, mem_length)

data = [int(x) for x in open('input09').read().strip()]
print(checksum(generate_layout(data)))