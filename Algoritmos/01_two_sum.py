class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print([i, j])   
                    return [i, j]


sol = Solution()
sol.twoSum([2, 7, 11, 15], 13)

# Em TWO_SUM temos uma lista de números e um alvo, onde devemos indicar
# em quais ÍNDICES da lista a soma dos valores alcança o alvo.
#
# Linha 3: for i in range(len(nums)):
# i representa o ÍNDICE de cada posição da lista (0, 1, 2, 3...)
#
# Linha 4: for j in range(i+1, len(nums)):
# j é outro índice que sempre começa UMA posição à frente de i,
# para evitar comparar um elemento com ele mesmo e não repetir pares.
#
# Se nums[i] + nums[j] == target, retornamos os índices [i, j]
#
# No fim, criamos um objeto da classe Solution() e chamamos o método
# sol.twoSum(). O self representa o próprio objeto (sol).
