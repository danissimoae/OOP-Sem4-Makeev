#include <iostream>


using namespace std;


class Base {
public:
    Base() {
        cout << "Base()" << endl;
    }

    Base(Base *obj) {
        cout << "Base(Base *obj)" << endl;
    }

    Base(Base &obj) {
        cout << "Base(Base &obj)" << endl;
    }

    virtual ~Base() {
        cout << "~Base()" << endl;
    }
};


class Desc: public Base {
public:
    Desc() {
        cout << "Desc()" << endl;
    }

    Desc(Desc *obj) {
        cout << "Desc(Desc *obj)" << endl;
    }

    Desc(Desc &obj) {
        cout << "Desc(Desc &obj)" << endl;
    }

    ~Desc() override {
        cout << "~Desc()" << endl;
    }
};


void func1(Base obj) {
    cout << "func1(Base obj)" << endl;

    Desc *d = dynamic_cast<Desc*>(&obj);
    cout << d << endl;
};


void func2(Base *obj) {
    cout << "func2(Base *obj)" << endl;

    Desc *d = dynamic_cast<Desc*>(obj);
    cout << d << endl;
};


void func3(Base &obj) {
    cout << "func3(Base &obj)" << endl;

    Desc *d = dynamic_cast<Desc*>(&obj);
    cout << d << endl;
};


int main() {
    {
        Base b1;
        cout << "b1: " << &b1 << endl;
        func1(b1);
        func2(&b1);
        func3(b1);*/

        Base *b2 = new Base();
        cout << "b2: " << b2 << endl;
        func1(*b2);
        func2(b2);
        func3(*b2);

        delete b2;
    }

    cout << endl;

    {
        Desc d1;
        cout << "d1: " << &d1 << endl;
        func1(d1);
        func2(&d1);
        func3(d1);

        Desc *d2 = new Desc();
        cout << "d2: " << d2 << endl;
        func1(*d2);
        func2(d2);
        func3(*d2);

        delete d2;
    }

    return 0;
}
