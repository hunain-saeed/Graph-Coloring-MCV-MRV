pk = {}
vertex = {}
colorSeq = []
color = {1:'Red', 2:'Green', 3:'Blue'}

def printColor():
    for i in vertex.keys():
        print(i, " : ", color[vertex[i]])

def colorGraph():
    ver = pickMRV(list(pk.keys()))
    colorSeq.append(ver)
    vertex[ver] = 1
    
    for j in pk.keys():
        ver = pickMRV(pk[j])
        colorSeq.append(ver)
        if ver != "":
            vertex[ver] = safeColor(ver)
        

    return

def safeColor(ver):
    col = []
    for i in pk[ver]:
        col.append(vertex[i])
    
    for i in color.keys():
        if i not in col:
            return i


def pickMRV(ver):
    minNode = ""
    lenNode = 999
    for i in ver:
        if vertex[i] == 0:
            if lenNode > len(pk[i]):        
                lenNode = len(pk[i])
                minNode = i
    
    return minNode


def main():
    global pk
    global vertex
    pk = {
        'Sindh':        ['Baluchistan', 'Punjab'],
        'Baluchistan':  ['NWFP', 'Punjab', 'Sindh'],
        'Punjab':       ['Sindh', 'Baluchistan', 'NWFP', 'Kashmir'],
        'NWFP':         ['Baluchistan', 'Punjab', 'Kashmir'],
        'Kashmir':      ['Punjab', 'NWFP']
    }

    vertex = {
        'Sindh': 0,
        'Baluchistan': 0,
        'Punjab': 0,
        'NWFP': 0,
        'Kashmir': 0
    }

    colorGraph()

    print("Coloring Sequence:")
    for i in colorSeq:
        print(i)

    printColor()

main()