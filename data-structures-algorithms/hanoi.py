# Towers of Hanoi puzzl
def hanoi(n, source, target, auxiliary):
    if n > 0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        hanoi(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target
        print('Move disk %s from peg %s to peg %s' % (n, source, target))

        # Move the n - 1 disks that we left on auxiliary to target
        hanoi(n - 1, auxiliary, target, source)


# Initiate call from source peg to target peg with auxiliary peg:
num_disks = 4
source_rod = 'A'
auxiliar_rod = 'B'
target_rod = 'C'
hanoi(num_disks, source_rod, target_rod, auxiliar_rod)
