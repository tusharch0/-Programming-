#include <bits/stdc++.h>
using namespace std;

class tree{    
	public:
		int data;
		tree *left;
		tree *right;
};

class sll{
    public:
    int data;
    sll* next;
};

sll* creatnode(int d){ 
	sll* temp=(sll*)malloc(sizeof(sll));
	temp->data=d;
	temp->next=NULL;
	return temp;
}

void display(sll* head){
	sll* current=head; 

	printf("displayig the converted list...\n");
	while(current!=NULL){ 
	    if(current->next)
		printf("%d->",current->data);
		else
		printf("%d->NULL\n",current->data);
		current=current->next; 
	}
}

sll* flatten(tree* root)
{
	sll* head=NULL,*tempL;
	queue<tree*> q;
	q.push(root);
	vector<int> store;

	tree* temp;
	while(!q.empty()){
		temp=q.front();
		q.pop();
		if(head==NULL){
		    head=creatnode(temp->data);
		    tempL=head;
		}
		else{
		    tempL->next=creatnode(temp->data);
		    tempL=tempL->next;
		}
		
		if(temp->left)
			q.push(temp->left);
		if(temp->right)
			q.push(temp->right);
		
	}
	
	
	return head;

}

tree* newnode(int data) 
{ 
	tree* node = (tree*)malloc(sizeof(tree)); 
	node->data = data; 
	node->left = NULL; 
	node->right = NULL; 

	return(node); 
} 


int main() 
{ 
	cout<<"same tree is built as shown in example\n";
	tree *root=newnode(2); 
	root->left= newnode(7); 
	root->right= newnode(5); 
	root->right->right=newnode(9);
	root->right->right->left=newnode(4);
	root->left->left=newnode(2); 
	root->left->right=newnode(6);
	root->left->right->left=newnode(5);
	root->left->right->right=newnode(11);

	cout<<"converting the tree into a single link list...\n";
	cout<<"by traversing the tree level-wise\n";
	sll* head=flatten(root);
	display(head);

	return 0; 
} 
