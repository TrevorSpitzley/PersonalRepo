#ifndef LIST_H
#define LIST_H

struct Node {
    int data;
    Node *prev;
    Node *next;
};

class LinkedList {

public:

    LinkedList();
    
    Node *head{};
    Node *tail{};

    int size();
    void insert(const int &element);
    void remove(const int &element);
    bool contains(const int &element);
    Node* findNode(const int &element);
    void print();
};

#endif
