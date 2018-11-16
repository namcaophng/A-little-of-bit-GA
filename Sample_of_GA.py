import random

population = []
index = 0
value = []
i_ = [0, 0, 0]
j_ = [0, 0, 0]
count = 0
# The first generation
def populate():
    x1 = random.uniform(0, 5)
    x2 = random.uniform(1, 3)
    x3 = random.uniform(6, 9)
    population.append([x1, x2, x3])

for i in range(50):
    populate()

# Fitness and max
def fitness(gen):
    x1 = gen[0]
    x2 = gen[1]
    x3 = gen[2]
    r = x1**2 - x1*x2 + x3
    return r


def fit():
    for b in population:
        value.append(fitness(b))


def delete_():
    min_ = fitness(population[0])
    index_ = population[0]
    for a in population:
        if fitness(a) < min_:
            min_ = fitness(a)
            index_ = a
    population.remove(index_)
# Crossover
def crossover(i, j):

    k = random.randrange(1, 3)
    if k == 1:
        i_[0]=i[0]
        i_[1]=j[1]
        i_[2]=j[2]
        j_[0]=j[0]
        j_[1]=i[1]
        j_[2]=i[2]
    else:
        i_[0]=i[0]
        i_[1]=i[1]
        i_[2]=j[2]
        j_[0]=j[0]
        j_[1]=j[1]
        j_[2]=i[2]
    population.append(i_)
    population.append(j_)
    delete_()
    delete_()
def mutation(i):
    k = random.randrange(0, 3)
    if k == 0:
        i_ = i
        i_[0] = random.uniform(0, 5)
    elif k == 1:
        i_ = i
        i_[1] = random.uniform(1, 3)
    else:
        i_ = i
        i_[2] = random.uniform(6, 9)
    population.append(i_)
    delete_()
# Main program
while count <5000:
    la = random.uniform(0,1)
    i = random.choice(population)
    population.remove(i)
    j = random.choice(population)
    population.append(i)
    if la <= 0.9:
        crossover(i, j)
    i = random.choice(population)
    if la <= 0.3:
        mutation(i)
    fit()
    best = max(value)
    print best
    count += 1
print population
print len(population)


