import string

def create_double_dict():
    alphabet_list = list(string.ascii_lowercase)
    double_alphabet_dict = {}
    double_list= []


    for x in alphabet_list:
        for y in alphabet_list:
            double = x+ y
            double_list.append(double)

    for a in double_list:
        double_alphabet_dict[a] = 0

    return(double_alphabet_dict)

def create_dict():
    alp_list=[]
    alp_dict={}
    alphabet_list = list(string.ascii_lowercase)
    for x in alphabet_list:
        alp_list.append(x)

    for a in alp_list:
        alp_dict[a] = 0

    return(alp_dict)