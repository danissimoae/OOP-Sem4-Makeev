#include <iostream>

using namespace std;

class Animal {
public:
    Animal() {
        cout << "Animal()" << endl;
    }

    void sound() {
        cout << "Something" << endl;
    }

    virtual ~Animal() {
        cout << "~Animal()" << endl;
    }
};


class Cat : public Animal {
public:
    Cat() {
        cout << "Cat()" << endl;
    }

    void sound() {
        cout << "Meow" << endl;
    }

    ~Cat() override {
        cout << "~Cat()" << endl;
    }
};

int main() {
    Animal* animal = new Cat();
    Cat* cat1 = new Cat();

    animal->sound();
    cat1->sound();

    delete animal;
    delete cat1;

    return 0;
}
