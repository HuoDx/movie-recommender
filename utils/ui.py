import os
import sys

def _clear_screen():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
def display_options(kv_pairs):
    
    _clear_screen()
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
        if(0 <= choice < len(option_list)+1):
            _clear_screen()
            option_list[choice-1]()
        input('\n ==Press [Enter] to continue.')

    except Exception as e:
        pass