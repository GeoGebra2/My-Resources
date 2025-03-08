import random

def generate_test_case():
    # Generate number of initial blocks
    n = random.randint(2, 100)
    
    # Generate starting addresses and sizes for each block
    starts = [random.randint(0, 10000) for _ in range(n)]
    sizes = [random.randint(1, 5000) for _ in range(n)]

    # Ensure starts are unique and sorted
    blocks = list(zip(starts, sizes))
    blocks.sort(key=lambda x: x)
    starts, sizes = zip(*blocks)

    # Generate operations
    m = random.randint(1, 50)
    ops = []
    for _ in range(m):
        op_type = random.choice([1, 2])

        if op_type == 1:  # Allocate operation
            alloc_size = random.randint(1, 500)
            ops.append(f"1 {alloc_size}")
            
        elif op_type == 2:  # Release operation
            # Make sure there was an allocation before attempting release
            if len(ops) > 0 and ops[-1].startswith("1"):
                start = random.choice(starts)
                alloc_size = random.randint(1, min(sizes))
                ops.append(f"2 {start} {alloc_size}")

    # Output test case
    print(n)
    print(' '.join(map(str, starts)))
    print(' '.join(map(str, sizes)))
    print(m)
    print('\n'.join(ops))

generate_test_case()