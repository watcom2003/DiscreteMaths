#include <iostream>

using namespace std;

int main()
{
    struct CELL {
        int element; 
        struct CELL *left;
        struct CELL *right;
    };
    typedef struct CELL *TREE;
    
    TREE t = NULL;    /* an empty tree */
    t = makeTree();   /* build a tree */
    printTree(t);
    
   int n = numElems(t);
   printf("No. of nodes: %d\n", n);

   if (hasElem(t, 19))
     printf("Found 19\n");
   else
     printf("19 not in the tree\n");


    return 0;
}
