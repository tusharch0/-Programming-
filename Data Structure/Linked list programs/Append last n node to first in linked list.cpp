#include<bits/stdc++.h>

using namespace std;

struct Node{
	int data;
	Node * next;
};

Node *newNode(int k){ 
	Node *temp = (Node*)malloc(sizeof(Node)); 
	temp->data = k; 
	temp->next = NULL; 
	return temp; 
}

Node *addNode(Node* head, int k){
	if(head == NULL){
		head = newNode(k);
	}
	else{
		Node * temp = head;
		Node * node = newNode(k);
		while(temp->next!= NULL){
			temp = temp->next;
		}
		temp-> next = node;
	}

	return head;
}

Node *createNewLL(){
	int cont = 1;
	int data;
	Node* head = NULL;
	while(cont){
		cout<<"Enter the data of the Node"<<endl;
		cin>>data;
		head = addNode(head,data);
		cout<<"Do you want to continue?(0/1)"<<endl;
		cin>>cont;
	}
	return head;
}

void *printLL(Node * head){
	while(head!= NULL){
		cout<<head->data<<"->";
		head = head-> next;
	}
	cout<<"NULL"<<endl;
}

Node *appendNNodes(Node* head, int n){
	Node *temp = head, *t = head;           
	int i = -n;                             
	while(temp->next!=NULL){
		if(i>=0){                          
			t = t->next;
		}
		temp = temp ->next;
		i++;
	}
	temp->next = head;         
	head = t->next;                   
	t->next = NULL;                         

	return head;
}

int main(){
	Node * head = createNewLL();
	cout<<"The linked list is"<<endl;
	printLL(head);
	int data;
	cout<<"Enter the number of nodes you want to append."<<endl;
	cin>>data;
	head = appendNNodes(head,data);
	cout<<"The new Linked List is" <<endl;

	printLL(head);
	return 0;
}
