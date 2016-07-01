#include <iostream>
#include <string>
#include <fstream>
using namespace std;

void replaceChar(string);

int main()
{
	string dnaInput;
	fstream dataFile;

	dataFile.open("rosalind_revc.txt", ios::in);
	dataFile >> dnaInput;
	dataFile.close();

	if (dataFile)
	{
		reverse(dnaInput.begin(), dnaInput.end());
		replaceChar(dnaInput);
	}
	else
	{
		cout << "ERROR" << endl;
	}

	system("pause");
	return 0;
}

void replaceChar(string input)
{
	fstream outputFile;
	
	int strLength = input.length();
	char ch1 = 'A'; 
	char ch2 = 'T';
	char ch3 = 'C';
	char ch4 = 'G';

	for (int count = 0; count < strLength; count++)
	{
		if (input[count] == ch1)
		{
			input[count] = ch2;
		}
		else if (input[count] == ch2)
		{
			input[count] = ch1;
		}
		else if (input[count] == ch3)
		{
			input[count] = ch4;
		}
		else if (input[count] == ch4)
		{
			input[count] = ch3;
		}
	}
	cout << input << endl;

	outputFile.open("output.txt", ios::out);
	outputFile << input;
	outputFile.close();
}
