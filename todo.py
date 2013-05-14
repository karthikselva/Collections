## Data Structures

array - O(1) access ,  fixed size , memory wastage , deletion hard
list - O(N) access, dynamic , deletion easy
	queue - FIFO 
	stack - LIFO
	Dequeue - Enqueue at first / enqueue atlast
Double and circular for easy access
	Double linked list browser forward backward
	Circular - Round robin scheduling till all elements becomes zero
Trees - O(logN)          b for best and O(N) for worst 
	Poly tree - Struct ptree { Data data , ptree *sibling , ptree *child }
	btree - Struct btree { Data data , ptree * right , ptree *left }
	AVL , Splay tree , BTREE to reduce worst case from O(N) ( Balance a unbalanced tree )
Graph 
	Vertex , edges 
	Cyclic , acyclic , directed , undirected
	DAG , Compilers CSE 
Hash table 
	O(1) access time for known key
	bit vector 
	fn=n%size / h1(x)=i*h2(x) ( i tends from 1->size on collision ) h2(x)=r-xmod(r) ( r a prime number smaller than hashtable size )
	rehashing - size=size*2
	extendible hashing - 00 	01 		10 		11      Main Memory
						  ^		^		^		^
						0011	0100	1000	1100	Secondary Memory
						0010	0101	1010	1111
						0001	0110	1011	1110
Trie 
	special prefix tree to find words starting 
	Radix trie with known words ( not with depth for len(string) )
Heap 	

	build_heap - strcutural property , heap order property
	delete_min - move right most to head and do build heap
	
Sorting techniques
Trees - Binary trees / bst / avl tree rotations / Hierarchy / traversals

### reversal link list

1->2->3->4->5->NULL

1<-2 3->4->5->NULL
	 ^
1<-2<-3 4->5->NULL
		^
1<-2<-3<-4 5->NULL
		   ^
1<-2<-3<-4<-5 NULL
			^
step 1: q=p->next # q=2
		r=q->next	# r=2->next =3
		p->next=NULL # 1->next=null

loop while r->next!=NULL:
	2->next=1
	p=2
	q=r
	r=r->next
step3:
	r->next=q

BST:
#include <stdlib.h>
#include <stdio.h>
using namespace std;

struct node
{
  int data;
  struct node* left;
  struct node* right;
};

struct node* insert_bst(struct node* root, int num){
  if(root == NULL){
    root = (struct node*)malloc(sizeof(struct node));
    root->data = num;
    root->left = NULL;
    root->right = NULL;
    return root;
  }else{
    if(num == root->data){
      return root;
    }

    if(num > root->data){
      root->right=insert_bst(root->right,num);
    }else{
      root->left=insert_bst(root->left,num);
    }
  }
  return root;
}

void inorder_traverse(struct node* root){
  if(root == NULL) return;

  inorder_traverse(root->left);
  printf("%d ",root->data);
  inorder_traverse(root->right);
}

struct node* bst_root = NULL;

int getmaxbst(struct node* root, int& subtreemin, int &subtreemax, int& max)
{
  if(root == NULL) return 0;

  int leftsubtreemin = -32767, rightsubtreemin = -32767;
  int leftsubtreemax = 32767, rightsubtreemax = 32767;
  int x,y;

  x = getmaxbst(root->left, leftsubtreemin, leftsubtreemax, max);
  y = getmaxbst(root->right, rightsubtreemin, rightsubtreemax, max);

  if(x==-1 || y ==-1)
    return -1;
  if(x==0) { leftsubtreemax = root->data; leftsubtreemin = root->data;}
  if(y==0) { rightsubtreemin = root->data; rightsubtreemax = root->data;}

  if(root->data < leftsubtreemax ||
     root->data > rightsubtreemin){
    return -1;
  }

  subtreemin = leftsubtreemin;
  subtreemax = rightsubtreemax;

  if(x+y+1 > max){
    max = x+y+1;
    bst_root = root;
  }

  return x+y+1;

}

int main()
{
  struct node* root=NULL;

  root=insert_bst(root,5);
  root=insert_bst(root,3);
  root=insert_bst(root,9);
  root=insert_bst(root,7);
  root=insert_bst(root,4);
  root=insert_bst(root,1);
  root=insert_bst(root,14);
  root=insert_bst(root,11);

  root->data = 0;

  int a,b,c,max=-32767;
  c = getmaxbst(root,a,b,max);
  printf("\nmax is %d\n",max);

  inorder_traverse(bst_root);
  return 1;
}

Inorder => left , Data , right - Sorting
Prerorder = > Data , left ,right - 
Post order => left , right , Data - Postfix

AVL tree rotation - single / double
heap 
Amortized time - what is it ?
Splay tree , Red black tree

## Random function Shuffle of cards
import random
a,b=range(1,52),[]
while len(a)!=0:
	tmp=random.choice(a)
	a.remove(tmp)
	b.append(tmp)
print b

other method 

a=range(1,52)
for i in range(0,51):
	t=random.randrange(0,51)
	tmp=a[t]
	a[t]=a[i]
	a[i]=tmp
	
## GCD 
gcd(a,0) = a
gcd(a,b) = gcd(b,a mod b).
lcm(a,b)=a*b / gcd(a,b)


## Maximum subsequence problem

def max_sum_subsequence(seq):
    maxsofar = 0
    maxendinghere = 0
    for s in seq:
        # invariant: maxendinghere and maxsofar are accurate
        # are accurate up to s
        maxendinghere = max(maxendinghere + s, 0)
        maxsofar = max(maxsofar, maxendinghere)
    return maxsofar


## Balanced tree  - Tree which has difference of two subtrees as <=1
Maximum - Minimum <=1 then balanced

def max_height(t):
	if t!=null
		return 1+max(height(t->left),height(t->right))
	else return 0
	
def min_height(t):
	if t!=null
		return 1+min(height(t->left),height(t->right))
	else return 0

operator precedence 

Postfix / Prefix

Backtracking
Hashing - Implement hash with mod / ( choose size as prime number )
Ø Direct method,
Ø Subtraction method,
Ø Modulo-Division method,
Ø Digit-Extraction method,
Ø Mid-Square method,
Ø Folding method,
Ø Pseudo-random method.

stacks - push pop peek , min in stack ,multiple stack
queue - front rear 
##### Towers of hanoi - 3 , move from a->c then rec(a->b) move(a,b) rec(b->c) 
To move N discs from S to D:
Move N-1 discs from S to Tmp
Move Nth disc from S to D
Move N-1 discs from Tmp to D

example for 3 discs S to D:

Move 2 discs from S to Tmp
	Move 1st disc from S to D
	Move 2nd disc from S to Tmp
	Move 1st disc from D to Tmp
Move 3rd disc from S to D
Move 2 Discs from Tmp to D
	Move 1st disc from Tmp to S
	Move 2nd disc from Tmp to D
	Move 1st disc from S to D
	
example for 4 discs:

Move 3 discs from S to Tmp
	Move 2 disc from S to D
		Move 1st disc from S to Tmp # printed in if loop
		Move 2nd disc from S to D # printed in Middle
		Move 1st disc from Tmp To D # Printed in if loop
	Move 3rd disc from S to Tmp
	Move 2 disc from D to Tmp
		Move 1st disc from D to S
		Move 2nd disc from D to Tmp
		Move 1st disc from S to Tmp
Move 4th disc from S to D
Move 3 Discs from Tmp to D
	Move 2 disc from Tmp to S
		Move 1st disc from Tmp to D
		Move 2nd disc from Tmp to S
		Move first disc from D to S
	Move 3rd disc from Tmp to D
	Move 2 disc from S to D
		Move 1st disc from S to Tmp
		Move 2nd disc from S to D
		Move first Disc from Tmp to D
			
Iterative :
	a,b,c=range(n),b,c
	while len(c)!=n:
		tmp=a[:-1]
		del a[:-1]
		if tmp&1 !=0 
			if c[:-1]&1!=0:
				c.append(tmp)
			else:
				b.append(tmp)
		else :
			if b[:-1]&1==0:
				b.append(tmp)
			else:
				c.append(tmp)
		swap(a,b,c)
		
		
Sorting a stack with two stacks - a[1,2,3,4,5] b[] , 

while a.top=!NULL: 
	tmp=pop(a)
	 while(b.top!=NULL && tmp>peek(b)):  
		push(a,pop(b)) 
	push(b,tmp)

Using queue as stack - When dequeue comes then shift A stack to other and pop from B stack. If 

tree - inorder successor next with particular node given  -> PARENT pointer present 

INORDER = LDR  Assume given node is p

input tree: 1 2 3 4 5 input node pointer : 3 output : give result as 4

#recursive - may fail
def successor(p):
	if p->right!=null then p=p->right while(p=p->left!=null); return p
	else p->parent->left==p: then return p
	else : tmp=p->parent p=null successor(tmp)

# Non-recursive
def successor(p):
	if p->right!=null then p=p->right while(p=p->left!=null); return p
	while e=p.parent!=NULL:
		if p->parent->left==p: then return p
		e=p
	return p

	
## Graph Implementation

graph.h				graph.c
-------				------
				#include "graph.h"

typedef char 	typedef struct vertexTag {
graphElementT;				  graphElementT element;
				  int visited;
				  struct edgeTag *edges;
				  struct vertexTag *next;
				} vertexT;

				typedef struct edgeTag {
				  struct vertexTag *connectsTo;
				  struct edgeTag *next;
				} edgeT;

typedef struct 		typedef struct graphCDT {
graphCDT			  vertexT *vertices;
*graphADT;				} graphCDT;

How it looks like ?

   |
   v
-------
|  A  |
|-----|     ---------     ---------
|   --+---> | B | --+---> | D | 0 |
|-----|     ---------     ---------
|  |  |
---+---
   |
   v
-------
|  B  |
|-----|
|  0  |
|-----|
|  |  |
---+---
   |
   v
-------
|  C  |
|-----|     ---------
|   --+---> | F | 0 |
|-----|     ---------
| NULL|
---+---
   
methods :
For general graph operations:
GraphAddVertex()
GraphAddEdge()
GraphIsReachable()
Because we are programming in C (setup/cleanup):
GraphCreate()
GraphDestroy()
action method example : GraphIsReachable().
				
				
### Trie:

              .
      /       |      \
     a        e       r
   /   \      |       |
  m     n     m       o
  |     |     |     /   \
  y     n     m    b     g
  |     |     |    |     |
\0 56 \0 15   a  \0 27   e
              |          |
            \0 30        r
                         |
                       \0 52
					  
trie.h                          trie.c
------				------
				#include "trie.h"

				typedef struct trieNodeTag {
				  char key;
				  trieValueT value;
typedef int trieValueT;		  struct trieNodeTag *next,
				                     *children;
				} trieNodeT;		

typedef struct trieCDT		typedef struct trieCDT {
	*trieADT;		  trieNodeT *root;
				} trieCDT;
	
###Depth first search / Breadth first search

  procedure DFS(G,v):
      label v as explored
      for all edges e in G.incidentEdges(v) do
          if edge e is unexplored then
              w <- G.opposite(v,e)
              if vertex w is unexplored then
                  label e as a discovery edge
                  recursively call DFS(G,w)
          else 
             label e as a back edge
			 
  procedure BFS(G,v):
      create a queue Q
      enqueue v onto Q
      mark v
      while Q is not empty:
          t <- Q.dequeue()
          if t is what we are looking for:
              return t
          for all edges e in G.incidentEdges(t) do
             o <- G.opposite(t,e)
             if o is not marked:
                  mark o
                  enqueue o onto Q
				  
#### Topological Sorting

L -> Empty list that will contain the sorted elements
S -> Set of all nodes with no incoming edges
while S is non-empty do
    remove a node n from S
    insert n into L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S
if graph has edges then
    return error (graph has at least one cycle)
else 
    return L (a topologically sorted order)
		
#Graphs - Prims Algorithm and Kruskal's algorithm
#prim's algorthm
procedure Prim(G: weighted connected graph with n vertices)
	T := a minimum-weight edge
	for i = 1 to n - 2
	begin
		e := an edge of minimum weight incident to a vertex in T and not forming a circuit
		in T if added to T
		T := T with e added
	end
return(T)

#Djikstra algrthm:
   function Dijkstra(Graph, source):
       for each vertex v in Graph:            // Initializations
           dist[v] := infinity ;              // Unknown distance function from source to v
           previous[v] := undefined ;         // Previous node in optimal path from source
       end for ;
       dist[source] := 0 ;                    // Distance from source to source
       Q := the set of all nodes in Graph ;   // All nodes in the graph are unoptimized - thus are in Q
       while Q is not empty:                  // The main loop
           u := vertex in Q with smallest distance in dist[] ;
          if dist[u] = infinity:
              break ;                        // all remaining vertices are inaccessible from source
          end if ;
          remove u from Q ;
          for each neighbor v of u:          // where v has not yet been removed from Q.
              alt := dist[u] + dist_between(u, v) ;
              if alt < dist[v]:              // Relax (u,v,a)
                  dist[v] := alt ;
                  previous[v] := u ;
                  decrease-key v in Q;       // Reorder v in the Queue
              end if ;
          end for ;
      end while ;
      return dist[] ;
  end Dijkstra.

#B-tree and B+ tree

#One tree tree is subtree of other tree tree2 - 
Inorder(tree1)==Inorder(tree2) && Preorder(tree1)==Preorder(tree2)
start from mathcing node
match(tree1,tree2)
	if tree1==null && tree2==null then return TRUE
	else if tree1==null || tree2==null then return FALSE
	if match(tree1.left,tree2.left)&&match(tree1.right,tree2.right)
	
#Find all posible path for given sum binary tree
sum(level,sum,tree,buffer)
		if tree=null
			return
		else add to buffer 
		find sum is equal
		sum(level+1,sum,tree.right,clone(buffer))
		sum(level+1,sum,tree.left,clone(buffer))
		
		4
	3	
		5
2
		2
	7
		1

## maximum subsequence problem

### insertion sort  - Partial sorting or Internal sorting occurs
for j<- 2 to n
	key = a[j]
	i=j-1
	while i>0 and a[i]>key
		do a[i]<-a[i+1]
		i--
	a[i+1]<-key

## bubble sort - complete sorting occurs at end of N-1 th loop

5 4 3 2 1


for i<-0 to n
	for j<-0 to i-1
		if a[i]>a[j]
			swap(a[i],a[j])
			
## selection sort
a=[1...n]
def select_sort(a):
	for i in range(len(a)):
		min,pos=65535,0
		for j in range(i,len(a)):
			if min > a[j]:
				min=a[j]
				pos=j
		a[pos]=a[i]
		a[i]=min
		print a
		
64 25 12 22 11
first min 11
11 25 12 22 64
second min 12
11 12 25 22 64
third min 22
11 12 22 25 64
fourth min 25
11 12 22 25 64   
	
### Merge sort

a[1..n] b[1..m] c[1..n+m]

def merge(a,b):
	c=[0]*(len(a)+len(b))
	index_a=0
	index_b=0
	while True:
		# copy rest of elements to array
		if index_a==len(a):
			for i in range(index_b,len(b)):
				c[index_a+index_b]=b[index_b]
			break
		elif index_b ==len(b):
			for i in range(index_a,len(a)):
				c[index_a+index_b]=a[index_a]
			break
		
		# copy first element to c	
		if a[index_a] < b[index_b]:
			c[index_a+index_b]=a[index_a]
			index_a=index_a+1
		else:
			c[index_a+index_b]=b[index_b]
			index_b=index_b+1
	return c

	
## delete occurence of one set

Set=	a e i o u 
Input = k a r t h i k

	k a r t h i k
	^
	k a r t h i k
	^
	
	k a r t h i k
	  ^
	k a r t h i k
	  ^
	 
	k a r t h i k
	    ^
	k a r t h i k
	  ^
	  
	k a r t h i k
	      ^
	k r r t h i k
		^
		
	k a r t h i k
	        ^
	k r t t h i k
		  ^
	
	k a r t h i k
	          ^
	k r t h h i k
		    ^
	
	k a r t h i k
	            ^
	k r t h h i k
		    ^
	
	k a r t h i k \0
	              ^
	k r t h k \0 k
			  ^

## delete duplicates in an array

a=[1,1,2,3,4,4,5,7]
i,j=0,0
loop of i till size:
	if(a[i]!=a[j])
		a[j]=a[i]
		j++

## delete duplicates in linked list
start,dup

loop start to end:
	
	
1234
123
12
1

char *a
tostr(num):
	if num%10==0:
		a=num+48
		a++
		return a

	else:
		a=tostr(num%10)

### reverse a number

1234
4321

def num(n):
	dest=0
	loop n%10!=0:
		v=n%10
		n=n/10
		dest=dest*10+v # 4 # 43 # 432 # 4321
		
 recursion ---
 
int rev_num = 0;
int BasePos =1 ;
int reversDigits2(int num)
{
   if(num > 0)
   {
     reversDigits2( num/10);
     rev_num += (num%10)*BasePos ;
     BasePos *=10 ;
   }
   return rev_num;
}

C program or code to find prime numbers between two numbers


#include<stdio.h>

int main(){

    int num,i,count,min,max;

     printf("Enter min range: ");
     scanf("%d",&min);

    printf("Enter max range: ");
    scanf("%d",&max);

    for(num = min;num<=max;num++){

         count = 0;

         for(i=2;i<=num/2;i++){
             if(num%i==0){
                 count++;
                 break;
             }
        }
        
         if(count==0 && num!= 1)
             printf("%d ",num);
    }
  
   return 0;
}

### string to decimal

str="534.535"
num=0
loop i till '.':
	num*10+getcharAt(i)
loop from '.' till end:
	num+getcharAt(j)/10

## reverse words in sentence 

input=abc def ghi
output =ghi def abc

reverse entire sentence

ihg fed cba
ghi def abc
reverse each string with space as delimiter


#include <stdio.h>

char *dst;
void rev_str(char* s)
{
 
    if(*s != '\0')
         rev_str(s+1); 
 
    
 printf("%c",*s); dst=s[0] dst++
}
 
int main()
{
   rev_str("born2c0de");
   return 0;
}


# b o r n 2 c 0 d e
				  ^
				^
			^
		  ^
		 ^
		^
	  ^
	 ^
  ^

first call stack = b
	second call stack = o 
	..
	kadaisi call stack= e
	e
	

def revstr(str):
	for i in 

def rev_sent(str):
	dst=[]
	dst1=[]
	for i in range(len(str)):
		dst.insert(0,4)
	for j in range(len(dst)):
		c=dst.pop()
		tmp=[]
		tmp1=[]
		if c!=' ':
			tmp.insert(0,c)
		else:
			for k in range(len(tmp)):
				tmp1.append(tmp.pop())
		dst1.append(tmp1)
	return dst1
			

## heap sort

build(array into heap )
sorting():
	if a=del_min(heap)!=-1:
		sort.add(a)
		sorting()

a=[sentinel,1,2,3,4,5,6,7,8,9]
parent=i/2
childs=2i+1,2i+2

del_min(heap):
	tmp=heap.root
	heap.root=heap.tail
	percolate(heap.root)
	return tmp

percolate_down(heap.root):
	if heap.root<heap.chid1:
		swap(heap.root,heap.child1)
		percolate(heap.child1)
	elif heap.root<heap.child2:
		swap(heap.root,heap.child2)
		percolate(heap.child2)
		
percolate_down(heap.tail):
	if heap.tail>heap.parent:
		swap(heap.parent,heap.tail)
		percolate(heap.parent)
		
	
## shell sort

particular displacement  
array a[1..n] 
increment=5
swap(a[1],a[1+increment],a[1+increment+increment])
Sedgewick increment 

Sort an array a[0...n-1].
gaps = [701, 301, 132, 57, 23, 10, 4, 1]
		0		1	2	3	4	5	6	7

		[23,301,132,57,701,10,4,1]
		[132,301,23,57,4,1,701,10]r
		[1,4,10,23,57,132,301,701]
 
foreach (gap in gaps)
    # Do an insertion sort for each gap size.
    for (i = gap; i < n; i += 1)
        temp = a[i]
        for (j = i; j >= gap and a[j - gap] > temp; j -= gap)
            a[j] = a[j - gap]
        a[j] = temp
		
### quick sort

### merge sorts



## binary search

a=[32,442,425,52,5]
a=[1,2,3,4,5]

def find(a,val,i):
	if i>len(a) or i==1:
		return -1
	if a[i]==val:
		return i
	elif a[i] > val:
		i=i/2
		find(a,val,i)
	elif a[i] < val:
		i=i/2+i
		find(a,val,i)

--- C Code for binary search iterative
int find(double searchKey)
{
int lowerBound = 0;
int upperBound = nElems-1;
int curIn;
while(true)
{
curIn = (lowerBound + upperBound ) / 2;
if(v[curIn]==searchKey)
return curIn; //found it
else if(lowerBound > upperBound)
return nElems; //can’t find it
else //divide range
{
if(v[curIn] < searchKey)
lowerBound = curIn + 1; //it’s in upper half
else
upperBound = curIn - 1; //it’s in lower half
} //end else divide range
} //end while
} //end find()

###### Understanding recusrions

#### bit wise 
N,M=0b10000000,0b10101
i,j=2,6
x=0xffff # 111111111111111
M=M<<i # 1010100
for i in range(i,j):
	x=x&(0<<i) # 111111110000111
N=N&x # 10000000
N=N|M
print bin(N)
	
# Decimal Point storage in Binary . Binary division and multiplication

# Next smallest number and largest number given a n bit

N=6 b=110 S=011 L=1001
N=3 b=11 S=011 L=101
N=13 b=1101 S=1011 L=1110

n=3
pos,x,i=[],1,0
while n!=0:
	if n&x !=0: pos.add(i)
	i++
	n=n&x
	x=x<<1
print pos

power of 2? num & num-1 . eg 1000&0111=0
missing element in natural a[1..n] ?
 n(n+1)/2 other number n(n+1)(2n+1)/6 solve x+y and x^2 + y^2 equations 
 
 
## Reverse a digit without duplicates in: 2542 out: 245 
def rev(num):
	rev=0
	a=[0]*10
	while num!=0:
		tmp=num%10
		if a[tmp]==0:
			a[tmp]=1
			rev=rev*10+tmp
		num=num/10
	return rev
		
# sum without +
SUM:
	a=110 b=010
	sum=a^b # 110^010 = 100 # 100 # 1000
	carry=a&b<<1 # 110&010<<1 = 100 # 1000
	a=sum
	b=carry
JNZ SUM

### infix to postfix

infix=1+2*3+(6-5)
postfix=123*+65-+ 

stack= el=1
stack=+ el=12
stack=+* el=12
stack=+* el=123
stack=+*+ el=123 => stack=+ el=123+*
stack=+(	el=123+*
stack=+(	el=123+*6
stack=+(-	el=123+*6
stack=+(-	el=123+*65
stack=+(-)	el=123+*65
stack=+		el=123+*65- # since EOF is reached move all stack elements to expression
stack= el=123*+65-+ 

# C
Operator precedence


1	()   []   ->   .   ::	Grouping, scope, array/member access
2	 !   ~   -   +   *   &   sizeof   type cast ++x   --x  	(most) unary operations, sizeof and type casts
3	*   /   %	Multiplication, division, modulo
4	+   -	Addition and subtraction
5	<<   >>	Bitwise shift left and right
6	<   <=   >   >=	Comparisons: less-than, ...
7	==   !=	Comparisons: equal and not equal
8	&	Bitwise AND
9	^	Bitwise exclusive OR
10	|	Bitwise inclusive (normal) OR
11	&&	Logical AND
12	||	Logical OR
13	 ?:	Conditional expression (ternary operator)
14	=   +=   -=   *=   /=   %=   &=   |=   ^=   <<=   >>=	Assignment operators
15	,	Comma operator

Ascii Values
Pointers - pointer on a function changes local value
macros
bitwise operators - find number of 1's & , swap odd and even bits num&0xaaaaaa<<1 | num&ox5555555>>1 , find unique or not - exor all elements , 

## Operating system

Rentrancy - Multiprogramming -> activation , activation record
Belady's anomaly - Virtual memory -> increase in number of frame nt increases speed
Binary semaphore -> mutual exculsion and concurrent process
thrasshing -> most of time in swapping and less time in processing ( large page faults )
Hoffman's condition -> mutual exclusion , hold and wait , no preemption , circular wait 
scheduler -> long term - multiprogramming , middle term - swapping in and out of real memory , short term - dispatcher which process next
turn around - submission to completion / response time submission to first response
Process- user data / system stack / user program / PCB
Translation Look aside buffer -> virtual memory -> page table entry -> physical memory reduced to single on TLB hit
resident set vs Working set - actual content in real memory to required for execution
safe state - no deadlock
cycle stealing - DMA controller suspends CPU and uses Data bus 
arm stickness - high acces on particular track

## Object oriented Design 

abcd
	
	bacd
	
		abcd
	acbd

	abdc
# Recursions
#### for Mondrian Rectangle

def recMondrian(l,b):
	if l==b:
		print 'l is:',l,' b is :',b
		return l
	else:
		print 'l is:',l,' b is :',b
		return recMondrian(min(l,b),max(l,b)-min(l,b))
	
### binary search
	
def bsearch(arr,pos,data):
	if pos >=len(arr) or arr[pos]==data :
		return pos
	if arr[pos/2]>data:
		return bsearch(arr,(pos/2)+(pos/4),data)
	elif arr[pos/2]<data:
		return bsearch(arr,pos/4,data)

### digit printing

def printNum(num):
	if num<0:
		print('-'),
		printNum(-num)
	elif num<10:
		print(num),
	else:
		printNum(num/10)
		printNum(num%10)
		
def printSimp(num):
	if num>0:
		printSimp(num/10)
		print(num%10),
	elif num<0:
		print('-'),
		printSimp(-num)
		
		
###  add all digits
	
def addDigits(num):
	if num>9:
		return num%10
	else:
		return addDigits(num/10)+addDigits(num%10)
			
		
def digitalRoot(n):
	s=addDigits(n)
	if s>9:
		return addDigits(s)
	else:
		return s

## digital Root

def digitalRoot(num):
	if num<10:
		return num%10
	else:
		 sum=digitalRoot(num/10)+ digitalRoot(num%10)
		 if sum>9:
			sum=digitalRoot(sum)
	return sum
	12131 
	1213
		121
			12
				1 printing 1..
			printing 2 ..
		printing 1 ..
	printing 3 ..
printing 1 ...

### permutation 

def permute(arr,k):
	if k==len(arr):
		print arr
	else:
		for i in range(k,len(arr)):
			arr[i],arr[k]=arr[k],arr[i]
			permute(arr,k+1)
			
my version

def permute(arr,k):
	if k==len(arr):
		print arr
		return arr
	else:
		arr[k-1],arr[k]=arr[k],arr[k-1]
		permute(permute(arr,k+1),k+1)
		
## selection sort

def selection(arr,x,y):
	if x == len(arr)-1 and y == len(arr)-1:
		return arr
	elif arr[x]>arr[y]:
		arr[x],arr[y]=arr[y],arr[x]
	selection(arr,x+1,y)
	selection(arr,x,y+1)
			
			
### find a number where  arr[1..N] where mod(a[k]-a[k+1]) >= 1

def findNum(arr,current,key):
	if current >= len(arr):
		return -1
	elif arr[current]==key:
		return current
	else:
		return findNum(arr,abs(arr[current]-key)+current,key)
		
		
#### printing an array reversely

def reversePrint(arr,pos):
	if pos>=len(arr):
		return 
	else:
		reversePrint(arr,pos+1)
		print arr[pos],
		
		
#### number in mobile 2 - abc , 3 - def ... 9 - wxy
n*3-3 ,n*3-2 , n*3 - 1


### find all the elemtns in Kth height from root node in a binary tree

do BFS till level K 
print all elements in level K

void BFS(node * root, int level, int k, Queue *q)
{
	if level == 1:
		enqueue(root)
		return
	if root ! = NULL and level < = K:
		if level == K-1:
			enqueue(root->right)
			enqueue(root->left)
			return
		else:
			BFS(root->right,level+1,q)
			BFS(root->left,level+1,q)
}

while q!=null:
	print q.dequeue()
	
#### convert huffmans code

input aaaabbbbcccc - a4b4c4

have pointer to 
*p="aaaabbbbcccc"
while p!=null:

	if *p++==*str:
		then  *(str+1)=*(str+1)+1
	else:
		str=str+2
*(str+2)='\0'
print str

Code:

#include<stdio.h>
main()
{
	char *p="aaaaabbbbccc\0",*str,*h;
	h=str=p;
	while(*p!='\0')
	{
		if(*p==*str||(*p<58&&*p>47))
		{
			if(*(str+1)<58&&*(str+1)>47)
				*(str+1)=*(str+1)+1;
			else
				*(str+1)=49;
		}
		else
		{
			str=str+2;
			*(str)=*p;
			*(str+1)=49;
		}
		p++;
	}
	*(str+2)='\0';
	printf("%s",h);
}


##### Braces permutation  n=1 {} n=2 {{}} , {}{} n=3  {}{}{} , {{{}}} , {{}{}} , 

####### Linked list -> next and  -> random clone it

##### kth element in a binary search tree

def inorder(node,k):
	inorder(node.left)
	n=n+1
	if n==k:
		print node 
		return
	inorder(node.right)
	
##### pythagoras triplet in an array

	a^2 + b^2 = c^2
	a=[1,2,3,....N]
	 for given k {2k+1, 2k(k+1), 2k(k+1)+1}
	
######### convert roman to decimal buggy

roman='XIXN'
d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
	
def romToDec(s,k,prev):
	if k+1==len(s) or prev => d[s[k]]:
		return d[s[k]]
	elif prev < d[s[k]]:
		return -d[s[k]]
	else:
		return d[s[k]]+romToDec(s,k+1,s[k])
		
		
#### fibonacci using golden ratio

import math 

def fibn(n):
	fv=math.sqrt(5)
	num=math.floor((1/fv)*(pow(((1+fv)/2),n)-pow(((1-fv)/2),n)))
	return num

	
########## Find division without / operator

a=12 b=9  so a/b=1

def div(a,b,q):
	if b*q <= a:
		return div(a,b,q+1)
	else:
		return q-1

		
	1 2 3 4 5 6
	
	2 4 6 1 3 5
	
##### binary tree to binary search tree

####### binary tree to doubly linked list

#### largest bst in binary tree

##### power of 4
def pow4(n):
	if n==1:
		return True
	elif n==0:
		return False
	elif n & n-1 == 0:
		return pow4(n>>2)
	else:
		return False
####### next largest palindrome of number 127 is 131

#### clone a linked list with next and random pointer

a->b->c->d
------^
   ------^
^-----
         ^
now copy the list linearly 

then have src , src1 , dest , dest1 

traverse from src to dest 
	check des from head to end till it finds the src.dest
	set the src1.dest to dest if it equals
	
for src,src1 in head -> end:
	for dest,dest1 in head -> end:
		if src.dest==dest:
			src1.dest=dest1

######## A tree is mirrored or not

int sameMirroredTree(struct node* a, struct node* b)
{ 
     // 1. both empty -> true 
     if (a==NULL && b==NULL) return(true);
     // 2. both non-empty -> compare them 
     else if (a!=NULL && b!=NULL) 
     { 
       return( 
                  a->data == b->data && 
                              sameMirroredTree(a->left, b->right) && 
                              sameMirroredTree(a->right, b->left) 
              ); 
      }
      else
      return false; 
}
### oneliner
bool IsMirror(Node* me, Node* myMirror)
{
       return ( (me != NULL && myMirror != NULL) && (me.Value == myMirror.Value) && IsMirror(me->Left, myMirror->Right) &&IsMirror(me->Right, myMirror->Left) &&);
}

###### Intersection of two linked lists

(1)take 2pointers initialize to head of the list
(2)increment both pointer till they reach end of the list and calculate list length l1,l2
(3) calculate absolute difference between l1-l2 ie n=|l1-l2|
(4) calculate nth element from end of the list.



