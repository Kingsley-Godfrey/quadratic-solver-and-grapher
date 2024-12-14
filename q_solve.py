import math
import matplotlib.pyplot as plt
import numpy as np

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

question = f"{a}x² + {b}x + {c} = 0"

discriminant = math.sqrt(((b)**2) - (4*(a)*(c)))

if discriminant < 0:
    print("no real solutions")

ans1 = ((-b) + discriminant) / (2*(a))
ans2 = ((-b) - discriminant) / (2*(a))

if ans1 == ans2:
    print(ans1)
else:
    print(ans1, ans2)

# graph code

x = np.linspace(-30, 30, 1000)

y = a * x**2 + b * x + c

plt.plot(x, y, label=f"{a}x² + {b}x + {c}", color="blue")

plt.scatter([ans1, ans2], [0,0], color='red', zorder=5, label="solutions")
plt.text(ans1, 0, f'ans 1 = {ans1:.2f}', fontsize=10, color='red', ha='left')
plt.text(ans2, 0, f'ans 2 = {ans2:.2f}', fontsize=10, color='red', ha='right')

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.title(f'Graph of {question}')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()