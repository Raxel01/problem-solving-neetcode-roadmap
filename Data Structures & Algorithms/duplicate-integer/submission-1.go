func hasDuplicate(nums []int) bool {
    // using set but no set in golang
    // we can iterate over elemnts Olog(n ^ 2)
    // I can use a map for each elemnts

    sliceLen := len(nums)
    checkMap := make(map[int]int)
    for _, number := range nums{
        checkMap[number] = number;
    }

    if len(checkMap) == sliceLen{
        return false
    }

    return true
}
