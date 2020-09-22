#include "linkList.h"
#include <iostream>

int main() {

    LinkedList list;

    for (int i = 0; i <= 10; i++) {
        if (i % 2 == 0)
            list.insert(i);
    }

    list.insert(5);

    list.print();

    if (list.contains(5))
        std::cout << "The list contains 5!" << std::endl;

    list.print();

    std::cout << "The size of the list is: " << list.size() << " nodes!" << std::endl;

    list.print();

    if (list.contains(6))
        std::cout << "The list contains 6!" << std::endl;

    list.remove(6);

    list.print();

    if (!list.contains(6))
        std::cout << "The list does not contain 6!" << std::endl;

    return 0;
}
