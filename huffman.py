__license__ = 'Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: huffman.py 2023-03-24'

"""
Huffman homework
2023-03
@author: louis.molinier
"""

from algo_py import bintree
from algo_py import heap


###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

###############################################################################
## COMPRESSION

def build_frequency_list(dataIN):
    """
    Builds a tuple list of the character frequencies in the input.
    """
    L = []
    R = []
    for i in range (256):
        L.append(0)
    for e in dataIN:
        L[ord(e)] +=1
    for i in range (256):
        if L[i] != 0:
            R.append((L[i],chr(i)))
    return R


def build_Huffman_tree(inputList):
    """
    Processes the frequency list into a Huffman tree according to the algorithm.
    """
    if len(inputList) == 0:
        return None
    H = heap.Heap()
    for (freq, val) in inputList:
	    H.push((freq, bintree.BinTree(val, None,None)))
    t = len(H.elts)
    while (t > 2):
	    (i , l) = H.pop()
	    (j , r) = H.pop()
	    B = bintree.BinTree(None,r,l)
	    H.push((i+j,B))
	    t -= 1
    return (H.pop())[1]


def charOf(B,c):
    if B != None:
        if B.key != c:
            tmp = charOf(B.left,c)
            if tmp == None:
                tmp = charOf(B.right,c)
                t = '1'
            else:
                t = '0'
            if tmp == None:
                return None
            else:
                return t + tmp
        else:
            return ""
    else:
        return None


def createDico(B, dico):
        L = [B]
        i = 0
        l = 1
        while i < l:
            T = L[i]
            if T.key != None:
                dico[ord(T.key)] = charOf(B, T.key)
            else:
                L.append(T.left)
                L.append(T.right)
                l += 2
            i += 1


def encode_data(huffmanTree, dataIN):
    """
    Encodes the input string to its binary string representation.
    """
    R = ""
    dico = []
    for i in range(256):
        dico.append(None)
    createDico(huffmanTree, dico)
    for e in dataIN:
	    R += dico[ord(e)]
    return R


def intToBin(c):
    R = ""
    while(c != 0):
        R = str(c%2) + R
        c //= 2
    l = len(R)
    while(l < 8):
        R = "0" + R
        l += 1
    return R
    

def encode_tree(huffmanTree):
    """
    Encodes a huffman tree to its binary representation using a preOrder traversal:
        * each leaf key is encoded into its binary representation on 8 bits preceded by '1'
        * each time we go left we add a '0' to the result
    """
    if huffmanTree is None:
        return ""
    elif huffmanTree.key is not None:
        return '1' + intToBin(ord(huffmanTree.key))
    return '0' + encode_tree(huffmanTree.left) + encode_tree(huffmanTree.right)

def createLchar():
    Lchar = []
    for i in range(256):
        Lchar.append(chr(i))
    return Lchar

def to_binary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    """
    R = ""
    l = len(dataIN)
    Lchar = createLchar()
    sep = l // 8
    for i in range(sep):
        n = 0
        for j in range(8):
            n *= 2
            if dataIN[i*8+j] != '0':
                n += 1
        R += Lchar[n]
    n = 0
    left = l % 8
    for i in range(l - left, l):
        n *= 2
        if dataIN[i] != '0':
            n += 1
    if left == 0:
        return (R, 0)
    else:
        R += Lchar[n]
        return (R, 8 - left)
    #


def compress(dataIn):
    """
    The main function that makes the whole compression process.
    """
    B = build_Huffman_tree(build_frequency_list(dataIn))
    return (to_binary(encode_data(B, dataIn)), to_binary(encode_tree(B)))
    
    
################################################################################
## DECOMPRESSION

def decode_data(huffmanTree, dataIN):
    """
    Decode a string using the corresponding huffman tree into something more readable.
    """
    R = ""
    B = huffmanTree
    for c in dataIN:
        if c == '0':
            B = B.left
        else:
            B = B.right
        if B.key != None:
            R += B.key
            B = huffmanTree
    return R

def binToChr(s):
    R = 0
    l = len(s)
    for i in range (l):
        R += int(s[l-1-i]) * (2**i)
    return chr(R)

def auxDecodeTree(dataIN, i):
    if (dataIN[i] == '1'):
        s = ""
        for j in range(8):
            s += dataIN[i+j+1]
        c = binToChr(s)
        return (i+9,bintree.BinTree(c,None,None))
    else:
        (x,B) = auxDecodeTree(dataIN, i+1)
        (y,T) = auxDecodeTree(dataIN, x)
        return (y, bintree.BinTree(None,B,T))
        
    
def decode_tree(dataIN):
    """
    Decodes a huffman tree from its binary representation:
        * a '0' means we add a new internal node and go to its left node
        * a '1' means the next 8 values are the encoded character of the current leaf         
    """
    return (auxDecodeTree(dataIN, 0))[1]


def createLbin():
    Lbin = []
    for i in range(256):
        Lbin.append(intToBin(i))
    return Lbin
    

def from_binary(dataIN, align):
    """
    Retrieve a string containing binary code from its real binary value (inverse of :func:`toBinary`).
    """
    R = ""
    l = len(dataIN)
    Lbin = createLbin()
    for i in range(l - 1):
        R += Lbin[ord(dataIN[i])]
    last = Lbin[ord(dataIN[l - 1])]
    tmp = ""
    for i in range(align, 8):
        tmp += last[i]
    R += tmp
    return R


def decompress(data, dataAlign, tree, treeAlign):
    """
    The whole decompression process.
    """
    return decode_data(decode_tree(from_binary(tree,treeAlign)),from_binary(data, dataAlign))
