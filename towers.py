import random

tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16,tower17,tower18,tower19,tower20,tower21,tower22,tower23,tower24 = '❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓',
a = random.randint(1, 3)
b = random.randint(4, 7)
c = random.randint(8, 11)
d = random.randint(12, 15)
e = random.randint(16, 19)
f = random.randint(20, 23)
if a == 1:
  tower1 = "✅"
elif a == 2:
  tower2 = "✅"
elif a == 3:
  tower3 = "✅"
if b == 4:
  tower4 = "✅"
elif b == 5:
  tower5 = "✅"
elif b == 6:
  tower6 = "✅"
elif b == 7:
  tower7 = "✅"
if c == 8:
  tower8 = "✅"
elif c == 9:
  tower9 = "✅"
elif c == 10:
  tower10 = "✅"
elif c == 11:
  tower11 = "✅"
if d == 12:
  tower12 = "✅"
elif d == 13:
  tower13 = "✅"
elif d == 14:
  tower14 = "✅"
elif d == 15:
  tower15 = "✅"
if e == 16:
  tower16 = "✅"
elif e == 17:
  tower17 = "✅"
elif e == 18:
  tower18 = "✅"
elif e == 19:
  tower19 = "✅"
if f == 20:
  tower20 = "✅"
elif f == 21:
  tower21 = "✅"
elif f == 22:
  tower22 = "✅"
elif f == 23:
  tower23 = "✅"
elif f == 24:
  tower24 = "✅"

row1 = tower1 + tower2 + tower3
row2 = tower4 + tower5 + tower6
row3 = tower7 + tower8 + tower9
row4 = tower10 + tower11 + tower12
row5 = tower13 + tower14 + tower15
row6 = tower16 + tower17 + tower18
row7 = tower19 + tower20 + tower21
row8 = tower22 + tower23 + tower24
print(row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7 + "\n" + row8)
