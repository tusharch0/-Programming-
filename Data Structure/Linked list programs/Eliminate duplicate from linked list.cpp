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

Node *removeDuplicate(Node* head){
	Node *temp = head;
	while(temp->next != NULL && temp != NULL){
		if(temp->data == temp->next->data){
			temp -> next = temp ->next ->next;
		}
		else{
			temp = temp->next;
		}
	}
	return head;
}

int main(){
	Node * head = createNewLL();
	cout<<"The linked list is"<<endl;
	printLL(head);

	head = removeDuplicate(head);
	cout<<"The new Linked List is" <<endl;
	printLL(head);

	return 0;
}
