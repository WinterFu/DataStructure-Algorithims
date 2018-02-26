/*****************************************************************************
** File Name:        LargeNumberAdd
** Author:           winter
** Modify:           2018/02/26
******************************************************************************
// 摘要：定义一个函数，在该函数中可以实现任意两个整数的加法。
/*---------------------------------------------------------------------------*
**                         Include Files                                     *
**---------------------------------------------------------------------------*/
#include "stdafx.h"
#include <iostream>
#include <string>
/*---------------------------------------------------------------------------*
**                         Namespace Cite                                    *
**---------------------------------------------------------------------------*/
using namespace std;
using namespace std;

void printNumber(const string& number, const int& sLength, int Sym)
{
	bool isBeginning0 = true;
	for (int i = 0; i < sLength; ++i)
	{
		if (isBeginning0 && number[i] != '0')
		{
			isBeginning0 = false;
			if (Sym == 1)
				cout << '-';
		}
		if (!isBeginning0)
			cout << number[i];
	}
	if (isBeginning0)
		cout << '0';
	cout << endl;
}

void Calculate(string& a, string& b, const int aSym, const int bSym, const char maxnumber, const int sLength)
{
	char ch = '0';
	int flag = 0;
	int Sym = 0; // Sym=0 输出为﹢

	if (aSym == 0 && bSym == 0)
	{
		if (maxnumber == 'a')
		{
			for (int i = sLength - 1; i >= 0; --i)
			{
				ch = a[i];
				a[i] = '0' + (((int)ch - (int)b[i] - flag) < 0 ? ((int)ch - (int)b[i] - flag + 10) : ((int)ch - (int)b[i] - flag));
				flag = (((int)ch - (int)b[i] - flag) < 0) ? 1 : 0; //借位标志
			}
			printNumber(a, sLength, Sym);
		}
		else
		{
			for (int i = sLength - 1; i >= 0; --i)
			{
				ch = b[i];
				b[i] = '0' + (((int)ch - (int)a[i] - flag) < 0 ? ((int)ch - (int)a[i] - flag + 10) : ((int)ch - (int)a[i] - flag));
				flag = (((int)ch - (int)a[i] - flag) < 0) ? 1 : 0; //借位标志
			}
			Sym = 1;
			printNumber(b, sLength, Sym);
		}
	}
	else if (aSym == 1 && bSym == 1)
	{
		if (maxnumber == 'a')
		{
			for (int i = sLength - 1; i >= 0; --i)
			{
				ch = a[i];
				a[i] = '0' + (((int)ch - (int)b[i] - flag) < 0 ? ((int)ch - (int)b[i] - flag + 10) : ((int)ch - (int)b[i] - flag));
				flag = (((int)ch - (int)b[i] - flag) < 0) ? 1 : 0; //借位标志
			}
			Sym = 1;
			printNumber(a, sLength, Sym);
		}
		else
		{
			for (int i = sLength - 1; i >= 0; --i)
			{
				ch = b[i];
				b[i] = '0' + (((int)ch - (int)a[i] - flag) < 0 ? ((int)ch - (int)a[i] - flag + 10) : ((int)ch - (int)a[i] - flag));
				flag = (((int)ch - (int)a[i] - flag) < 0) ? 1 : 0; //借位标志
			}
			printNumber(b, sLength, Sym);
		}
	}
	else
	{
		if (aSym == 0)
		{
			for (int i = sLength - 1; i >= 0; --i)
			{
				ch = a[i];
				a[i] = '0' + ((int)ch + (int)b[i] - 96 + flag) % 10;
				flag = ((int)ch + (int)b[i] - 96 + flag) / 10; //进位标志
			}
			printNumber(a, sLength, Sym);
		}
		else
		{
			for (int i = sLength - 1; i >= 0; --i)
			{
				ch = a[i];
				a[i] = '0' + ((int)ch + (int)b[i] - 96 + flag) % 10;
				flag = ((int)ch + (int)b[i] - 96 + flag) / 10; //进位标志
			}
			Sym = 1;
			printNumber(a, sLength, Sym);
		}
	}
}

void LargeNumberSub(string& a, string& b)
{
	// 标识正负
	int aSym = (a[0] == '-') ? 1 : 0;
	int bSym = (b[0] == '-') ? 1 : 0;
	// 符号位归零（方便计算）
	if (a[0] == '-' || a[0] == '+')
		a[0] = '0';
	if (b[0] == '-' || b[0] == '+')
		b[0] = '0';
	// 绝对值大数标识
	char maxnumber = 'a';

	// 计算加数和的长度
	int sLength = (a.size() > b.size() ? a.size() : b.size()) + 1;

	// 补零
	int aLen0 = sLength - a.size();
	int bLen0 = sLength - b.size();
	for (int i = 0; i < aLen0; ++i)
		a.insert(0, "0");
	for (int i = 0; i < bLen0; ++i)
		b.insert(0, "0");

	// 判断大小
	for (int i = 0; i < sLength; ++i)
	{
		if (a[i] > b[i])
		{
			maxnumber = 'a';
			break;
		}
		else if (a[i] < b[i])
		{
			maxnumber = 'b';
			break;
		}
	}

	// 计算
	Calculate(a, b, aSym, bSym, maxnumber, sLength);
}

void Showcin(const string& a, const string& b)
{
	for (int i = (a[0] == '+' ? 1 : 0); i < a.size(); ++i)
		cout << a[i];
	cout << " - ";
	if (b[0] == '-')
		cout << "(";
	for (int i = (b[0] == '+') ? 1 : 0; i < b.size(); ++i)
		cout << b[i];
	if (b[0] == '-')
		cout << ")";
	cout << " = ";
}

bool check(const string& a, const string& b)
{
	for (int i = 0; i < a.size(); ++i)
	{
		if (i == 0 && (a[0] == '+' || a[0] == '-'))
			continue;
		if (a[i] < '0' || a[i] > '9')
		{
			cout << "- -!!! 无效输入！只允许输入带符号的整数。" << endl;
			return true;
		}
	}
	for (int i = 0; i < b.size(); ++i)
	{
		if (i == 0 && (b[0] == '+' || b[0] == '-'))
			continue;
		if (b[i] < '0' || b[i] > '9')
		{
			cout << "- -!!! 无效输入！只允许输入带符号的整数。" << endl;
			return true;
		}
	}
	return false;
}

// ====================测试代码====================
void Part()
{
	bool InvalidInput = true;
	string a, b;
	cout << "请输入两个需要相减的整数(支持正负整数) ";
	cout << "输入格式【a空格b  or  a回车b】:" << endl;
	while (cin >> a >> b)
	{
		// 非法输入检测&处理
		InvalidInput = check(a, b);

		if (!InvalidInput)
		{
			// 显示输入
			Showcin(a, b);
			//大数运算
			LargeNumberSub(a, b);
		}

		cout << "请再次输入两个需要相减的整数(支持正负整数) ";
		cout << "输入格式【a空格b  or  a回车b】:" << endl;
	}
}

int main(int argc, char* argv[])
{
	cout << "------------------------------ 大数减法 ------------------------------" << endl;
	Part();

	system("pause");
	return 0;
}
