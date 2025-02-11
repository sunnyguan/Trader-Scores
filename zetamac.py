"""
Generates score trend over time for zetamac
"""

import matplotlib.pyplot as plt

data = open('zetamac.txt', 'r')

scores = data.read().split()
scores = [int(score) for score in scores if score !=
          '0']  # 0 to separate between days

p = len(scores)
LAG = 10
means = []

for i in range(LAG - 1):
    sump = sum(scores[0:i + 1])
    means.append(1.0*sump/(i + 1))

for i in range(LAG, p + 1):
    sump = sum(scores[i - LAG:i])
    means.append(1.0*sump/LAG)

axes = plt.gca()
axes.set_ylim([min(scores) - 1, max(scores) + 1])

y = range(len(means))
plt.xlabel('No. of tries', fontsize=10)
plt.ylabel('Score', fontsize=10)

line_up,  	= plt.plot(y, scores, label='Scores')
line_down, 	= plt.plot(y, means, label='De-noised')

plt.legend(handles=[line_up, line_down])
fig = plt.gcf()
plt.show()
fig.savefig('scores.png')
