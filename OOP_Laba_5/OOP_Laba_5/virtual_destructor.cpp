#include <iostream>

using namespace std;

class Animal {
public:
    Animal() {
        cout << "Animal()" << endl;
    }

    virtual void sound() {
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

    void sound() override {
        cout << "Meow" << endl;
    }

    ~Cat() override {
        cout << "~Cat()" << endl;
    }
};


class Dog : public Animal {
public:
    Dog() {
        cout << "Dog()" << endl;
    }

    void sound() override {
        cout << "Woof" << endl;
    }
    /*~Dog() override {
        cout << "~Dog()" << endl;
    }*/
};


int main() {
    Animal* animal = new Animal();
    Cat* cat1 = new Cat();
    Dog* dog1 = new Dog();

    animal->sound();
    cat1->sound();
    dog1->sound();

    delete animal;
    delete cat1;
    delete dog1;

    return 0;
}
