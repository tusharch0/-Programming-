#include <bits/stdc++.h>
using namespace std;

// tree node is defined
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

sll* creatnode(int d){ //create node for single linked list
	sll* temp=(sll*)malloc(sizeof(sll));
	temp->data=d;
	temp->next=NULL;
	return temp;
}

void display(sll* head){
	sll* current=head; // current node set to head

	printf("displaying the converted list...\n");
	while(current!=NULL){ //traverse until current node isn't NULL
	    if(current->next)
		printf("%d->",current->data);
		else
		printf("%d->NULL\n",current->data);
		current=current->next; // go to next node
	}
}

sll* flatten(tree* root)
{
	//Declare queue using STL
	sll* head=NULL,*tempL;
	queue<tree*> q;
	//enqueue the root
	q.push(root);
	vector<int> store;

	tree* temp;
	//do the level order traversal & build single linked list
	while(!q.empty()){
		//dequeue
		temp=q.front();
		q.pop();
		if(head==NULL){//for inserting first node
		    head=creatnode(temp->data);
		    tempL=head;
		}
		else{//for inserting rest of the nodes
		    tempL->next=creatnode(temp->data);
		    tempL=tempL->next;
		}

		// do level order traversing
		if(temp->left)//for left child
			q.push(temp->left);
		if(temp->right)//for right child
			q.push(temp->right);

	}


	return head;

}

tree* newnode(int data)  // creating new node for tree
{
	tree* node = (tree*)malloc(sizeof(tree));
	node->data = data;
	node->left = NULL;
	node->right = NULL;

	return(node);
}


int main()
{
	//**same tree is built as shown in example**
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
	//displaying the list built from the tree
	display(head);

	return 0;
}
