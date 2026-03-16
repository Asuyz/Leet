# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            soma = a + b + carry
            carry = soma // 10

            current.next = ListNode(soma % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        
        lista3 = []
        node = dummy.next
        while node:
            lista3.append(node.val)
            node = node.next

        print("".join(map(str, lista3)))

        return dummy.next
        
  
sol = Solution()
sol.addTwoNumbers([2,4,3],[5,6,4])

# Neste exercicio em especifico ele pede o uso de listNode para a resolução, foi usada ia para converter o código para o requisito segue o código feito por eu:
#
#l1 = list(reversed(l1))
        #l2 = list(reversed(l2))

        #carry = 0
        #lista3 = []

        ##for a, b in zip(l1, l2):
            #soma = a + b + carry
            #carry = soma // 10      
            ##lista3.append(soma % 10) 

        ##if carry:
            ##lista3.append(carry)    

        ##lista3 = list((lista3))
        ##print(lista3)
# 
# --------------------------------------------------------------------------------------------
# 
# Nas primeiras linhas estabelecemos as listas e invertemos elas.
# Logo em seguita criamos o carry para a soma correta dos valores dentro das listas e a lista 3 para armazenar a soma das listas
# Somamos a duas listas usando zip e fazemos uma conversão caso a soma dos valores ultrapasse 10 e armazenamos no carry 
# If carry é se o carry passar de 10 somamos este valor na lista. Exemplo: [7,10,7] passa a ser [8,0,7]
#
# ---------------------------------------------------------------------------------------------
# Logica com ListNode
#
# Aqui o l1 e l2 são ListNodes, ou seja, uma cadeia de nós
# onde cada um tem .val (o valor) e .next (o próximo nó).
# Como o LeetCode já entrega os números na ordem invertida
# (2 → 4 → 3 representa 342), não precisamos reverter no início
# e podemos somar diretamente da esquerda para a direita.
# O dummy é um nó auxiliar vazio usado para facilitar a construção
# do resultado, e o current é um ponteiro que avança a cada iteração
# criando novos nós. No final, percorremos os nós do resultado
# para montar a lista e printar.
