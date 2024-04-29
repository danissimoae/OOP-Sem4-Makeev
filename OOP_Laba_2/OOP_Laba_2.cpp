#include <iostream>
#include <stdio.h>

// Class Point
class Point {
public:
	int x, y;
public:
	Point() {
		printf("Point(); \n");
		x = 0;
		y = 0;
	}

	Point(int x, int y) {
		printf("Point(int x, int y); %d, %d \n", x, y);
		this->x = x;
		this->y = y;
	}

	Point(const Point& p) {
		printf("Point(const Point &p); \n");
		x = p.x;
		y = p.y;
	}

	~Point() {
		printf("~Point(); %d, %d; \n", x, y);
	}

	void set(int x, int y) {
		this->x = x;
		this->y = y;
		printf("Point::set(), x = %d, y = %d \n", x, y);
	}

	void copy(Point& p) {
		x = p.x;
		y = p.y;
		printf("Point::copy(), x = %d, y = %d \n", x, y);
	}

	void move(int dx, int dy) {
		x = x + dx;
		y = y + dy;
		printf("Point::move(), dx = %d, dy = %d \n", dx, dy);
	}

	void clear();
};

void Point::clear() {;
	x = 0;
	y = 0;
	printf("Point::clear(), %d, %d \n", x, y);
}



class ColoredPoint : private Point {
public:
	int color;
public:
	ColoredPoint() : Point() {
		printf("ColoredPoint(); \n");
		color = 0;
	}

	ColoredPoint(int x, int y, int color) : Point(x, y) {
		printf("ColoredPoint(int x, int y, int color); %d, %d, %d \n", x, y, color);
		this->color = color;
	}

	ColoredPoint(const ColoredPoint& p) {
		printf("ColoredPoint(const ColoredPoint& p); \n");
		color = p.color;
		x = p.x;
		y = p.y;
	}

	~ColoredPoint() {
		printf("~ColoredPoint(); %d, %d, %d\n", x, y, color);
	}

	void setColor(int newColor) {
		color = newColor;
	}
};


class Circle {
public:
	Point *center;
	
public:
	Circle() {
		printf("Circle(); \n");
		center = new Point;
	}

	Circle(int x, int y) {
		printf("Circle(int x, int y); %d, %d \n", x, y);
		center = new Point(x, y);
	}

	Circle(const Circle& c) {
		printf("Circle(const Circle& c); \n");
		// UB
		// center = c.center;
		center = new Point(*(c.center));
	}

	~Circle() {
		printf("~Circle(); %d, %d, %d\n", center->x, center->y);
		delete center;
	}

	void setCenter(int x, int y) {
		printf("Circle::setCenter(); \n");
		center = new Point(x, y);
	}
};




int main() {

	// Проверка класса Point статика

	/*Point pBase;
	Point pParam(3, 5);
	Point pCopy(pParam);

	// Првоерка класса Point динамика

	Point* pBaseDyn = new Point;
	Point* pParamDyn = new Point(3, 3);
	Point* pCopyDyn = new Point(*pParamDyn);

	delete pBaseDyn;
	delete pParamDyn;
	delete pCopyDyn;

	// Првоерка спецификаторов доступа -
	pBase.x; // Доступны, тк спецификатор public
	pParam.copy(pBase);


	// Проверка класса ColoredPoint
	ColoredPoint* cpDyn = new ColoredPoint;
	delete cpDyn;*/


	// В переменную-указатель на базовый класс поместить объект-потомок:
	// какие методы можно вызывать, какие нет?
	/*Point* pDaughter = new ColoredPoint;
	pDaughter->set(10, 10);
	pDaughter->clear();
	delete pDaughter;*/

	//Point pB;
	//pB.move(2,3);

	//ColoredPoint pD;

	/*ColoredPoint* pParent = new ColoredPoint;
	delete pParent;*/


	// Композиция
	// UB test
	/*Circle* c = new Circle;
	Circle* cc = new Circle(*c);
	delete c;
	delete cc;*/

	/*Circle* cCopy = new Circle(3, 5);
	cCopy->setCenter(2, 3);
	delete cCopy;*/


	return 0;
};
