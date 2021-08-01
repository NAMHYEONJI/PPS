def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        li = []
    check = True
    
    for j in range(len(i)):
      if i[j] in skill:
      	li.append(i[j])

    for k in range(len(li)):
      if li[k] != skill[k]:
        check = False
        break

    if check == True:
        answer += 1

    return answer
    