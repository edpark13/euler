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

if __name__ == '__main__':
  print lattice_path([2, 2])
