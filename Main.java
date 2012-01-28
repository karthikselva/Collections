public class Main
{
	public static void main(String args[]) 
	{
		Stack s=new Stack();
		for(int i=0;i<10;i++)
			s.push(i);
		s.display();
		for(int i=0;i<10;i++)
		{
			System.out.println(s.Sdeq());
		}
	}
}

class List<Type> 
{
	Type data;
	List next;
	
	List()
	{
		data=null;
		next=null;
	}
	
	public List insert_begin(Type data)
	{
		List<Type> head=this.next;
		if(head==null)
		{
			head=new List();
			head.data=data;
			this.next=head;
			return head;
		}
		
		List<Type> nextlist=new List();
		nextlist.data=data;
		nextlist.next=this.next;
		this.next=nextlist;
		return head;
	}
	
	public List insert_pos(Type data,int pos)
	{
		List lpos=this.next;
		int count=0;
		while(lpos!=null&&count+1!=pos)
		{
			lpos=lpos.next;
			count=count+1;
		}	
		
		if(lpos==null)
			return this;
		List<Type> nextlist=new List();
		nextlist.data=data;
		List swap=lpos.next;
		lpos.next=nextlist;
		nextlist.next=swap;
		return this;
	}
	
	public List insert_end(Type data)
	{
		List tail=this.next;
		while(tail.next!=null)tail=tail.next;
		List nextlist=new List();
		nextlist.data=data;
		tail.next=nextlist;
		tail=nextlist;
		return this;
	}
	
	public Type delete_last()
	{
		List traverse=this.next;
		if(traverse.next==null)
			{
				Type data=(Type)traverse.data;
				this.next=null;
				return (Type)traverse.data;
			}
		while(traverse.next!=null&&traverse.next.next!=null)traverse=traverse.next;
		Type tmp=(Type)traverse.next.data;
		traverse.next=null;
		return tmp;
	}
	/*
	void bubblesort()
	{
		
		List traverse=this;
		while(traverse!=null)
		{
			List start=this;
			while(start.next!=null)
			{
				if(start.data>start.next.data)
				{
					int tem=start.data;
					start.data=start.next.data;
					start.next.data=tem;
				}
				start=start.next;
			}
			traverse=traverse.next;
		}
	}*/
	
	public void display()
	{
		List traverse=this.next;
		while(traverse!=null)
		{
			System.out.print(traverse.data+"->");
			traverse=traverse.next;
		}
		System.out.print("NULL \n");
	}
	
	public List findLoop()
	{
		List hare=this.next;
		List tortoise=this.next;
		while(hare.next!=null&&tortoise.next!=null&&hare.next.next!=null)
		{
			hare=hare.next.next;
			tortoise=tortoise.next;
			if(hare==tortoise)
				return hare;
		}
		hare=null;
		return hare;
	}
	
	public int hasLoop()
	{
		List hare=this.next;
		List tortoise=this.next;
		while(hare.next!=null&&tortoise.next!=null&&hare.next.next!=null)
		{
			hare=hare.next.next;
			tortoise=tortoise.next;
			if(hare==tortoise)
				return 1;
		}
		return -1;
	}
	
	public List ptrOf(Type data)
	{
		List traverse=this.next;
		while(traverse.next!=null&&traverse.data!=data)
		traverse=traverse.next;
		return traverse;
	}
	
	public int makeLoop(List src)
	{
		List loop=this.next;
		while(loop.next!=null)loop=loop.next;
		loop.next=src;
		return 1;
	}
	
	public int removeLoop()
	{
		List hare=this.findLoop();
		if(hare==null)
			return -1;
		List tortoise=this.next;
		while(hare.next!=tortoise.next)
		{
			System.out.println(" Hare "+hare.data);
			System.out.println(" Tortoise "+tortoise.data);
			hare=hare.next;
			tortoise=tortoise.next;
		}
		hare.next=null;
		
		return 1;
	}
	
	public List merge(List second)
	{
		List one=this.next;
		second=second.next;
		List tmp1=one.next;
		List tmp2=second.next;
		while(one.next!=null&&second.next!=null)
		{
			one.next=second;
			second.next=tmp1;
			one=tmp1;
			second=tmp2;
			tmp1=one.next;
			tmp2=second.next;
		}
		if(second.next!=null)
			one.next=second;
		if(one.next!=null)
		{
			List tmp=one.next;
			one.next=second;
			second.next=tmp;
		}
		
		return this;
	}
}

class Stack<Type> extends List
{
	int length=0;
	int deq=0;
	Stack()
	{
		super();
	}
	
	List push(Type data)
	{
		length=length+1;
		return insert_begin(data);
	}
	
	Type pop()
	{
		Type data=null;
		length=length-1;
		try
		{
		List head=this.next;
		data=(Type)head.data;
		this.next=this.next.next;
		return data;
		}
		catch(Exception e)
		{
			length=length+1;
			System.out.println(" POP failed No data ");
			return data;
		}
	}
	Type peek()
	{
		if(this.next!=null)
			return (Type)this.next.data;
		return null;
	}
	
	int getlength()
	{
		return length;
	}
	/*
	void sortStackWithStack()
	{
		Stack tmp=new Stack();
		while(this.peek()!=null)
		{
			Integer data=(Integer)this.pop();
			while(((Integer)tmp.peek().)intValue()==null||data.intValue()>((Integer)tmp.peek()).intValue())
			{
				this.push(tmp.pop());
			}
			tmp.push(data);
		}
	} */
	
	void reverse()
	{
		return;
	}
	
	int evalExpr(String expr)
	{
		String tmp="";
		int Result=0;
		for(char c:expr.toCharArray())
		{
			if(c>47&&c<57)
			{
				tmp=tmp+c+"";
				continue;
			}
			this.push((Type)tmp);
			tmp="";
			this.push((Type)(c+""));
			
		}
		if(!tmp.equals("")) this.push((Type)tmp);
		return Result;
	}
	
	boolean getPrecedence(char operator1,char operator2)
	{
		
		return false;
	}
	
	int operatorPrecedence(char operator)
	{
		switch(operator)
		{
		case '+':
			return 15;
		}
		return -1;
	}
	
	Type Sdeq()
	{
		Stack s=new Stack();
		Type data=null;
		while(this.next!=null&&deq==0)
		{
			s.push(this.pop());
		}
		if(this.next==null)
		{
			data=(Type)s.pop();
			this.next=s.next;
			deq=1;
		}
		else
		{
			data=(Type)this.pop();
			if(this.next==null) deq=0;
		}
	return data;
	}
}

class Queue<Type> extends List
{
	Queue()
	{
		super();
	}
	
	List enq(Type data)
	{
		return insert_begin(data);
	}
	
	Type deq()
	{
		return (Type)delete_last();
	}
	
	boolean isEmpty()
	{
		if(this.next==null) return true;
		return false;
	}
	
	Type Qpop()
	{
		Queue second=new Queue();
		Queue head=this;
		while(head.next.next!=null)
		{
			second.enq(head.deq());
		}
		Type data=(Type)head.deq();
		this.next=second.next;
		return data;
	}
}

class Edges<Type> extends List
{
	Edges()
	{
		super();
	}
	int weight;
	boolean visited;
	Edges<Type> next;
}

class Graph<Type> 
{
	Type data;
	Graph<Type> Vertex=null;
	Edges<Type> Edge=null;
	Type Data=null;
	boolean visited=false;
	Graph()
	{
		
	}
	Graph addVertex(Type node)
	{
		Graph<Type> NewGraph=new Graph();
		NewGraph.data=node;
		Graph End=this.Vertex;
		while(End!=null&&End.Vertex!=null)End=End.Vertex;
		End=NewGraph;
		NewGraph.Vertex=this;
		return End;
	}
	void addEdge(Type Src,Type Dest,int weight)
	{
		Graph Origin=this;
		while(Origin!=null&&Origin.data!=Src)
			Origin=Origin.Vertex;
		if(Origin==null)
			return;
		Edges Pos=Origin.Edge;
		if(Pos==null)
		{
			Pos=new Edges();
			Pos.data=Dest;
			Pos.weight=weight;
			Origin.Edge=Pos;
			return;
		}
		while(Pos.next!=null)
			Pos=Pos.next;
		Pos.next=new Edges();
		Pos.next.data=Dest;
		Pos.next.weight=weight;
		Pos.next.next=null;
		
	}
	
	
	void display()
	{
		Graph<Type> Cursor=this;
		while(Cursor!=null&&Cursor.data!=null)
		{
			System.out.print(Cursor.data+" =>");
			Edges Edge=Cursor.Edge;
			while(Edge!=null)
			{
				System.out.print(Edge.data+" Distance: "+Edge.weight+" | ");
				Edge=Edge.next;
			}
			System.out.println("null");
			Cursor=Cursor.Vertex;
		}
		
	}
	
	List getNear(Type d)
	{
		
		Graph Traverse=this;
		while(Traverse.data!=d&&Traverse.Vertex!=null)
		{
			Traverse=Traverse.Vertex;
		}
	return Traverse.Edge;
	}
	
	boolean isReachable(Type Src,Type Dest)
	{
		Graph Traverse=this;
		while(Traverse.data!=Src&&Traverse.Vertex!=null)
		{
			Traverse=Traverse.Vertex;
		}
		if(Traverse==null)
			return false;
		Edges W=Traverse.Edge;
		while(W!=null&&W.data!=Dest)
			W=W.next;
		if(W!=null&&W.data==Dest)
			return true;
		return false;
	}
	
	
}

class HashMap
{
	int Size=2;
	int Data[];
	
	HashMap()
	{
		Size=Number.nextPrime(Size);
		Data=new int[Size];
	}
	
	int put(int data)
	{
		if(data%Size>Size)
			this.rehash();
		if(Data[data%Size]==0)
		{
			Data[data%Size]=data;
			Size=Size+1;
		}
		return 1;
	}
	
	int rehash()
	{
		Size=Number.nextPrime(Size);
		Data=new int[Size];
		return 1;
	}
	void display()
	{
		for(int i=0;i<Size;i++)
		{
			if(Data[i]!=0)
				System.out.println(" Data["+i+"] => "+Data[i]);
		}
	}
}

class Heap 
{
	int Data[];
	int Size=4;
	int Last=0;
	int Head=1;
	boolean heap=false; // min heap | to make it max heap give heap=true;
	Heap()
	{
		Data=new int[Size];
	}
	
	Heap(boolean set)
	{
		Data=new int[Size];
		heap=set;
	}
	
	int deleteMin()
	{
		if(Head >Last) return -1;
		int data=Data[Head];
		Data[Head]=Data[Last];
		Data[Last]=65535;
		Last=Last-1;
		percolateDown(Head);
		return data;
	}
	
	void initHeap()
	{
		for(int i=Head;i<Data.length;i++)
		{
			if(Data[i]==0)
				Data[i]=65535;
		}
	}
	int insert(int data)
	{
		Last=Last+1;
		if(Last+1>Data.length)
			Data=(int[])resizeArray(Data,2*Last); // Resize Heap
		initHeap();
		Data[Last]=data;
		percolateUp(Last);
		return 1;
	}
	
	void percolateUp(int Last)
	{
		if(Last==Head||Data[Last]==Data[Last/2]) return;
		if(Data[Last]<Data[Last/2])
			swap(Last,Last/2);
		percolateUp(Last/2);
	}
	
	void percolateDown(int Head)
	{
		int Tail=Last;
		if(Head>=Last||Head*2>Last&&Head*2+1>Last)
			return;
		if(Data[Head*2]>Data[Head*2+1])
			Tail=Head*2+1;
		else
			Tail=Head*2;
		 if(Data[Tail]<Data[Head])
		{
			swap(Tail,Head);
		}
		percolateDown(Tail);
	}
	
	void swap(int Elem1,int Elem2)
	{
		int tmp=Data[Elem1];
		Data[Elem1]=Data[Elem2];
		Data[Elem2]=tmp;
	}
	
	private static Object resizeArray (Object oldArray, int newSize) 
	{
	   int oldSize = java.lang.reflect.Array.getLength(oldArray);
	   Class elementType = oldArray.getClass().getComponentType();
	   Object newArray = java.lang.reflect.Array.newInstance(
			 elementType,newSize);
	   int preserveLength = Math.min(oldSize,newSize);
	   if (preserveLength > 0)
		  System.arraycopy (oldArray,0,newArray,0,preserveLength);
	   return newArray; 
   }
   
   void display()
   {
		int space=Data.length;
		System.out.println(" Displaying Heap : \n");	
		for(int i=1;i<Data.length;i=2*i)
		{
			for(int j=0;j<i;j++)
			{
				for(int x=0;x<space>>2;x++)
					System.out.print("  ");
			if(Data[i+j]==65535) break;
				System.out.print(Data[i+j]+" ");
			}
			space=space>>1;
			System.out.println("\n");
		}
	}
	
}

class Number
{
	int Num;
	
	Number(int Num)
	{
		this.Num=Num;
	}
	
	int gcd(int Other)
	{
		return gcdCalc(max(this.Num,Other),min(this.Num,Other));
	}
	
	int gcdCalc(int N1,int N2)
	{
		if(N2==0)
			return N1;
		return gcdCalc(N2,N1%N2);
	}
	
	int lcm(int Other)
	{
		
		return (this.Num*Other)/gcdCalc(max(this.Num,Other),min(this.Num,Other));
	}
	
	boolean isPrime()
	{
		int count=0;
		for(int i=2;i<this.Num;i++)
		{
			if(this.Num%i==0)
				return false;
		}
		return true;
	}
	
	public static int nextPrime(int num)
	{
		for(int i=num+1;;i++)
		{
			Number tmp=new Number(i);
			if(tmp.isPrime())
			{
				return i;
			}
		}
	}
	
	int min(int N1,int N2)
	{
		if(N1<N2) 
			return N1;
		return N2;
	}
	
	int max(int N1,int N2)
	{
		if(N1>N2) 
			return N1;
		return N2;
	}
	
	int random()
	{
		return 1;
	}
	
	public static int stringToInt(String Value)
	{
		int Result=0;
		for(char c:Value.toCharArray())
			Result=Result*10+(c-48);
		System.out.println(Result);
		return Result;
	}
	
	int reverse()
	{
		int tmp=0,num=this.Num;
		while(num!=0)
		{
			tmp=tmp*10+(num%10);
			num=num/10;
		}
		return tmp;
	}
	
	float sqrt()
	{	
		int Near=calcSqrt(1);
		int Rem=(this.Num-Near*Near)*100;
		int Mantissa=0;
		int tmp=Near;
		for(int i=0;i<6;i++)
		{
			int res[]=calcDecimal(Rem,tmp);
			tmp=res[0];
			System.out.println(res[0]+"  "+res[1]+"  "+res[2]);
			Mantissa=res[1]+Mantissa*10;
			Rem=Rem*100;
			
		}
		System.out.println(Near+"."+Mantissa);
		return 1.0F;
	}
	
	int calcSqrt(int num)
	{
		if(this.Num-num*num<1)
			return num-1;
		else 
			return calcSqrt(num+1);
	}
	
	int[] calcDecimal(int rem,int num)
	{
		int tmp=1;
		while(true)
		{
			int res[]=new int[3];
			int n=num*2;
			n=n*10 + tmp;
			int n1=n*tmp;
			res[0]=(n-1)*(tmp-1);
			res[1]=tmp-1;
			res[2]=rem-(n-1)*(tmp-1);
			System.out.println(" n is "+n+" tmp is "+tmp);
			if(rem-n1<0)
				return res;
			tmp++;
		}
	}
	
	int factorial()
	{
		return factorialRec(this.Num);
	}
	
	int factorialRec(int num)
	{
		if(num==1)
			return 1;
		else 
			return num*factorialRec(num-1);
	}
	
	int factorialIter(int num)
	{
		int tmp=1;
		for(int i=1;i<num+1;i++)
		{
			tmp=i*tmp;
		}
		return tmp;
	}
	
	int fibonacci()
	{
		return fibonacciRec(this.Num);
	}
	
	int fibonacciRec(int num)
	{
		if(num==1||num==0)
			return 1;
		else 
			return fibonacciRec(num-1)+fibonacciRec(num-2);
	}
	
	int fibonacciIter(int num)
	{
		int a=0,b=1,c=0;
		for(int i=0;i<num;i++)
		{
			a=b;
			b=c;
			c=a+b;
		}
		return c;
	}
	
	int countSetbits()
	{
		int one=1,count=0;
		for(int i=0;i<32;i++)
		{
			if((one&this.Num)!=0)
				count=count+1;
			one=one<<1;
		}
		return count;
	}
	
	int swapOddEven()
	{
		int odd=this.Num&0xaaaaaaaa;
		int even=this.Num&0x55555555;
		return (odd>>1|even<<1);
	}
	
	String toBin()
	{	
		return toBase(2);
	}
	
	String toOct()
	{	
		return toBase(8);
	}
	
	String toHex()
	{
		return toBase(16);
	}
	
	String toBase(int base)
	{
		int num=this.Num;
		int res=0;
		String result="";
		while(num!=0)
		{
			res=num%base;
			num=num/base;
			result=choice(res)+result;
		}
		return result;
	}
	
	char choice(int res)
	{
		switch(res)
		{
			case 10:
				return 'A';
			case 11:
				return 'B';
			case 12:
				return 'C';
			case 13:
				return 'D';
			case 14:
				return 'E';
			case 15:
				return 'F';
			default:
				return (char)(res+48);
		}
	}
			
	
}

class Hanoi 
{
	int NumDisc=0;
	String Discs="";
	char Source='A';
	char Dest='C';
	char Tmp='B';
	
	Stack s[];
	
	Hanoi(int Num)
	{
		NumDisc=Num;
		for(int disc=0;disc<NumDisc;disc++)
			Discs+=(char)(disc+65)+"";
		s=new Stack[NumDisc];
	}
	
	int setSrc(char Src)
	{
		Source=Src;
		return 1;
	}
	
	int setDest(char Dest)
	{
		this.Dest=Dest;
		return 1;
	}
	
	int setTmp(char Tmp)
	{
		this.Tmp=Tmp;
		return 1;
	}

	void move(char Src,char Dest,char Tmp,int NumDisc)
	{	
		if(NumDisc==1)
		{
			System.out.println(" Moving From "+Src+" To "+Dest);
			return;
		}
		move(Src,Tmp,Dest,NumDisc-1);
		System.out.println(" Moving From "+Src+" To "+Dest);
		move(Tmp,Dest,Src,NumDisc-1);
	}
	
	int startMove()
	{
		move(Source,Dest,Tmp,NumDisc);
		return 1;
	}
	
	void discs()
	{
		System.out.println(Discs);
	}
}	


class BST 
{

	BST Right=null;
	BST Left=null;
	int Data=-1;

	BST()
	{
		
	}
	
	int insert(int data)
	{
		this.Right=insertBST(data,this.Right);
		return 1;
	}
	
	BST insertBST(int data,BST root)
	{
		if(root==null)
		{	
			root=new BST();
			root.Data=data;
			System.out.println("inserting "+data);
			return root;
		}
		else if(data>root.Data)
			root.Right=insertBST(data,root.Right);
		else if(data<root.Data)
			root.Left=insertBST(data,root.Left);
		return root;
	}
	
	void inorder()
	{
		System.out.println(" ######## In Order ");
		inorderTraversal(this.Right);
	}
	void inorderTraversal(BST node)
	{
		if(node==null) return;
		inorderTraversal(node.Left);
		System.out.println(" "+node.Data);
		inorderTraversal(node.Right);
	}
	
	void preorder()
	{
		System.out.println(" ######## Pre Order ");
		preorderTraversal(this.Right);
	}
	
	void preorderTraversal(BST node)
	{
		if(node==null) return;
		System.out.println(" "+node.Data);
		inorderTraversal(node.Left);
		inorderTraversal(node.Right);
	}
	
	void postorder()
	{
		System.out.println(" ######## Post Order ");
		postorderTraversal(this.Right);
	}
	void postorderTraversal(BST node)
	{
		if(node==null) return;
		inorderTraversal(node.Left);
		inorderTraversal(node.Right);
		System.out.println(" "+node.Data);
	}
	
	void BFS()
	{
		Queue<Integer> q=new Queue();
		q.enq(this.Right.Data);
		dispBFS(this.Right,q);
	}
	
	void dispBFS(BST root,Queue q)
	{
		Integer tmp=0;
		if((tmp=(Integer)q.deq())!=null) System.out.println(" Reached here "+tmp.intValue());
		if(root.Right==null)return;
		q.enq(root.Right.Data);
		q.enq(root.Left.Data);
		dispBFS(root.Right,q);
		
	}
	
	int maxheight()
	{
		BST head=this.Right;
		return calcMaxHeight(head);
	}
	
	
	int calcMaxHeight(BST root)
	{
		if(root==null)return 0;
		return 1+max(calcMaxHeight(root.Right),calcMaxHeight(root.Left));
	}
	
	
	int minheight()
	{
		BST head=this.Right;
		return calcMinHeight(head);
	}
	
	
	int calcMinHeight(BST root)
	{
		if(root==null)return 0;
		return 1+min(calcMinHeight(root.Right),calcMinHeight(root.Left));
	}
	int max(int n1,int n2)
	{
		if(n1>n2) 
			return n1;
		return n2;
	}
	
	int min(int n1,int n2)
	{
		if(n1<n2) 
			return n1;
		return n2;
	}
	
	boolean isBalanced()
	{
		if(this.maxheight()-this.minheight()>1)
			return false;
		return true;
	}
	
	void display()
	{
		BST root=this.Right;
		int Space=1<<this.maxheight();
		System.out.println("##### Displaying Tree : \n");
		Queue<BST> q=new Queue();
		q.enq(root);
		recDisplay(root,Space,q);
	}
	void dispSpace(int Space)
	{
		for(int i=0;i<Space;i++)
		System.out.print(" ");
	}
	void recDisplay(BST root,int Space,Queue q)
	{
		if(root==null) return;

			while(!q.isEmpty())
			{
				BST tmp=(BST)q.deq();
				dispSpace(Space);
				if(tmp!=null)System.out.print(tmp.Data);
			}
			System.out.println();
			q.enq(root.Right);
			q.enq(root.Left);
			recDisplay(root.Right,Space>>1,q);
			recDisplay(root.Left,Space>>1,q);

	}
	
}

class Sorting 
{

	int Data[];
	
	Sorting(int Range)
	{
		Data=new int[Range];
		for(int i=1;i<Range+1;i++)
			Data[i-1]=i;
	}
	
	
	int bubbleSort()
	{
		int Iterations=0;
		for(int index1=0;index1<Data.length;index1++)
		{
			for(int index2=index1;index2<Data.length;index2++)
			{
				if(Data[index1]>Data[index2])
					swap(index1,index2);
				Iterations++;
			}
		}
		return Iterations;
	
	}
	
	int insertionSort()
	{
		int Iterations=0;
		for(int Index=1;Index<Data.length;Index++)
		{
			int Element=Data[Index];
			int Start=Index-1;
			while(Start>=0&&Data[Start]>Element)
			{
				swap(Start,Start+1);
				Start=Start-1;
				Iterations++;
			}
			Data[Start+1]=Element;
		}
		return Iterations;
	}
	
	int quickSort()
	{
	
		return 1;
	}
	
	int mergeSort()
	{
		return 1;
	}
	
	int selectionSort()
	{
		int Iterations=0;
		int MinIndex=0;
		
		for(int Index1=0;Index1<Data.length;Index1++)
		{
			for(int Index2=Index1;Index2<Data.length;Index2++)
			{
				if(Data[Index2]<Data[MinIndex])
				{
					MinIndex=Index2;
				}
				Iterations++;
			}
			swap(MinIndex,Index1);
		}
		
		return Iterations;
	}
	int heapSort()
	{
		Heap sort=new Heap();
		
		for(int i=0;i<Data.length;i++)
			sort.insert(Data[i]);
		for(int i=0;i<Data.length;i++)
			Data[i]=sort.deleteMin();		
		return 1;
	}
	
	int pigeonSort()
	{
		int Pigeon[]=new int[Data.length];
		for(int d:Data)
		{
			Pigeon[d-1]+=1;
		}
		Data=Pigeon;
		return 1;
	}
	
	int findValue(int data)
	{
		int right=Data.length-1;
		int left=0;
		int mid=0;
		while(left<=right)
		{
			mid=(right+left)/2;
			if(data>Data[mid])
			{
				left=mid+1;
			}
			else if(data<Data[mid])
			{
				right=mid-1;
			}
			if(data==Data[mid])
				return mid;
		}
		
		return -1;
	}
			
	
	int shuffle()
	{
		for(int i=1;i<Data.length;i++)
			swap((int)(Math.random()*pow(10,9)%Data.length),i);
		return 1;
	}
	
	int negShuffle()
	{
		int minus=1;
		for(int i=1;i<Data.length;i++)
		{
			minus=minus*(-minus);
			Data[i]=minus*Data[i];
			swap((int)(Math.random()*pow(10,9)%Data.length),i);
		}
		return 1;
	}
	
	int maxSubseq()
	{
		int maxsofar=0;
		int maxendinghere=0;
		for(int i=0;i<Data.length;i++)
		{
			maxendinghere=max(maxendinghere+Data[i],0);
			maxsofar=max(maxsofar,maxendinghere);
		}
		return maxsofar;
	}
	
	int max(int num1,int num2)
	{
		if(num1>num2)
			return num1;
		return num2;
	}
	int swap(int x1,int x2)
	{
		int tmp=Data[x1];
		Data[x1]=Data[x2];
		Data[x2]=tmp;
		return 1;
	}
	
	int pow(int num,int raise)
	{
		int res=1;
		for(int i=1;i<raise;i++)
			res=res*num;
		return res;
	}
	
	void display()
	{
		System.out.println();
		int flag=0;
		for(int i=0;i<Data.length;i++)
			System.out.print(" "+Data[i]);
		System.out.println();
	}
	
}


class KString 
{
	private String Data="";
	
	KString(String S)
	{
		this.Data=S;
	}
	
	boolean findRotation(String s)
	{
		return isSubstring(s+s);
	}
	
	boolean isSubstring(String s)
	{
		int count=0;
		for(char c:s.toCharArray())
		{
			if(count<Data.length()&&c==Data.charAt(count))
			{
				count++;
				if(count==Data.length())
					return true;
			}
			else
				count=0;
		}
		return false;
	}

	void printReverse()
	{
		System.out.println(reverse());
	}
	
	String reverse()
	{
		Stack<Character> s=new Stack();
		String Tmp="";
		for(int i=0;i<Data.length();i++)
		{
			s.push(Data.charAt(i));
		}
		for(int i=0;i<Data.length();i++)
		{
			Tmp+=s.pop()+"";
		}
		return Tmp;
		
	}
	
	String deleteSet(String set)
	{
		int Source,Destination=0;
		StringBuilder Result=new StringBuilder(this.Data);
		for(Source=0;Source<Data.length();Source++)
		{
			int flag=0;
			for(int setIndex=0;setIndex<set.length();setIndex++)
			{
				if(Result.charAt(Source)==set.charAt(setIndex))
				{
					flag=1;
					break;
				}
				
			}
			if(flag==0)
			{
			Result.setCharAt(Destination,Result.charAt(Source));
			Destination++;
			}
		}
		for(;Destination<Data.length();Destination++)
		{
			Result.setCharAt(Destination,' ');
			
		}
		return Result.toString();
	}
}

class Trie
{
	char value=' ';
	Trie child=null;
	Trie sibling=null;
	
	Trie()
	{
		
	}
	int insert(String s)
	{
		for(char c:s.toCharArray())
		{
			if(this.child==null)
			{
				this.child=new Trie();
				this.value=c;
							System.out.println(" inserting new root ");

			}
			else
			{
				Trie sib=this.sibling;
				while(sib!=null)sib=sib.sibling;
				sib=new Trie();
				sib.value=c;
				sib.child=null;
							System.out.println(" inserting sibling ");

			}
		}
		return 1;
	}
			
	void display()
	{
		System.out.println(".");
		Trie child=this.child;
		Trie sib=this.sibling;
		while(sib!=null)
		{
			System.out.print(sib.value);
			sib=sib.sibling;
		}
		
	}
}