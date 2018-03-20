class Solution{

private:
	std::vector<int> result;

public:
	void backtracking(std::vector<int>& C, const int T){
		static int sum = 0, flag = C[0];
		std::vector<int>::iterator iterC = C.begin();
		for (; *iterC != flag; ++iterC);
		for (; iterC < C.end(); ++iterC)
		{
			result.push_back(*iterC); sum += *iterC;
			if (sum == T)
			{
				std::vector<int>::iterator iterR = result.begin();
				for (; iterR < result.end(); ++iterR) std::cout << *iterR << " "; std::cout << "\n";
			}
			if (sum >= T) { result.pop_back(); sum -= *iterC; continue; }
			flag = *iterC; BackTracking(C, T);
			result.pop_back(); sum -= *iterC;
		}

	}
};

int main()
{
	Solution winter;
	winter.backtracking(std::vector<int> [2, 3, 6, 7], 7);
	system("pause");
	return 0;
}