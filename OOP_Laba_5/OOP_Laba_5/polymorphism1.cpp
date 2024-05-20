#include <iostream>

using namespace std;

class Animal {
public:
    Animal() {
        cout << "Animal()" << endl;
    }

    virtual void sound() {
        cout << "Something" << endl;
        shake();
    }

    virtual void shake() {
        cout << "Shake" << endl;
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

    void shake() override {
        cout << "redefined shake" << endl;
    }

    ~Cat() override {
        cout << "~Cat()" << endl;
    }
};

int main() {
    Animal* animal = new Animal();
    Cat* cat1 = new Cat();

    animal->sound();
    cat1->sound();

    delete animal;
    delete cat1;

    return 0;
}
