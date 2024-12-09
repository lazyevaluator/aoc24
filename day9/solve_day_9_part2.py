# keep memory as list of tuples (data, size) where data = -1 is empty space
disk = [(i//2 if i % 2 == 0 else - 1, int(x)) for i , x in 
        enumerate(open('input09').read().strip())]

def defragment(disk):
    k = len(disk)
    for i in range(k-1, -1, -1):
        for j in range(i):
            move_data, move_length = disk[i]
            j_data, j_length = disk[j]
            if j_data == -1 and move_data != -1 and j_length >= move_length:
                disk[i] = (-1, move_length)
                disk[j] = (-1, j_length - move_length)
                disk.insert(j, (move_data, move_length))

    return disk

def calculate_checksum(disk):
    index = 0
    checksum = 0

    for (data, length) in disk:
        if data != -1:
            checksum += data*(index*length + ((length-1) * length)//2)
        index += length
    
    return checksum
        
print(calculate_checksum(defragment(disk)))