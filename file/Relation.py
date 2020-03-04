"""
Properties of relations (see Pages 576--578 for details).
"""

def reflexive(R, A):
    """Returns True if a relation R on set A is reflexive, False otherwise."""
    for a in A:
        if (a, a) not in R:
            return False
    return True

def symmetric(R, A):
    """Returns True if a relation R on set A is symmetric, False otherwise."""
    for a, b in R:
        if (b, a) not in R:
            return False
    return True

def transitive(R, A):
    """Returns True if a relation R on set A is transitive, False otherwise."""
    for a in A:
        for b in A:
            if (a, b) in R:
                for c in A:
                    if (b, c) in R and (a, c) not in R:
                        return False
    return True

if __name__ == "__main__":
    # see Example 7 on Page 576
    A = set([1, 2, 3, 4])
    R1 = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (3, 4), (4, 1), (4,3),(1,4),(1,3),(2,3),(2,4),(3,1),(3,2),(4,2), (4, 4)]
    R2 = [(1, 1), (1, 2), (2, 1),(2,2),(3,3),(4,4)]
    R3 = [(1, 1), (1, 2), (1, 4), (2, 1), (2, 2), (3, 3), (4, 1), (4, 4), (4,2),(2,4)]
    R4 = [(2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3),(1,1),(2,2),(3,3),(4,4),(1,2),(1,3),(2,3),(1,4),(2,4),(3,4)]
    R5 = [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4) , (2,1),(3,1),(4,1),(3,2),(4,2),(4,3)]
    R6 = [(3, 4),(4,3),(1,1),(2,2),(3,3),(4,4)]
    for R in [R1, R2, R3, R4, R5, R6]:
        print (R)
        print ("  reflexive: ", reflexive(R, A))
        print ("  symmetric: ", symmetric(R, A))
        print ("  transitive:", transitive(R, A))
