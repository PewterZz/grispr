s1 = [
    -0.3333333333333333,
    -1.0,
    1.6666666666666667,
    2.0,
    3.6666666666666665,
    4.0,
    3.3333333333333335,
    2.6666666666666665,
    2.3333333333333335,
]
s2 = [
    -0.3333333333333333,
    -1.0,
    1.6666666666666667,
    2.0,
    3.6666666666666665,
    4.0,
    3.3333333333333335,
    2.6666666666666665,
    2.3333333333333335,
]
s3 = [
    -1.3333333333333333,
    -0.6666666666666666,
    -0.3333333333333333,
    -0.6666666666666666,
    -0.3333333333333333,
    -0.3333333333333333,
    0.0,
    0.0,
    0.0,
]
s4 = [
    -3.3333333333333335,
    -5.0,
    -3.6666666666666665,
    -3.3333333333333335,
    -3.6666666666666665,
    -2.0,
    -1.6666666666666667,
    -2.0,
    -2.3333333333333335,
]
s5 = [
    -1.6666666666666667,
    0.3333333333333333,
    1.3333333333333333,
    2.0,
    0.6666666666666666,
    1.0,
    0.0,
    0.0,
    0.0,
]
s6 = [
    -1.6666666666666667,
    -0.3333333333333333,
    -2.3333333333333335,
    -0.6666666666666666,
    -0.6666666666666666,
    -1.6666666666666667,
    -2.3333333333333335,
    -1.0,
    -1.6666666666666667,
]
s7 = [
    0.6666666666666666,
    -1.0,
    -0.6666666666666666,
    -0.6666666666666666,
    -0.6666666666666666,
    -0.3333333333333333,
    0.0,
    1.3333333333333333,
    2.0,
]
s8 = [
    -1.0,
    -1.0,
    0.0,
    0.3333333333333333,
    -0.3333333333333333,
    -0.6666666666666666,
    1.0,
    2.3333333333333335,
    2.3333333333333335,
]
s9 = [
    0.0,
    -0.6666666666666666,
    -0.6666666666666666,
    -2.0,
    -1.3333333333333333,
    -1.3333333333333333,
    -0.6666666666666666,
    0.0,
    0.0,
]
c = [
    -32.0,
    -34.333333333333336,
    -25.0,
    -21.0,
    -19.666666666666668,
    -18.0,
    -22.0,
    -28.333333333333332,
    -26.333333333333332,
]

import matplotlib.pyplot as plt
from scipy import stats
import scienceplots
import pandas as pd

a = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
for index, content in enumerate(a):
    df = pd.DataFrame(
        [
            {"id": f"subject{index + 1}", "gen": gen, "avg": x}
            for gen, x in enumerate(content)
        ]
    )

    df.to_csv(f"./tables/subject{index + 1}.csv")

plt.style.use(["grid", "notebook", "science"])
fig, axes = plt.subplots(ncols=3, nrows=4, figsize=(30, 15))

axes[0][0].plot([i for i in range(9)], s1)
axes[0][0].set_title("Subject 1")
axes[0][0].set_xlabel("Generation")
axes[0][0].set_ylabel("Average Fitness")
axes[0][0].set_ylim([-35, 5])
axes[0][1].plot([i for i in range(9)], s2)
axes[0][1].set_title("Subject 2")
axes[0][1].set_xlabel("Generation")
axes[0][1].set_ylabel("Average Fitness")
axes[0][1].set_ylim([-35, 5])
axes[0][2].plot([i for i in range(9)], s3)
axes[0][2].set_title("Subject 3")
axes[0][2].set_xlabel("Generation")
axes[0][2].set_ylabel("Average Fitness")
axes[0][2].set_ylim([-35, 5])
axes[1][0].plot([i for i in range(9)], s4)
axes[1][0].set_title("Subject 4")
axes[1][0].set_xlabel("Generation")
axes[1][0].set_ylabel("Average Fitness")
axes[1][0].set_ylim([-35, 5])
axes[1][1].plot([i for i in range(9)], s5)
axes[1][1].set_title("Subject 5")
axes[1][1].set_xlabel("Generation")
axes[1][1].set_ylabel("Average Fitness")
axes[1][1].set_ylim([-35, 5])
axes[1][2].plot([i for i in range(9)], s6)
axes[1][2].set_title("Subject 6")
axes[1][2].set_xlabel("Generation")
axes[1][2].set_ylabel("Average Fitness")
axes[1][2].set_ylim([-35, 5])
axes[2][0].plot([i for i in range(9)], s7)
axes[2][0].set_title("Subject 7")
axes[2][0].set_xlabel("Generation")
axes[2][0].set_ylabel("Average Fitness")
axes[2][0].set_ylim([-35, 5])
axes[2][1].plot([i for i in range(9)], s8)
axes[2][1].set_title("Subject 8")
axes[2][1].set_xlabel("Generation")
axes[2][1].set_ylabel("Average Fitness")
axes[2][1].set_ylim([-35, 5])
axes[2][2].plot([i for i in range(9)], s9)
axes[2][2].set_title("Subject 9")
axes[2][2].set_xlabel("Generation")
axes[2][2].set_ylabel("Average Fitness")
axes[2][2].set_ylim([-35, 5])
axes[3][0].plot([i for i in range(9)], c)
axes[3][0].set_title("Constant")
axes[3][0].set_xlabel("Generation")
axes[3][0].set_ylabel("Average Fitness")
axes[3][0].set_ylim([-35, 5])

fig.delaxes(axes[3][1])
fig.delaxes(axes[3][2])
fig.tight_layout()
fig.savefig("sample.png")
