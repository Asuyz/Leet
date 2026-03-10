class Solution(object):
    def isPalindrome(self, x):
            lista = list(str(x))
            if lista == list(reversed(lista)):
                return True
            else:
                 return False


sol = Solution()
print(sol.isPalindrome(121))

# Transformamos o número (x) em uma lista e convertemos com (str(x)) 
# pois o número precisa virar uma string antes do uso
#
# Usamos reversed(lista) e não reversed(x) para inverter a lista não o número
#
# Depois retornamos o True ou False