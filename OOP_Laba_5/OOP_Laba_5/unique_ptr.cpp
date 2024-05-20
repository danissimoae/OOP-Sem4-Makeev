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

    Dot(Dot &p): x(p.x), y(p.y) {
        cout << "Dot(Dot &p)" << endl;
    }

    void printCoord() {
        cout << "x:" << x << " y:" << y << endl;
    }

    ~Dot() {
        cout << "~Dot()" << endl;
    }
};


unique_ptr<Dot> func(unique_ptr<Dot> p) {
    p->printCoord();
    return p;
}


int main() {
    unique_ptr<Dot> p1(new Dot());
    p1->printCoord();

    unique_ptr<Dot> p2 = make_unique<Dot>(5, 15);
    p2->printCoord();

    unique_ptr<Dot> p3 = make_unique<Dot>(*p2.get());
    p3->printCoord();

    p1 = func(std::move(p1));
    p1->printCoord();


    return 0;
}
