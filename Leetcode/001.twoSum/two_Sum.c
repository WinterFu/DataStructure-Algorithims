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