const productOfArrayExceptSelf = function (nums) {
    const size = nums.length
    const answer = []
    const cumOrder = []
    const cumReversed = []

    cumOrder[0] = nums[0]
    cumReversed[0] = nums[size - 1]
    
    for (let i=1; i < size; i++) {
        cumOrder[i] = cumOrder[i-1] * nums[i]
        cumReversed[i] = cumReversed[i-1] * nums[size - i -1]
    }

    answer[0] = cumReversed[size - 2]

    answer[size - 1] = cumOrder[size - 2]

    for (let i=1; i < size - 1; i++) {
        answer[i] = cumOrder[i-1] * cumReversed[size - i - 2]
    }

    return answer

}

const productOfArrayExceptSelfImpoved = function (nums) {
    const size = nums.length;
    const answer = new Array(size).fill(1);

    let leftProduct = 1;
    for (let i=0; i < size; i++) {
       answer[i] *= leftProduct;
       leftProduct *= nums[i];
    }

    let rightProduct = 1;
    for (let i=size - 1; i >=0; i--) {
        answer[i] *= rightProduct;
        rightProduct *= nums[i];
    }

    return answer;

}

productOfArrayExceptSelfImpoved([1,2,3,4]);