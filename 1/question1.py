def group_by_owners(file_dict):
    owner_dict = {}
    for k,v in file_dict.items():
        if v not in owner_dict:
            owner_dict[v] = [k]
        else:
            owner_dict[v].append(k)
    
    return owner_dict #dict containig a list of file names for each owner name

#dict with file name and owner name 
file_dict = {               
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

owner_dict = group_by_owners(file_dict)

print(owner_dict)