points_new = []

def gen_bump(a, b, length):
  length *= 1/3
  
  points_new.append((
    (a[1] > b[1]) * length + -(a[1] < b[1]) * length,
    (a[1] < b[1]) * length + -(a[1] > b[1]) * length
  ))
  points_new.append(
    points_new[-1][0],
    points_new[-1][1]
  )
