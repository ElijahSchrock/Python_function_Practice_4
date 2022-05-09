def max_num(a, b, c):
    return max([a, b, c])


print(
    max_num(
        1,
        4,
        7,
    )
)


def mult_list(list):
    if len(list) == 0:
        return 0
    result = list[0]

    if len(list) > 1:
        for i in list[1:]:
            result = result * i
    return result


print(mult_list([10, 2, 3]))


def rev_string(string):
    return string[::-1]


print(rev_string("dog"))


def num_within(stp, a, b):
    return stp in range(a, b + 1)

print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

def is_vowel(letter):
  vowels = ['a', 'e', 'i', 'o', 'u']
  if letter in vowels:
    return True
  else:
    return False

print(list(filter(is_vowel, ['g', 'i', 'a', 'c'])))

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(7)