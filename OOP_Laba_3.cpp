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
		cout << "Кленовый лист" << endl;
	}
};

class Pine : public Trees {
public:
	void leaf() override {
		cout << "Хвойный лист" << endl;
	}
};

class Oak : public Trees {
public:
	void leaf() override {
		cout << "Дубовый лист" << endl;
	}
};


int main() {
	setlocale(LC_ALL, "rus");
	
	CustomArray<Trees*> forest(4);
	for (int i = 0; i < forest.getSize(); i++) {
		if (i % 2) {
			forest.setValue(i, new Maple());
		}
		else {
			forest.setValue(i, new Pine());
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

	forest.addLast(new Pine());

	for (int i = 0; i < forest.getSize(); i++) {
		forest.getValue(i)->leaf();
	}

	cout << endl;

	forest.addIn(new Maple(), 3);

	for (int i = 0; i < forest.getSize(); i++) {
		forest.getValue(i)->leaf();
	}

	cout << endl;

	//////////////////////////////////////////////

	std::cout << "Состояние контейнера до выполнения действий:" << std::endl;
	for (int i = 0; i < forest.getSize(); i++) {
		forest.getValue(i)->leaf();
	}

	std::cout << std::endl;

	// Время начала работы
	clock_t startTime = clock();

	// Цикл из 100 случайных действий
	for (int i = 0; i < 1000; i++) {
		int action = rand() % 3; // Случайный выбор действия
		int index = rand() % forest.getSize(); // Случайный индекс элемента

		switch (action) {
		case 0:
			forest.addFirst(new Oak());
			break;
		case 1:
			forest.addLast(new Pine());
			break;
		case 2:
			forest.getValue(index)->leaf();
			break;
		default:
			break;
		}
	}

	// Время окончания работы
	clock_t endTime = clock();

	// Вычисление времени работы
	double totalTime = double(endTime - startTime) / CLOCKS_PER_SEC;

	std::cout << std::endl;
	std::cout << "Время выполнения: " << totalTime << " секунд" << std::endl;

	return 0;
}
