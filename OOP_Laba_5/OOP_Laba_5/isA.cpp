#include <iostream>


using namespace std;


class Animal {
public:
    Animal() {
        cout << "Animal()" << endl;
    }

    virtual bool isA(const string &who) {
        return who == "Animal";
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

    void catchMouse() {
        cout << "The mouse is caught" << endl;
    }

    bool isA(const string& who) override {
        return who == "Cat";
    }

    void sound() override {
        cout << "Meow" << endl;
    }

    ~Cat() override {
        cout << "~Cat()" << endl;
    }
};


class Manul : public Cat {
public:
    Manul() {
        cout << "Manul()" << endl;
    }

    bool isA(const string &who) override {
        return who == "Manul";
    }

    ~Manul() override {
        cout << "~Manul()" << endl;
    }
};

class Dog : public Animal {
public:
    Dog() {
        cout << "Dog()" << endl;
    }

    bool isA(const string& who) override {
        return who == "Dog";
    }

    ~Dog() override {
        cout << "~Dog()" << endl;
    }
};



int main() {
    Animal* zoo[4];
    zoo[0] = new Animal();
    zoo[1] = new Cat();
    zoo[2] = new Manul();
    zoo[3] = new Dog();

    for (int i = 0; i < 4; i++) {
        if (zoo[i]->isA("Cat")) {
            static_cast<Cat*>(zoo[i])->catchMouse();
        }

        zoo[i]->sound();
    }

    delete zoo[0];
    delete zoo[1];
    delete zoo[2];

    return 0;
}*/
