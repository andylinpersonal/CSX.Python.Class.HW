#-*- Coding:UTF8 -*-

Dict = {"P":"Pikachu", "M":"Mickey Mouse", "H":"Hello kitty"}

while True:
    string = input()
    if string == '-1':
        break
    '''
    more simple version:
    if string in Dict:
        print(Dict[string])
    '''
    for i in Dict:
        if i == string:
            print(Dict[string])
            break
    else:
        print('%s does not exist. Enter a new one:'%string)
        newIn = input()
        #如果不存在 新增該項目到字典
        Dict.update({string:newIn})
        
