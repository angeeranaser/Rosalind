#include <iostream>
#include <fstream>
using namespace std;

long rabbitPairs(int, int);

int main()
{
	int result = rabbitPairs(28, 2);
	cout << result << endl;

	fstream outputFile;
	outputFile.open("output.txt", ios::out);
	outputFile << result;
	outputFile.close();

	system("pause");
	return 0;
}

long rabbitPairs(int numberMonths, int numberOffspring)
{
	if (numberMonths == 1)
	{
		return 1;
	}
	
	if (numberMonths == 2)
	{
		return numberOffspring;
	}

	long firstGen = rabbitPairs(numberMonths - 1, numberOffspring);
	long secondGen = rabbitPairs(numberMonths - 2, numberOffspring);

	if (numberMonths <= 4)
	{
		return (firstGen + secondGen);
	}

	return (firstGen + (secondGen * numberOffspring));
}