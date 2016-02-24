import time

def lattice_path(grid_size):
  if grid_size == [0, 0]:
    return 1
  paths = 0
  if grid_size[0] > 0:
    print grid_size
    paths += lattice_path([grid_size[0] - 1, grid_size[1]])
  if grid_size[1] > 0:
    print grid_size
    paths += lattice_path([grid_size[0], grid_size[1] - 1])
  return paths


def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        # print "i is " + str(i)
        for j in range(i):
            # print "j is " + str(j)
            L[j] = L[j]+L[j-1]
            print "j is %s and L[j] is %s" % (j, L[j])
        L[i] = 2 * L[i - 1]
        print "i is %s and L[i] is %s" % (i, L[i])
    return L[cube_size - 1]

if __name__ == '__main__':
  # print lattice_path([2, 2])
  start = time.time()
  n = route_num(4)
  elapsed = (time.time() - start)
  print "%s found in %s seconds" % (n,elapsed)
