def solution(string):
   if len(string) == 0:
      return string
   else:
      return solution(string[1:]) + string[0]
'''dsadasdas '''''''sadasdas'''''

print(solution("hola"))