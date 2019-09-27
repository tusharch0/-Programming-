#include<bits/stdc++.h>
using namespace std;

class node{
    public:
	int data; 
	struct node *next;
};

void display(class node* head){
	node* current=head; 
	while(current!=NULL){ 
		printf("%d ",current->data);
		current=current->next; 
	}
}

node* creatnode(int d){
	node* temp=(node*)malloc(sizeof(node));
	temp->data=d;
	temp->next=NULL;
	return temp;
}
node* mergeList(node* split1,node* split2){
    
    node* newhead=NULL;
    if(split1==NULL)
    return split2;
    if(split2==NULL)
    return split1;
    
    if(split1->data<=split2->data){
        newhead=split1;
        newhead->next=mergeList(split1->next,split2);
    }
    else{
        newhead=split2;
        newhead->next=mergeList(split1,split2->next);
    }
    
    
    return newhead;
    
}



void splitList(node* head,node** split1,node** split2){
    
    node* slow=head;
    node* fast=head->next;
    
    while(fast!=NULL){
        fast=fast->next;
        if(fast!=NULL){
            slow=slow->next;
            fast=fast->next;
        }
    }
    
    *split1=head;
    *split2=slow->next;
    slow->next=NULL;
}

void mergeSort(node** refToHead){
    node* head=*refToHead;
    node* split1,*split2;
    if(head==NULL || head->next==NULL){
        return;
    }
    splitList(head,&split1,&split2);
    mergeSort(&split1);
    mergeSort(&split2);
    
    *refToHead=mergeList(split1,split2);
    
    return;
    
}


node* findUnion(node* head1, node* head2){
    
    if(head1==NULL && head2==NULL)
    return NULL;
    
    node* head3;
    if(head1->data<head2->data){
            
        head3=creatnode(head1->data);
        head1=head1->next;
    }
    else if(head1->data==head2->data){
            
        head3=creatnode(head1->data);
    
        head1=head1->next;
        head2=head2->next;
    }
    else{
        
        head3=creatnode(head2->data);
        head2=head2->next;
    }
    node* temp=head3;
    while( head1!=NULL && head2!=NULL){
        
        if(head1->data<head2->data){
            temp->next=creatnode(head1->data);
            temp=temp->next;
            head1=head1->next;
        }
        else if(head1->data==head2->data){
            
            temp->next=creatnode(head1->data);
            
            temp=temp->next;
            
            head1=head1->next;
            head2=head2->next;
        }
        else{
            temp->next=creatnode(head2->data);
            temp=temp->next;
            head2=head2->next;
        }
        
        
    }
    
    while(head1!=NULL){
        temp->next=creatnode(head1->data);
        temp=temp->next;
        head1=head1->next;
    }
    while(head2!=NULL){
        temp->next=creatnode(head2->data);
        temp=temp->next;
        head2=head2->next;
    }
    
    return head3;
    
}

int main(){
	printf("creating the linked list by inserting new nodes at the end\n");
	printf("enter 0 to stop building the list, else enter any integer\n");
	int k;
	node* curr,*temp;
	cout<<"enter list1...\n";
	scanf("%d",&k);
	node* head1=creatnode(k);
	scanf("%d",&k);
	temp=head1;
	while(k){
		curr=creatnode(k);
		temp->next=curr;
		temp=temp->next;
		scanf("%d",&k);
	}
	cout<<"displaying list1...\n";
	display(head1); 
	cout<<"\nenter list2...\n";
	scanf("%d",&k);
	node* head2=creatnode(k); 
	scanf("%d",&k);
	temp=head2;

	while(k){
		curr=creatnode(k);
		temp->next=curr;
		temp=temp->next;
		scanf("%d",&k);
	}
	cout<<"displaying list1...\n";
	display(head2);
	
	mergeSort(&head1);
	mergeSort(&head2);
	
	
	cout<<"\ndisplaying their union...\n";
	
	node* head3=findUnion(head1,head2);
	
	display(head3);
	return 0;
}
