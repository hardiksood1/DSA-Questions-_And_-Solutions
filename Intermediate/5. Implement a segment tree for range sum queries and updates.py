# 5.Implement a segment tree for range sum queries and updates.

class SegmentTree:
    def __init__(self, arr):
        """
        Initialize the segment tree with the given array.
        """
        self.n = len(arr)
        # Initialize the segment tree with all zeros
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        """
        Build the segment tree recursively.
        """
        if start == end:
            # Leaf node will have a single element
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            # Build left child
            self.build(arr, 2 * node + 1, start, mid)
            # Build right child
            self.build(arr, 2 * node + 2, mid + 1, end)
            # Internal node will have the sum of both children
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index, value):
        """
        Update the value at index to value.
        """
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node, start, end, idx, val):
        if start == end:
            # Leaf node
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                # If index is in the left child
                self._update(2 * node + 1, start, mid, idx, val)
            else:
                # If index is in the right child
                self._update(2 * node + 2, mid + 1, end, idx, val)
            # Update current node after updating child
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, l, r):
        """
        Query the sum in range [l, r]
        """
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            # Range completely outside the node range
            return 0
        if l <= start and end <= r:
            # Range completely inside the node range
            return self.tree[node]
        # Partial overlap
        mid = (start + end) // 2
        left_sum = self._query(2 * node + 1, start, mid, l, r)
        right_sum = self._query(2 * node + 2, mid + 1, end, l, r)
        return left_sum + right_sum

# Example usage
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

print("Sum of values in range [1, 3]:", seg_tree.query(1, 3))  # Output: 15
seg_tree.update(1, 10)  # Update index 1 to value 10
print("Sum of values in range [1, 3] after update:", seg_tree.query(1, 3))  # Output: 22

# Result

# Sum of values in range [1, 3]: 15
# Sum of values in range [1, 3] after update: 22
