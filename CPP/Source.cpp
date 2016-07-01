#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	string input1;
	string input2;
	fstream dataFile;
	int hammCount = 0;

	dataFile.open("rosalind_hamm.txt", ios::in);
	getline(dataFile, input1);
	cout << input1 << endl << endl;
	getline(dataFile, input2);
	cout << input2 << endl << endl;
	dataFile.close();

	int strLength = input1.length();

	if (dataFile)
	{	
		for (int count = 0; count < strLength; count++)
		{
			if (input1[count] != input2[count])
			{
				hammCount++;
			}
		}

		cout << hammCount << endl;

	}
	else
	{
		cout << "ERR\n";
	}
	system("pause");
	return 0;
}