func twoSum(nums []int, target int) []int {
    // two pointers
	// i init, (init + 1)
	// if init + init+1 == target ok
	// else (init+1++)
	// all elements O(n ^ 2) not best solution
	// elme[i] + elem[i + 1]
	// i + 1 overlaping
	// Slices, HashTabe(HashMap)
	// iterate sur nums ajout elements [value(int)]indice(int)
	// key : numbers , value: indice

	for i := 0 ; i < len(nums) -1;  i++{
		for j := i + 1; j < len(nums); j++{
			if nums[i] + nums[j] == target{
				return []int{i, j}
			}
		}
	}
	return []int{0, 0}

}
