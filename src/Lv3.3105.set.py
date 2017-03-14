#-*- coding:utf8 -*-

setMathPassed = {"柯南", "灰原", "步美", "美環", "光彦"}
setEnglishPassed = {"柯南", "灰原", "丸尾", "野口", "步美"}

setAllPeople = setMathPassed.union(setEnglishPassed)
setAllDiffEng = setAllPeople.difference(setEnglishPassed)
setAllDiffMath = setAllPeople.difference(setMathPassed)
setAllPass = setMathPassed.intersection(setEnglishPassed)

lstAllDiffEng = list(setAllDiffEng)
lstAllDiffMath = list(setAllDiffMath)
lstAllPass = list(setAllPass)

lstAllDiffEng.sort()
lstAllDiffMath.sort()
lstAllPass.sort()

print(lstAllDiffEng)
print(lstAllDiffMath)
print(lstAllPass)
