#!/usr/bin/node

const args = process.argv.slice(2);

function findSecondLargest (numbers) {
  const integers = numbers.map(Number);

  if (integers.length <= 1) {
    return 0;
  }

  const sortedUniqueIntegers = [...new Set(integers)].sort((a, b) => b - a);

  return sortedUniqueIntegers[1] || 0;
}

console.log(findSecondLargest(args));
