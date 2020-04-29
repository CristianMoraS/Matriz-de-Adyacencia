import os

adjacencyList = {1: {1}, 2: {2, 3}, 3: {2, 3}}


class AdjacencyMatrix():

       def __init__(self, adjacencyList, label = ""):
           """ 
           Instanciation method of the class.
           Create an adjacency matrix from an adjacencyList.
           It is supposed that graph vertices are labeled with numbers from 1 to n.
           """

           self.matrix = []
           self.label = label

           #create an empty matrix
           for i in range(len(adjacencyList.keys())):
               self.matrix.append( [0]*(len(adjacencyList.keys())) )

           for key in adjacencyList.keys():
               for value in adjacencyList[key]:
                   self[key-1][value-1] = 1

       def __str__(self):
           # return self.__repr__() is another possibility that just print the list of list
           # see python doc about difference between __str__ and __repr__

           #label first line
           string = self.label + "\t"
           for i in range(len(self.matrix)):
               string += str(i+1) + "\t"
           string += "\n"

           #for each matrix line :
           for row in range(len(self.matrix)):
               string += str(row+1) + "\t"
               for column in range(len(self.matrix)):
                   string += str(self[row][column]) + "\t"
               string += "\n"


           return string

       def __repr__(self):
           return str(self.matrix)

       def __getitem__(self, index):
           """ Allow to access matrix element using matrix[index][index] syntax """
           return self.matrix.__getitem__(index)

       def __setitem__(self, index, item):
           """ Allow to set matrix element using matrix[index][index] = value syntax """
           return self.matrix.__setitem__(index, item)

       def areAdjacent(self, i, j):
           return self[i-1][j-1] == 1

m = AdjacencyMatrix(adjacencyList, label="mbr")
print(m)
print("m.areAdjacent(1,2) :",m.areAdjacent(1,2))
print("m.areAdjacent(2,3) :",m.areAdjacent(2,3))
file = open("C:/Users/Acer/Desktop/Matriz y lista adyacente/MatrizAdyacente.txt", "w")
    m.write("m.areAdjacent(1,2) :",m.areAdjacent(1,2)+ os.linesep)
    m.write("m.areAdjacent(2,3) :",m.areAdjacent(2,3))
file.close()