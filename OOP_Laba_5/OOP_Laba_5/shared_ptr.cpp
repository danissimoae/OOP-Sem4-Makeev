#include <iostream>
#include <memory>

using namespace std;

class Dot {
private:
    int x{0};
    int y{0};

public:
    Dot() {
        cout << "Dot()" << endl;
    }

    Dot(int x, int y): x(x), y(y) {
        cout << "Dot(int x, int y)" << endl;
    }

    Dot(const Dot &p): x(p.x), y(p.y) {
        cout << "Dot(const Dot &p)" << endl;
    }

    void printCoord() {
        cout << "x:" << x << " y:" << y << endl;
    }

    ~Dot() {
        cout << "~Dot()" << endl;
    }
};

shared_ptr<Dot> func(shared_ptr<Dot> p) {
    p->printCoord();
    return p;
}

int main() {
    shared_ptr<Dot> p1 = make_shared<Dot>();
    p1->printCoord();

    shared_ptr<Dot> p2 = make_shared<Dot>(5, 15);
    p2->printCoord();

    shared_ptr<Dot> p3 = make_shared<Dot>(*p2);
    p3->printCoord();

    p1 = func(p1);
    p1->printCoord();

    return 0;
}
