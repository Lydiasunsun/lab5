import matplotlib.pyplot as plt


studentscores = {"larry": 80, "curly": 75, "mo": 90}

student = studentscores.keys()
score = studentscores.values()
plt.bar(student, score)
plt.show()
#
# if __name__ == '__main__':
#     # get the scores into a list
#     scores = studentscores.values()
#     # get the names into a
