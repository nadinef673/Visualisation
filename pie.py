import matplotlib.pyplot as plt

students = ["Boys", "Girls"]
data = [12, 8]

fig = plt.figure(figsize = (12, 8))
plt.pie(data, labels = students)

plt.show()