import random
maxFit=0
def random_genotype(size): #making random genotypes    
    a=[]
    for i in range(size):    
        a.append(random.randint(1, size))
    return a
def fitness(gentype): #Calculate fitness for genotypes
    col_clashes =sum([gentype.count(alley)-1 for alley in gentype])/2 #count each element of geneo type for multi appearance and miness 1 then divide by 2
    dig_clashes = 0
    n=len(gentype)
    for i in range(n): #count dig if [x2-x1]==[y2-y1] dig condition
        for j in range(i+1,n):
            x = abs(i-j)
            y = abs(gentype[i] - gentype[j])
            if(x == y):
                dig_clashes += 1
    return (maxFit - dig_clashes - col_clashes) #return fittnes of genotype

def random_pick(population):# select 5 candidate parnt
        return [random.choice(population) for i in range(5)]

def crossover(x, y): #cross_over 
    n = len(x)
    c = random.randint(0, n - 1)   
    return x[0:c] + y[c:n],y[0:c] + x[c:n]

def mutate(x):  #randomly changing the value of a random index of a chromosome with 80% probablity
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x
def printG(solution):#print Solution on screen
    board = []
    for x in range(n):
        board.append(["-"] * n)
    for i in range(n):
        board[n-solution[i]][i]="*"
    for row in board:
            print (" ".join(row))
               

if __name__ == "__main__":
    population=[]
    n = int(input("Insert number of Queen: "))
    maxFit = (n*(n-1))/2
    for i in range(100):    
        population.append(random_genotype(n))
      
    
    population = [random_genotype(n) for _ in range(100)]
    generation=1
    while not maxFit in [fitness(gen) for gen in population] and generation < 10000:
        generation +=1
        print ("Generation:",generation, " \ ")
        population5=random_pick(population)
        fitness5=[fitness(n1) for n1 in population5]
        zip1=zip(population5,fitness5)
        zip1=(sorted(zip1, key = lambda x: x[1]))
        x=zip1[4][0]
        y=zip1[3][0]
        
        childes=crossover(x, y)
        x=childes[0]
        y=childes[1]
        if random.randint(1,100) < 80:
            x=mutate(x)
        if random.randint(1,100) < 80:
            y=mutate(y)
        fitnessPopulation=[fitness(n1) for n1 in population]
        for index in range(2):
            index=fitnessPopulation.index(min(fitnessPopulation))
            fitnessPopulation.pop(index)
            population.pop(index)
        population.append(x)
        population.append(y)
    print("Solved in Generation {}!".format(generation))
    for gen in population:
        if fitness(gen) == maxFit:
            print("");
            print("One of the Possible solutions: ")
            solution = gen
            printG(solution)
            n=input("Press any key to Exit: ")
            
   
        
        
         

        
