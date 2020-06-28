import unittest
loader = unittest.TestLoader()
tests = loader.discover(".")
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)

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
        self.delete_deepest(self.root, self.search(content))

#Método de eliminación.
    def delete_deepest(self, base, delnode): 
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

    def showtree(self):
        self.show_aux(self.root)
        
    def show_aux(self, base):
        if(base.left):
            self.show_aux(base.left)
        print(base.content)
        if(base.right):
            self.show_aux(base.right)

#Encontrar el Máximo
            
    def findmax(self):
        if(self.root.content is None):
            return None
        else:
            return self.findmax_aux(self.root)
        
    def findmax_aux(self, base):
        if (base is None):  
            return float('-inf') 
  
        res = base.content 
        lres = self.findmax_aux(base.left)
        rres = self.findmax_aux(base.right)
        if (lres > res): 
            res = lres  
        if (rres > res):  
            res = rres   
        return res

#Encontrar el mínimo
    
    def findmin(self):
        if(self.root.content is None):
            return None
        else:
            return self.findmin_aux(self.root).content

    def findmin_aux(self, base):
        if(base.left is None):
            return base
        else:
            return self.findmin_aux(base.left)

#Hacer impreso del árbol InOrder

    def printinorder(self):
        self.printino_aux(self.root)

    def printino_aux(self, base):
        if(base):
            self.printino_aux(base.left)
            print(base.content)
            self.printino_aux(base.right)

#Hacer impreso del árbol PostOrder
            
    def printpostorder(self):
        self.printposto_aux(self.root)
            
    def printposto_aux(self, base):
        if(base):
            self.printposto_aux(base.left)
            self.printposto_aux(base.right)
            print(base.content)

#Hacer impreso del árbol PreOrder
            
    def printpreorder(self):
        self.printpreo_aux(self.root)
            
    def printpreo_aux(self, base):
        if(base != None):
            print(base.content)
            self.printpreo_aux(base.left)
            self.printpreo_aux(base.right)

#Clase Nodo
class Node:
    def __init__(self):
        self.right = None
        self.left = None
        self.content = None

class TestRoot(unittest.TestCase):
    def test_sum(self):
        a1 = BinaryTree()

        self.assertEqual(a1.findmin(), None)
        self.assertEqual(a1.findmax(), None)

        a1.insert(12)
        a1.insert(6)
        a1.insert(3)
        a1.insert(7)
        a1.insert(14)
        a1.showtree()
        
        print("El mayor es: " + str(a1.findmax()))
        print("El menor es: " + str(a1.findmin()))
        print("Probando busqueda del nodo 14" + str(a1.search(14)))
        
        a1.printinorder()
        
        a1.printpostorder()
        
        a1.printpreorder()

        self.assertEqual(a1.findmin(), 3)
        self.assertEqual(a1.findmax(), 14)

        a1.deletion(14)
        self.assertEqual(a1.root.right, None)
        self.assertEqual(a1.findmax(), 12)
        
        a1.deletion(7)
        self.assertEqual(a1.root.left.right, None)
        a1.deletion(3)
        self.assertEqual(a1.root.left.left, None)
        a1.deletion(6)
        a1.insert(10)
        a1.insert(2)
        self.assertEqual(a1.findmin(), 2)
        self.assertEqual(a1.search(10).content, 10)
        a1.deletion(12)

        a2 = BinaryTree()
        a2.insert(12)
        a2.insert(15)
        a2.insert(16)
        a2.deletion(16)
        self.assertEqual(a2.findmax(), 15)
        
        


if __name__ == '__main__':
    unittest.main()
