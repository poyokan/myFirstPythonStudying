

def str_to_float(str):
    """
    change str to float
    @param str : str
    @return : float(str) or if can't change str to float,return None
    
    """
    try:
        return float(str)
    
    except ValueError:
        return None

def main():
    item = str_to_float(input("floatに変えたい数字を入力してください:"))
    print(item,":",type(item))

main()