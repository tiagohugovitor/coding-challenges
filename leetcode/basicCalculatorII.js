const basicCalculatorII = function (s) {
    const operationWithoutSpaces = s.replace(/ /g, '');
    const operators = operationWithoutSpaces.split(/[0-9]+/).filter(op => op !== "");
    const numbers = operationWithoutSpaces.split(/[\*\+\-/]/g).map(num => parseInt(num));

    const processOperators = (ops, nums, validOps) => {
        let i = 0;
        while (i < ops.length) {
            if (validOps.includes(ops[i])) {
                let result = 0
                if (validOps.includes('*')) {
                    result = ops[i] === '*'
                        ? nums[i] * nums[i + 1]
                        : nums[i] / nums[i + 1];
                } else {
                    result = ops[i] === '+'
                        ? nums[i] + nums[i + 1]
                        : nums[i] - nums[i + 1];
                }
                nums[i] = Math.floor(result);
                nums.splice(i + 1, 1);
                ops.splice(i, 1);
            } else {
                i++;
            }
        }
    };

    processOperators(operators, numbers, ['*', '/']);

    processOperators(operators, numbers, ['+', '-']);

    return numbers[0];
}

console.log(basicCalculatorII('3+2+5'))

const basicCalculatorIIStack = function (s) {
    const operationWithoutSpaces = s.replace(/ /g, '');
    const stack = [];
    let num = 0;
    let sign = '+';

    for (let i = 0; i < operationWithoutSpaces.length; i++) {
        const char = operationWithoutSpaces[i];

        if (!isNaN(char) && char !== ' ') {
            num = num * 10 + parseInt(char, 10);
        }


        if (isNaN(char) || i === operationWithoutSpaces.length - 1) {
            if (char !== ' ') {
                if (sign === '+') {
                    stack.push(num); 
                } else if (sign === '-') {
                    stack.push(-num);
                } else if (sign === '*') {
                    stack.push(stack.pop() * num);
                } else if (sign === '/') {
                    stack.push(Math.trunc(stack.pop() / num));
                }

                sign = char;
                num = 0;
            }
        }
    }

    return stack.reduce((acc, val) => acc + val, 0);
};

console.log(basicCalculatorIIStack(' 3/2 '));
