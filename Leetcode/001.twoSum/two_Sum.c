void twoSum(int num[], int n, int target){
	if(n < 1 || num == NULL || target <= 1)
		return

	qucick_sort(num, 0, n);
	
	int strat = 0;
	int end = n-1;
	while(counter_s < counter_e){
		int current_sum = num[start] + num[end];
		
		if(current_sum == target){
			printf("%d,%d", start, end)
		}
		else if(current_sum<target){
			start++;
		}
		else{
			end--;
		}

	}
}

int *twoSum(int *nums, int numsSize, int target){
	int goal = 0;
	int *Index = (int*) malloc(sizeof(int)*2);

	for(int i = 0; i < numsSize-1; ++i)
	{
		goal = target - nums[i];
		for(int j = i + 1; j < numsSize; ++j)
		{
			if(nums[j] == goal && nums[j] != nums[i])
			{
				Index[0] = i; Index[1] = [j];
				return Index;
			}
		}
	}
	return NULL;
}