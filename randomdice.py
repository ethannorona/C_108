import random
import plotly.figure_factory as pf

dice_results = []

for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_results.append(dice1 + dice2)
    
fig = pf.create_distplot([dice_results],["Result"])

fig.show()