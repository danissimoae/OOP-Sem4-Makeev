#include <iostream>
#include <ctime>


using namespace std;


template <class T>
class CustomArray {
private:
	T *values;
	int size;
public:
	int getSize() {
		return size;
	}

	T getValue(int idx) {
		return values[idx];
	}

	void setValue(int idx, T elem) {
		values[idx] = elem;
	}

	void addFirst(T elem) {
		size = size + 1;
		T* newValues = new T[size];
		newValues[0] = elem;
		for (int i = 1; i < size; i++) {
			newValues[i] = values[i - 1];
		}
		delete[] values;
		values = newValues;
	}

	void addLast(T elem) {
		size = size + 1;
		T* newValues = new T[size];
		for (int i = 0; i < size - 1; i++) {
			newValues[i] = values[i];
		}
		newValues[size - 1] = elem;
		delete[] values;
		values = newValues;
	}

	void addIn(T elem, int idx) {
		size = size + 1;
		T* newValues = new T[size];
		for (int i = 0; i < idx; i++) {
			newValues[i] = values[i];
		}
		newValues[idx] = elem;
		for (int i = idx + 1; i < size; i++) {
			newValues[i] = values[i];
		}
		delete[] values;
		values = newValues;
	}

	T pop(int idx) {
		size = size - 1;
		T* newValues = new T[size];
		for (int i = 0; i < idx; i++) {
			newValues[i] = values[i];
		}
		T elem = values[idx];
		for (int i = idx; i < size; i++) {
			newValues[i] = values[i];
		}
		delete[] values;
		values = newValues;
		return elem;
	}

	CustomArray(int size) {
		this->size = size;
		this->values = new T[size];
	}

	CustomArray(CustomArray& a) {
		this->size = a.getSize();
		this->values = new T[this->size];
		for (int i = 0; i < this->size; i++) {
			values[i] = a.getValue(i);
		}
	}

	~CustomArray() {
		delete[] values;
	}
};


class Trees {
public:
	virtual void leaf() {
		cout << "Undefined leaf" << endl;
	}
};

class Maple : public Trees {
public:
	void leaf() override {
		cout << "Maple leaf" << endl;
	}
};

class Pine : public Trees {
public:
	void leaf() override {
		cout << "Pine leaf" << endl;
	}
};

class Oak : public Trees {
public:
	void leaf() override {
		cout << "Oak leaf" << endl;
	}
};


int main() {
    CustomArray<Trees*> forest(4);
    for (int i = 0; i < forest.getSize(); i++) {
        if (i % 2) {
            forest.setValue(i, new Pine());
        }
        else {
            forest.setValue(i, new Maple());
        }
    }

    for (int i = 0; i < forest.getSize(); i++) {
        forest.getValue(i)->leaf();
    }


    cout << endl;


    forest.addFirst(new Oak());

    for (int i = 0; i < forest.getSize(); i++) {
        forest.getValue(i)->leaf();
    }


    cout << endl;


    forest.addLast(new Oak());

    for (int i = 0; i < forest.getSize(); i++) {
        forest.getValue(i)->leaf();
    }


    cout << endl;


    forest.addIn(new Oak(), 3);

    for (int i = 0; i < forest.getSize(); i++) {
        forest.getValue(i)->leaf();
    }


    cout << endl << endl << endl;

    clock_t start = clock();
    for (int i = 0; i < 100; i++) {
        int random_action;
        if (forest.getSize() == 0) {
            random_action = 0;
        }
        else {
            random_action = rand();
        }
        if (random_action % 3 == 0) {
            Trees* tree;
            int random_object = rand();
            if (random_object % 3 == 0) {
                tree = new Pine();
            }
            else if (random_action % 3 == 1) {
                tree = new Maple();
            }
            else {
                tree = new Oak();
            }
            int random_index;
            if (forest.getSize() > 0) {
                random_index = rand() % forest.getSize();
            }
            else {
                random_index = 0;
            }
            forest.addIn(tree, random_index);
        }
        else if (random_action % 3 == 1) {
            int random_index = rand() % forest.getSize();
            Trees* tree = forest.getValue(random_index);
            forest.pop(random_index);
            delete tree;
        }
        else {
            int random_index = rand() % forest.getSize();
            forest.getValue(random_index)->leaf();
        }
    }

    clock_t end = clock();
    double seconds = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Время: %f секунд \n", seconds);

    return -1;
}
