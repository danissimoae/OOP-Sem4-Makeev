#include "Point.h"

class ColoredPoint: public Point {
public:
	int color;
public:
	ColoredPoint() : Point() {
		printf("ColoredPoint(); \n");
		color = 0;
	}

	ColoredPoint(int x, int y, int color): Point(x, y) {
		printf("ColoredPoint(int x, int y, int color); %d, %d, %d \n", x, y, color);
		this->color = color;
	}

	ColoredPoint(const ColoredPoint  &p) {
		printf("ColoredPoint(const ColoredPoint& p); \n");
		color = p.color;
		x = p.x;
		y = p.y;
	}

	~ColoredPoint() {
		printf("~ColoredPoint(); %d, %d, %d\n", x, y, color);
	}
};