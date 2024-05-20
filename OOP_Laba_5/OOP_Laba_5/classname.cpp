#include <iostream>


using namespace std;


class Animal {
public:
    Animal() {
        cout << "Animal()" << endl;
    }

    virtual string classname() {
        return "Animal";
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

    string classname() override {
        return "Cat";
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

    string classname() override {
        return "Manul";
    }

    ~Manul() override {
        cout << "~Manul()" << endl;
    }
};



int main() {
    Animal* zoo[3];
    zoo[0] = new Animal();
    zoo[1] = new Cat();
    zoo[2] = new Manul();

    for (int i = 0; i < 3; i++) {
        if (zoo[i]->classname() == "Cat" || zoo[i]->classname() == "Manul") {
            static_cast<Cat*>(zoo[i])->catchMouse();
        }

        zoo[i]->sound();
    }

    delete zoo[0];
    delete zoo[1];
    delete zoo[2];

    return 0;
}
