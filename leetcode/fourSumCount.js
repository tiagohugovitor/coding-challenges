const fourSumCount = function(nums1, nums2, nums3, nums4) {
    let count = 0
    let dict = {}
    for (const i of nums1) {
        for (const j of nums2) {
            const s = i + j
            dict[s] = (dict[s] || 0) + 1
        }
    }

    for (const i of nums3) {
        for (const j of nums4) {
            const target = 0 - (i + j)
            if (dict[target]) {
                count += dict[target]
            }
        }
    }
    return count
}

