#include <iostream>
#include "Point.h"
#include "ColoredPoint.h"

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
	pParam.copy(pBase);*/


	// Проверка класса ColoredPoint
	ColoredPoint* cpDyn = new ColoredPoint;


	return 0;
};