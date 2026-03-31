func calculateFromIndex(index int, nums []int) int {
	prod := 1

	for i := 0; i < len(nums); i++ {
		if i == index {
			continue
		}
		prod *= nums[i]
	}
	return prod
}

func productExceptSelf(nums []int) []int {
	var result []int

	for i := 0; i < len(nums); i++ {
		result = append(result, calculateFromIndex(i, nums))
	}
	return result
}

// BAD : repeated work here ! let's solve
// calculate prod exceptSelf can we register prev calculation
// 

// <---> prefix | <---> suffix

// 0--> prefix +1 prod +len
// 1-->pref -self-->  0 -->self+1 --> len
// pref[index] == 1 suffi[index] = 24 ==> prod = 24
// index[1] ==> 24
// index [2]
// pref 
// 2-->pref -self --> 0 ---> self +1 --> len

// for index (One)
// 
