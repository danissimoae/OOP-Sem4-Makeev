#include <iostream>
#include <ctime>


using namespace std;


template <class T>
class CustomArray {
private:
	T* values;
	int size;
public:
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
		if (idx < 0 || idx > size) {
			throw out_of_range("Index out of range");
		}
		size = size + 1;
		T* newValues = new T[size];
		for (int i = 0; i < idx; i++) {
			newValues[i] = values[i];
		}
		newValues[idx] = elem;
		for (int i = idx + 1; i < size; i++) {
			newValues[i] = values[i - 1];
		}
		delete[] values;
		values = newValues;
	}

	T pop(int idx) {
		if (idx < 0 || idx >= size) {
			throw out_of_range("Index out of range");
		}
		T elem = values[idx];
		size = size - 1;
		T* newValues = new T[size];
		for (int i = 0; i < idx; i++) {
			newValues[i] = values[i];
		}
		for (int i = idx + 1; i < size + 1; i++) {
			newValues[i - 1] = values[i];
		}
		delete[] values;
		values = newValues;
		return elem;
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


void performRandomActions(CustomArray<Trees*>& forest, int numActions) {
	for (int i = 0; i < numActions; i++) {
		int randomAction = rand() % 3;
		if (randomAction == 0) { // Add
			int randomIndex = rand() % (forest.getSize() + 1);
			forest.addIn(new Oak(), randomIndex);
		}
		else if (randomAction == 1 && forest.getSize() > 0) { // Remove
			int randomIndex = rand() % forest.getSize();
			Trees* tree = forest.getValue(randomIndex);
			forest.pop(randomIndex);
			delete tree;
		}
		else { // Method call
			if (forest.getSize() > 0) {
				int randomIndex = rand() % forest.getSize();
				forest.getValue(randomIndex)->leaf();
			}
		}
	}
}

int main() {
	srand(time(nullptr));

	cout << "100 случайных действий:" << endl;
	CustomArray<Trees*> forest1(4);
	performRandomActions(forest1, 100);

	cout << "1000 случайных действий:" << endl;
	CustomArray<Trees*> forest2(4);
	performRandomActions(forest2, 1000);

	cout << "10000 случайных действий:" << endl;
	CustomArray<Trees*> forest3(4);
	performRandomActions(forest3, 10000);

	return 0;
}
