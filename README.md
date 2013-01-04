# RETAIL CENTER

## Introduction
You are given the tree data structure that describes the retail center of a particular product. Each internal node (v) including the root contains a natural integer - capacity(v). Capacity(root) describes the amount of products that are exist in the HQ of the retail center. Capacity(v) of every other internal node describes the amount of items which can be stored there at the same time. The leaf describes the demand in a product such that each leaf is a customer with who needs only **one** product. Supply of a product is performed by moving the item from the HQ (root) to the retailing center that is going to sell the product. 

## Chapter A
You have to implement recursive algorithm which must answer the following questions: *Is it possible to supply the demand for a product?* What is the time complexity of the algorithm? For example, on ![figure 1](https://raw.github.com/bolshchikov/retail-center/master/img/ex1.png) 

it is impossible to make the delivery, while it is possible on

![figure 2](https://raw.github.com/bolshchikov/retail-center/master/img/ex2.png)

Algorithm should implement the function `bool canDemandBeAnswered(Node* root)`.

## Chapter B
Here it is additionally given that each leaf now has new attribute - price(v). The price that a customer willing to pay for a product. You have to implement the algorithms which returns the linked list of nodes which describes customers with maximum sum. Guidelines:

* The algorithms should meet the requirements of chapter A;
* Each customer can purchase only one product
* You can assume that each node has only two children (binary tree)

What is the complexity of the algorithm?
On the figure below, gray nodes - are the nodes that should be returned by algorithm.

![figure 3](https://raw.github.com/bolshchikov/retail-center/master/img/ex3.png) 

The algorithm should use function `Node* getBestCustomers(Node* root)`.

## Chapter C
Let's say that tree used in chapter B how has at most k children. What's going to be the complexity of your algorithm?

## Implementation guidelines
1. `Node.py` contains description of a class Node
2. `HW.py` contains implementation of necessary function
3. File `example_main.py` is used for a check.

## TODO
1. <del>Rewrite given files into Python</del>
	* <del>Node.h</del>
	* <del>HW.cpp</del>
	* <del>example_main.cpp</del>
2. <del>Implement Chapter A</del>
3. <del>Implement Chapter B</del>
4. Write Chapter C
5. Write documentation