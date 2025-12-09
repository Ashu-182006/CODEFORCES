#include <iostream>
using namespace std;
#define NULL 0

struct Node {
    int data;
    Node *next;
};

struct Node *first , *temp , *ttemp;

void first_node(){
    first = new Node;
    cout << "Enter data: ";
    cin >> first->data;
    first->next = NULL;
}

void add_node(){
    temp = first;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    ttemp = new Node;
    cout << "Enter data: ";
    cin >> ttemp->data;
    ttemp->next = NULL;
    temp->next = ttemp;
}

void add_before_node(int n){
    temp = first;
    while (temp->data != n) {
        ttemp = temp;
        temp = temp->next;
    }
    Node *new_node = new Node;
    cout << "Enter data: ";
    cin >> new_node->data;
    new_node->next = temp;
    ttemp->next = new_node;
}

void add_after_node(int n){
    temp = first;
    while (temp->data != n) {
        temp = temp->next;
    }
    Node *new_node = new Node;
    cout << "Enter data: ";
    cin >> new_node->data;
    new_node->next = temp->next;
    temp->next = new_node;
}

void delete_before_node(int n){
    temp = first;
    while (temp->next->data != n) {
        temp = temp->next;
    }
    ttemp = temp->next;
    temp->next = ttemp->next;
    delete ttemp;
}

void delete_after_node(int n){
    temp = first;
    while (temp->data != n) {
        temp = temp->next;
    }
    ttemp = temp->next;
    temp->next = ttemp->next;
    delete ttemp;
}

void display(){
    temp = first;
    while (temp != NULL) {
        cout << temp->data << endl;
        temp = temp->next;
    }
}

void delete_linked_list() {
    temp = first;
    while (temp != NULL) {
        ttemp = temp->next;
        delete temp;
        temp = ttemp;
    }
    first = NULL;
}

int main() {
    int n=0;
    while(n != -1) {
        cout << "1. Create linked list\n"
                << "2. Add node in the linked list\n"
                << "3. Add node before a given node\n"
                << "4. Add node after a given node\n"
                << "5. Delete node before a given node\n"
                << "6. Delete node after a given node\n"
                << "7. Display list\n"
                << "-1. Exit\n";
        cout << "Enter your choice: ";
        cin >> n;
        switch(n) {
            case 1:
                first_node();
                break;
            case 2:
                add_node();
                break;
            case 3: {
                int val;
                cout << "Enter the value of the node to add before: ";
                cin >> val;
                add_before_node(val);
                break;
            }
            case 4: {
                int val;
                cout << "Enter the value of the node to add after: ";
                cin >> val;
                add_after_node(val);
                break;
            }
            case 5: {
                int val;
                cout << "Enter the value of the node to delete before: ";
                cin >> val;
                delete_before_node(val);
                break;
            }
            case 6: {
                int val;
                cout << "Enter the value of the node to delete after: ";
                cin >> val;
                delete_after_node(val);
                break;
            }
            case 7:
                display();
                break;
            case -1: {
                cout << "Exiting...\n"
                        << "Thank you!\n";
                delete_linked_list();
                break;
            }
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    }
    return 0;
}