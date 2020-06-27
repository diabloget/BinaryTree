#Clase Árbol Binario

class BinaryTree:
    def __init__(self):
        self.root = Node()

#insertar elemento en el árbol.

    def insert(self, content):
        self.insert_aux(content, self.root)

    def insert_aux(self, content, base):
        if(base.content):
            if(content < base.content):
                if(base.left is None):
                    base.left = Node()
                    base.left.content = content
                else:
                    self.insert_aux(content, base.left)
            elif(content > base.content):
                if(base.right is None):
                    base.right = Node()
                    base.right.content = content
                else:
                    self.insert_aux(content, base.right)  
        else:
            base.content = content

#Eliminar nodo en árbol.
    def deletion(self, content):
        self.deletion_aux(self.root, content)
        
    def deletion_aux(self, base, content): 
        if (base is None): 
            return None
        
        if (base.left is None and base.right is None): 
            if (base.content is content):  
                return None
            else: 
                return base
            
        contentnode = None
        queue = [base] 
        
        while(len(queue)): 
            temp = queue.pop(0)
            
            if (temp.content is content): 
                contentnode = temp
                
            if (temp.left): 
                queue.append(temp.left)
                
            if (temp.right): 
                queue.append(temp.right)
                
        if (contentnode):  
            x = temp.content
            self.deleteDeepest(base, temp) 
            contentnode = x
            
        return base

#Search
    def search(self, content):
        return self.search_aux(self.root, content)
    
    def search_aux(self, base, content): 
        if (base is None or base.content == content): 
            return base 
      
        if (base.content < content): 
            return self.search_aux(base.right, content)
        
        return self.search_aux(base.left, content)

#Intermediario entre Search para buscar el nodo y el elemento eliminar, que necesita conocer
#la posición en memoria de dicho nodo para eliminarlo.
    
    def deletion(self, content):
        self.deleteDeepest(self.root, self.search(content))

#Método de eliminación.
    def deleteDeepest(self, base, delnode): 
        queue = [base] 
        
        while(len(queue)): 
            temp = queue.pop(0) 
            if (temp is delnode): 
                temp = None
                return
            
            if (temp.right): 
                if (temp.right is delnode): 
                    temp.right = None
                    return
                else: 
                    queue.append(temp.right)
                    
            if (temp.left): 
                if (temp.left is delnode): 
                    temp.left = None
                    return
                else: 
                    queue.append(temp.left) 
            
#Mostrar todo el árbol en orden.

    def showTree(self):
        self.showT_aux(self.root)
        
    def showT_aux(self, base):
        if(base.left):
            self.showT_aux(base.left)
        print(base.content)
        if(base.right):
            self.showT_aux(base.right)

#Encontrar el Máximo
            
    def findMax(self):
        if(self.root is None):
            return None
        else:
            return self.findMax_aux(self.root)
        
    def findMax_aux(self, base):
        if (base is None):  
            return float('-inf') 
  
        res = base.content 
        lres = self.findMax_aux(base.left)
        rres = self.findMax_aux(base.right)
        if (lres > res): 
            res = lres  
        if (rres > res):  
            res = rres   
        return res

#Encontrar el mínimo
    
    def findMin(self):
        if(self.root is None):
            return None
        else:
            return self.findMin_aux(self.root).content

    def findMin_aux(self, base):
        if(base.left is None):
            return base
        else:
            return self.findMin_aux(base.left)

#Hacer impreso del árbol InOrder

    def printInOrder(self):
        self.printInO_aux(self.root)

    def printInO_aux(self, base):
        if(base):
            self.printInO_aux(base.left)
            print(base.content)
            self.printInO_aux(base.right)

#Hacer impreso del árbol PostOrder
            
    def printPostOrder(self):
        self.printPostO_aux(self.root)
            
    def printPostO_aux(self, base):
        if(base):
            self.printPostO_aux(base.left)
            self.printPostO_aux(base.right)
            print(base.content)

#Hacer impreso del árbol PreOrder
            
    def printPreOrder(self):
        self.printPreO_aux(self.root)
            
    def printPreO_aux(self, base):
        if(base != None):
            print(base.content)
            self.printPreO_aux(base.left)
            self.printPreO_aux(base.right)

#Clase Nodo
class Node:
    def __init__(self):
        self.right = None
        self.left = None
        self.content = None


a1 = BinaryTree()
a1.insert(12)
a1.insert(6)
a1.insert(14)
a1.insert(3)
a1.showTree()


print("El mayor es: " + str(a1.findMax()))
print("El menor es: " + str(a1.findMin()))

print("Impreso In Order: ")
a1.printInOrder()
print("Impreso Post Order: ")
a1.printPostOrder()
print("Impreso Pre Order: ")
a1.printPreOrder()
#print(a1.root.left.content)
a1.deletion(14)
#a1.deleteDeepest(a1.root, a1.root.left)
print("Impreso In Order despues de eliminar el nodo con valor 6: ")
a1.printInOrder()

        

    
        
