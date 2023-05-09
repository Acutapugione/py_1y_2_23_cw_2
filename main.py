    
def plus(*args, **kwargs): 
    return sum( args )


def find_not_unique(*args:tuple[list]):
    not_unique_list = []
    
    for index, list_ in enumerate(args):
        for item in list_:
            if item in not_unique_list:
                continue
            
            for item in args[index+1]:
                if item in list_:
                    not_unique_list.append(item)
                
    return set(not_unique_list)


#****************************************
print(
    find_not_unique(
        [1, 2, 3, 4, 0.33, 1, 2, 4, 9, 8, 5, 7,],
        [7, 6, 4, .33, 3.5, .25, 7.125,],
        [0.33, 7, 3.5, 0.25, 4],
        [0.33, 7, 3.5, 0.25, 4],
        [0.33, 7, 3.5, 0.25, 4],
        [0.33, 7, 3.5, 0.25, 4],
    )
)

# print("Lorem ipsum dolor sit, amet consectetur\
# adipisicing elit. Aperiam nam rem odio id.\
# Vel laudantium, odit cupiditate consectetur\
# voluptatum neque laboriosam provident vero,\
# voluptatem dignissimos fugit blanditiis.")