#loops
from lesson4 import scores

while True:
    print("Nice one")
    break

scores=[78,83,48,38,82,46]

for score in scores:
    if score >= 50 and score <=70 and score % 2==0:
       print(score)

