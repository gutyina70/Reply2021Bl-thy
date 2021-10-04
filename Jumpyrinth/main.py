with open('2c464e58-9121-11e9-aec5-34415dec71f2.txt') as f:
  map = f.readlines()

stack = []
flags = []


def read_number(i, j, direction):
  num = ''
  while True:
    if direction == 'left':
      j -= 1
    elif direction == 'right':
      j += 1
    elif direction == 'up':
      i -= 1
    elif direction == 'down':
      i += 1
    try:
      num += str(int(map[i][j]))
    except ValueError:
      break
  num = int(num)
  return num


def solve_from(i, j):
  flag = ''
  while True:
    tile = map[i][j]
    if tile == 'X':
      break

    elif tile == '@':  # End of the path, check the FLAG string. ;)
      flags.append(flag + '\n')
      break

    elif tile == '#':  # Do nothing.
      pass

    elif tile == '(':  # Pop from the STACK and prepend the char to the FLAG string, then jump to the left by the number of chars specified on the right.
      # (1) Pop from the STACK and prepend the char to the FLAG string.
      char = stack.pop()
      flag = char + flag
      # (2) Read this number
      num = read_number(i, j, 'right')
      # (3) Then jump here.
      j -= num

    elif tile == ')':  # Pop from the STACK and append the char to the FLAG string, then jump to the right by the number of chars specified on the left.
      # (1) Pop from the STACK and append the char to the FLAG string.
      char = stack.pop()
      flag = flag + char
      # (2) Read this number.
      num = read_number(i, j, 'left')
      # (3) Then jump here.
      j += num

    elif tile == '-':  # Remove the first char of the FLAG string, then jump above by the number of chars specified below.
      # (1) Remove the first char of the FLAG string.
      flag = flag[1:]
      # (2) Read this number.
      num = read_number(i, j, 'down')
      # (3) Then jump here.
      i -= num

    elif tile == '+':  # Remove the last char of the FLAG string, then jump below by the number of chars specified above.
      # (1) Remove the last char of the FLAG string.
      flag = flag[:-1]
      # (2) Read this number.
      num = read_number(i, j, 'up')
      # (3) Then jump here.
      i += num

    elif tile == '%':  # Reverse the FLAG string, then move down of one position.
      # (1) Reverse the FLAG string.
      flag = flag[::-1]
      # (2) Then move here.
      i += 1

    elif tile == '[':  # Read the char to the right, push it into the STACK, than jump to the char at the right of it.
      # (1) Read this char and push it into the STACK.
      j += 1
      char = map[i][j]
      stack.append(char)
      # (2) Then jump here.
      j += 1

    elif tile == ']':  # Read the char to the left, push it into the STACK, than jump to the char at the left of it.
      # (1) Read this char and push it into the STACK.
      j -= 1
      char = map[i][j]
      stack.append(char)
      # (2) Then jump here.
      j -= 1

    elif tile == '*':  # Read the char above it, push it into the STACK, than jump to the char above of that char.
      # (1) Read this char and push it into the STACK.
      i -= 1
      char = map[i][j]
      stack.append(char)
      # (2) Then jump here.
      i -= 1

    elif tile == '.':  # Read the char below it, push it into the STACK, than jump to the char below of that char.
      # (1) Read this char and push it into the STACK.
      i += 1
      char = map[i][j]
      stack.append(char)
      # (2) Then jump here.
      i += 1

    elif tile == '<':  # Jump to the left by the number of chars specified on the right.
      # (1) Read this number.
      num = read_number(i, j, 'right')
      # (2) Then jump here.
      j -= num

    elif tile == '>':  # Jump to the right by the number of chars specified on the left.
      # (1) Read this number.
      num = read_number(i, j, 'left')
      # (2) Then jump here.
      j += num

    elif tile == '^':  # Jump above by the number of chars specified below.
      # (1) Read this number.
      num = read_number(i, j, 'down')
      # (2) Then jump here.
      i -= num

    elif tile == 'v':  # Jump below by the number of chars specified above.
      # (1) Read this number.
      num = read_number(i, j, 'up')
      # (2) Then jump here.
      i += num


def main():
  for i, line in enumerate(map):
    for j, char in enumerate(line):
      if char == '$':
        solve_from(i + 1, j)

  # find the only real flag
  filtered = filter(lambda x: '{FLG:' in x, flags)
  flag: str = list(filtered)[0]
  print(flag)


main()
