#include <iostream>
#include <ctime>

using namespace std;

int main()
{
	clock_t begin = clock();
	int sum = 0;
	for (int i=0; i<1000000; i++)
	{
		sum = sum + i;
	}
	clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	cout << elapsed_secs << endl;

	return 0;
}
