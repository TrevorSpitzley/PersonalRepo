#include "linkList.h"
#include <iostream>

// Constructor for list
LinkedList::LinkedList() {
    this->head = new Node();
    this->tail = new Node();

    this->head->next = this->tail;
    this->head->prev = nullptr;

    this->tail->prev = this->head;
    this->tail->next = nullptr;
}

// Size function
int LinkedList::size() {
    int size = 0;
    Node *temp = this->head->next;
    while (temp != this->tail){
        temp = temp->next;
        size++;
    }
    return size;
}

// Insert function
void LinkedList::insert(const int &element) {
    // New node
    Node *temp = new Node();
    // Set data
    temp->data = element;
    //std::cout << element << std::endl;
    // Make tail the next node
    temp->next = this->tail;
    // Make the prev node of temp the tail->prev node
    temp->prev = this->tail->prev; 
    // Make the next node of tail->prev the temp node
    this->tail->prev->next = temp;
    // Make the prev node of tail the temp node
    this->tail->prev = temp;
}

// Remove function
void LinkedList::remove(const int &element) {
    // New node
    Node *temp = this->head->next;
    // Makes sure list contains node
    if (this->contains(element) == true)
        // Finds node
        while (temp->data != element)
            temp = temp->next;
    // Sets prev and next of temp
    temp->prev->next = temp->next;
    temp->next->prev = temp->prev;
    // Sets pointers to null and deletes
    temp->prev = nullptr;
    temp->next = nullptr;
    delete temp;
}

// Contains function
bool LinkedList::contains(const int &element) {
    Node *temp = this->head->next;
    while (temp != this->tail) {
        if (temp->data == element)
            return true;
        temp = temp->next;
    }
    return false;
}

// Find function
Node* LinkedList::findNode(const int &element) {
    Node *temp = this->head->next;
    while (temp->next != this->tail) {
        if (temp->data == element)
            return temp;
        temp = temp->next;
    }
    return this->head;
}

// Print function
void LinkedList::print() {
    Node *temp = this->head->next;
    while (temp != this->tail) {
        if (temp->next != this->tail){
            std::cout << temp->data << ", ";
        } else {
            std::cout << temp->data << std::endl;
        }
        temp = temp->next;
    }
}
