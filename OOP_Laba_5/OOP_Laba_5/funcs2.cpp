#include <iostream>


using namespace std;


class Base {
public:
    Base() {
        cout << "Base()" << endl;
    }

    Base(Base &b) {
        cout << "Base(Base &b)" << endl;
    }

    ~Base() {
        cout << "~Base()" << endl;
    }
};


Base func1() {
    cout << "func1()" << endl;
    Base b;
    return b;
};

// Возвращает указатель на уничтоженный объект (стековую переменную),
// что приводит к неопределенному поведению.
Base* func2() {
    cout << "func2()" << endl;
    Base b;
    return &b;
};

// Возвращает ссылку на уничтоженный объект (стековую переменную),
// что приводит к неопределенному поведению
Base& func3() {
    cout << "func3()" << endl;
    Base b;
    return b;
};

// Потенциальная утечка памяти, так как объект на куче не освобождается.
Base func4() {
    cout << "func4()" << endl;
    Base *b = new Base();
    return *b;
};

// Необходимо явное удаление (возможно забыть)
Base* func5() {
    cout << "func5()" << endl;
    Base *b = new Base();
    return b;
};

// Необходимо явное удаление (возможно забыть
Base& func6() {
    cout << "func6()" << endl;
    Base *b = new Base();
    return *b;
};


int main() {
    {
        Base b1 = func1();
        cout << "main" << endl;
    }

    cout << endl;

    {
        Base *b2 = func2();
        cout << "main" << endl;
        delete b2;
    }

    cout << endl;

    {
        Base &b3 = func3();
        cout << "main" << endl;
    }

    cout << endl;

    {
        Base b4 = func4();
        cout << "main" << endl;
    }

    cout << endl;

    {
        Base *b5 = func5();
        cout << "main" << endl;
        delete b5;
    }

    cout << endl;

    {
        Base &b6 = func6();
        cout << "main" << endl;
        delete &b6;
    }


    return 0;
}
