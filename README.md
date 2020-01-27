# AVL Tree

AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes.

## Requirement

Use Python programming language to run the code.

## Usage
Here is the driver code.
```
def Test():

    avl = AVLTree()

    x = None
    x = avl.Insert(x, 10)
    x = avl.Insert(x, 20)
    x = avl.Insert(x, 30)
    x = avl.Insert(x, 40)
    x = avl.Insert(x, 50)
    x = avl.Insert(x, 25)

    avl.Delete(x, 40)

    avl.PreOrder(x)
    avl.PostOrder(x)
    avl.InOrder(x)

    return avl

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[UIT](https://www.uit.edu/)
