const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n").map(Number);

let card = input.slice(1);
class BinaryHeap {
  constructor() {
    this.heap = [];
  }

  // 원소를 힙에 삽입
  insert(value) {
    this.heap.push(value);
    this.heapifyUp();
  }

  // 최상위 원소를 제거하고 반환
  extract() {
    if (this.heap.length === 0) {
      return null;
    }

    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    const root = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown();

    return root;
  }

  // 힙을 위로 재정렬
  heapifyUp() {
    let currentIndex = this.heap.length - 1;

    while (currentIndex > 0) {
      const parentIndex = Math.floor((currentIndex - 1) / 2);
      if (this.heap[parentIndex] <= this.heap[currentIndex]) {
        break;
      }

      // 부모와 자식을 교체
      [this.heap[parentIndex], this.heap[currentIndex]] = [
        this.heap[currentIndex],
        this.heap[parentIndex],
      ];
      currentIndex = parentIndex;
    }
  }

  // 힙을 아래로 재정렬
  heapifyDown() {
    let currentIndex = 0;

    while (true) {
      const leftChildIndex = 2 * currentIndex + 1;
      const rightChildIndex = 2 * currentIndex + 2;
      let smallestChildIndex = currentIndex;

      if (
        leftChildIndex < this.heap.length &&
        this.heap[leftChildIndex] < this.heap[smallestChildIndex]
      ) {
        smallestChildIndex = leftChildIndex;
      }

      if (
        rightChildIndex < this.heap.length &&
        this.heap[rightChildIndex] < this.heap[smallestChildIndex]
      ) {
        smallestChildIndex = rightChildIndex;
      }

      if (smallestChildIndex === currentIndex) {
        break;
      }

      // 부모와 가장 작은 자식을 교체
      [this.heap[currentIndex], this.heap[smallestChildIndex]] = [
        this.heap[smallestChildIndex],
        this.heap[currentIndex],
      ];
      currentIndex = smallestChildIndex;
    }
  }
}


const heap = new BinaryHeap();

for (let i = 0; i < input[0]; i++) {
  heap.insert(card[i]);
}
let ans = 0;
while (heap.heap.length > 1) {
  a = parseInt(heap.extract());
  b = parseInt(heap.extract());
  let sum = a + b;
  ans += sum;
  heap.insert(a + b);
}

console.log(ans);
