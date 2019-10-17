#include<iostream>
#include<stack>
using namespace std;

/*structure to store a BST*/
struct node       
{
	int info;
	node *left,*right;
};

/*Method to create a newNode if a tree does not exist*/
node *newNode(int n)  
{
	node *ptr=new node;
	ptr->info=n;
	ptr->left=ptr->right=NULL;
	return ptr;
}

/*Method to insert given node in the BST */
node *insert(node* node,int info)  
{
	if(node==NULL)
	{
		return newNode(info);
	}
	if(info < node->info)          
	{
		node->left=insert(node->left,info);
	}
	else
	{
		node->right=insert(node->right,info);
	}
	return node;
}

/*Method to print postorder traversal of a BST*/
void postorder(node *root)             
{
	stack<node*> post;
	post.push(root);
	
	stack<int> pout;
	while(!post.empty())
	{
		node *curr=post.top();
		post.pop();
		pout.push(curr->info);
		
		if(curr->left)
		{
			post.push(curr->left);
		}
		if(curr->right)
		{
			post.push(curr->right);
		}
	}
	cout<<"PostOrder traversal :";
	while(!pout.empty())
	{
		cout<<pout.top()<<" ";
		pout.pop();
	}
}

//Main program
int main()
{
	node* root=newNode(60);
	
	insert(root,50);
	insert(root,70);
	insert(root,40);
	insert(root,30);
	insert(root,80);
	insert(root,75);
	insert(root,65);
	insert(root,45);
	insert(root,55);
	insert(root,90);
	insert(root,67);
	
	/*Call/invoke statement for postorder method*/
	postorder(root);            
	
	cout<<endl;
	
	return 0;	
}
