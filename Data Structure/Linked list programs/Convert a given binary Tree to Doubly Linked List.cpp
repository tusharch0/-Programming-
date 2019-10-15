#include <bits/stdc++.h>
using namespace std;

struct node {
    int data;
    node* left;
    node* right;
};

struct node* create_node(int x)
{
    struct node* temp = new node;
    temp->data = x;
    temp->left = NULL;
    temp->right = NULL;
    return temp;
}

void BinarytoDll(node* root, node** head)
{
    if (root == NULL)
        return;
    BinarytoDll(root->right, head);
    root->right = *head;
    if (*head != NULL) {
        (*head)->left = root;
    }
    *head = root;
    BinarytoDll(root->left, head);
}

void print(node* head)
{
    struct node* temp = head;
    while (temp) {
        cout << temp->data << " ";
        temp = temp->right;
    }
}

void print_tree(node* root)
{
    if (root == NULL) {
        return;
    }
    print_tree(root->left);
    cout << root->data << " ";
    print_tree(root->right);
}

int main()
{
    struct node* root = create_node(5);
    root->left = create_node(6);
    root->right = create_node(7);
    root->left->left = create_node(8);
    root->left->right = create_node(1);
    root->right->right = create_node(0);
    cout << "Print Tree" << endl;
    print_tree(root);
    struct node* head = NULL;
    BinarytoDll(root, &head);
    cout << "\nDoubly Linked List" << endl;
    print(head);

    return 0;
}
