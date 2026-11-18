#include <iostream>
#include <algorithm>

using namespace std;

struct node
{
    int data;
    node * left;
    node * right;
};

class BinaryTree
{
    private:
        node * root;
    public:
        void insert(int item);
        void inordertrav();
        void inorder(node *);
        void postordertrav();
        void postorder(node *);
        void preordertrav();
        void preorder(node *);
};

void BinaryTree :: insert(int item)
{
    node * p = new node;
    node * parent;
    p->data = item;
    p->left = NULL;
    p->right = NULL;
    parent = NULL;
    if (root == NULL)
    {
        root = p;
    }
    else
    {
        node * ptr;
        ptr = root;
        while (ptr != NULL)
        {
            parent = ptr;
            if (item > ptr->data)
            {
                ptr = ptr->right;
            }
            else
            {
                ptr = ptr = ptr->left;
            }
            if (item < parent->data)
            {
                parent ->left = p;
            }
            else
            {
                parent ->right = p;
            }
        }
    }
}

void BinaryTree :: inordertrav()
{
    inorder(root);
}

void BinaryTree ::preordertrav()
{
    preorder(root);
}

void BinaryTree ::postordertrav()
{
    postorder(root);
}

void BinaryTree :: inorder(node * ptr)
{
    if(ptr !=NULL)
    {
        inorder(ptr ->left);
        cout << " " << ptr -> data << " ";
        inorder(ptr -> right);
    }
}

void BinaryTree ::preorder(node *ptr)
{
    if (ptr != NULL)
    {
        cout << " " << ptr->data << " ";
        inorder(ptr->left);
        inorder(ptr->right);
    }
}

void BinaryTree ::postorder(node *ptr)
{
    if (ptr != NULL)
    {
        inorder(ptr->left);
        inorder(ptr->right);
        cout << " " << ptr->data << " ";
    }
}

int main()
{
    BinaryTree b;
    b.insert(52);
    b.insert(25);
    b.insert(50);
    b.insert(15);
    b.insert(40);
    b.insert(45);
    b.insert(20);
    cout << "inorder" << endl;
    b.inordertrav();
    cout << endl << "postorder" << endl;
    b.postordertrav();
    cout << endl << "preorder" << endl;
    b.preordertrav();
    return 0;
}

