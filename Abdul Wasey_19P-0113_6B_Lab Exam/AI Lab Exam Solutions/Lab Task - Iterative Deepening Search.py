myGraph = {
1: [2,3,5],
2: [4,5],
3: [5,6],
5: [],
6: [7,9],
4: [5,8],
7: [4,5,8],
8: [],
9: [7,8]}

def IDS(myG, value):
    key = 1
    i = 0
    
    while True:
        print("Iteration", i+1)
        stck = []
        visited = []
        stck.append(key)
        for x in range(i+1):
           
            size = len(stck)
            for y in range(size):
                visiting = stck.pop(0)
                print(visiting, end=", ")
                if visiting is value:
                    return True

                else:
                    visited.append(visiting)
                    for val in myG.get(visiting):
                        if val not in visited:
                            stck.append(val)
                            visited.append(val)
        print()
        i+=1
        if not stck:
            break

if(IDS(myGraph, 7)):
    print("\n\nFound")
else:
    print("\nNot Found")
    