def display_options(kv_pairs):
    print(" Please Choose")
    print("#-------#")
    option_list = []
    index = 1
    print('| Choice\t| Option|')
    for k,v in kv_pairs.items():
        print('| %s\t| %d\t|'%(k, index))
        index += 1
        option_list.append(v)
    
    try:
        choice = int(input())
        if(0 <= choice < len(option_list)):
            option_list[choice-1]()
    except Exception as e:
        pass