//
// Created by trevo on 2/13/2020.
//
#include "bst.h"
#include <iostream>
#include <queue>

//Constructor
BinarySearchTree::BinarySearchTree() {
    this->root= nullptr;
}
//insert method
void BinarySearchTree::insert(const int & num, BinarySearchTree::BinaryNode* &node) {
    if (node == nullptr) {
        node = new BinaryNode();
        node->data = num;
        node->left = nullptr;
        node->right = nullptr;
    }
    else if (num < node->data)
        insert(num, node->left);

    else if (num > node->data)
        insert(num, node->right);

    else
        return;
}
//make empty method
void BinarySearchTree::makeEmpty(BinarySearchTree::BinaryNode* &node) {
    if (node != nullptr){
        makeEmpty(node->left);
        makeEmpty(node->right);
        delete node;
    }
    node = nullptr;
}
//Level order
void BinarySearchTree::levelorder(BinarySearchTree::BinaryNode * node) {
    if (node == nullptr)
        std::cout<< "The Tree is empty!"<<std::endl;
    else {
        std::queue<BinaryNode *> q;
        q.push(node);
        while (!q.empty()){
            if (q.front()->left != nullptr)
                q.push(q.front()->left);
            if (q.front()->right != nullptr)
                q.push(q.front()->right);
            std::cout<<q.front()->data<< " ";
            q.pop();
        }
        std::cout<<""<<std::endl;
    }
}
