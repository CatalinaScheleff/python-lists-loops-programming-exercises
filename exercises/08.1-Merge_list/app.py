chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    merged_list = []

    for name in list1:
        merged_list.append(name)

    for name in list2:
        merged_list.append(name)
    return merged_list

    
print(merge_list(chunk_one, chunk_two))
