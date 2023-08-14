import numpy
import matplotlib.pyplot as plt

lang = [
    "C",
    "Java",
    "Python",
    "C++",
    "C#",
    "Visual Basic",
    "JavaScript",
    "PHP",
    "R",
    "Groovy",
]
value = [17.38, 11.96, 11.72, 7.56, 3.95, 3.84, 2.20, 1.99, 1.90, 1.84]

index = numpy.arange(len(lang))
plt.bar(index, value)
plt.ylabel("Popularność [%]")
plt.xticks(index, lang, rotation=30)
plt.title("Popularność języków programowania")
plt.show()
