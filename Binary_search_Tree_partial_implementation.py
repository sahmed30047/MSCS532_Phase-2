# This method recursively inserts products into the BST based on their price, ensuring that the tree maintains its sorted property.

def insert(self, price, product):
    if self.root is None:
        self.root = Node(price, product)
    else:
        self._insert(self.root, price, product)

def _insert(self, current_node, price, product):
    if price < current_node.price:
        if current_node.left is None:
            current_node.left = Node(price, product)
        else:
            self._insert(current_node.left, price, product)
    elif price > current_node.price:
        if current_node.right is None:
            current_node.right = Node(price, product)
        else:
            self._insert(current_node.right, price, product)
