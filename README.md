# RETAIL CENTER

## Introduction
You are given the tree data structure that describes the retail center of a particular product. Each internal node (v) including the root contains a natural integer - capacity(v). Capacity(root) describes the amount of products that are exist in the HQ of the retail center. Capacity(v) of every other internal node describes the amount of items which can be stored there at the same time. The leaf describes the demand in a product such that each leaf is a customer with who needs only **one** product. Supply of a product is performed by moving the item from the HQ (root) to the retailing center that is going to sell the product. 

## Chapter A
You have to implement recursive algorithm which must answer the following questions: *Is it possible to supply the demand for a product?* What is the time complexity of the algorithm? For example, on ![figure 1](https://raw.github.com/bolshchikov/retail-center/master/ex1.png) 

it is impossible to make the delivery, while it is possible on

![figure 2](https://raw.github.com/bolshchikov/retail-center/master/ex2.png)

Algorithm should implement the function `bool canDEmandBeAnswered(Node* root)`.