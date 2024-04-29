// Class Point
class Point{
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

void Point::clear() {
	x = 0;
	y = 0;
}
