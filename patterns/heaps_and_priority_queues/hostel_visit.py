"""
Problem Name: Hostel Visit

Problem Difficulty: 2

Problem Constraints: 1 < = k < = Q < = 10^5
-10^6 < = x , y < = 10^6

Problem Description:
Dean of MAIT is going to visit Hostels of MAIT. As you know that he is a very busy person so he decided to visit only first "K" nearest Hostels. Hostels are situated in 2D plane. You are given the coordinates of hostels and you have to answer the Rocket distance of Kth nearest hostel from origin ( Dean's place ) .

Input Format: First line of input contains Q Total no. of queries and K 
There are two types of queries: 
 
first type : 1 x y 
For query of 1st type, you came to know about the co-ordinates ( x , y ) of newly constructed hostel.
second type : 2 
For query of 2nd type, you have to output the Rocket distance of Kth nearest hostel till now. 
 
The Dean will always stay at his place ( origin ).
It is gauranted that there will be atleast k queries of type 1 before first query of type 2. 
 
Rocket distance between two points ( x2 , y2 ) and ( x1 , y1 ) is defined as (x2 - x1)2 + (y2 - y1)2 
Sample Input: 9 3
1 10 10
1 9 9
1 -8 -8
2
1 7 7
2
1 6 6 
1 5 5
2
Output Format: For each query of type 2 output the Rocket distance of Kth nearest hostel from Origin. 
Sample Output: 200
162
98
"""
import heapq

def calculate_rocket_distance(x: float, y: float) -> float:
	return x ** 2 + y ** 2

def main():
	k = int(input("Enter k: "))
	maxHeap = []
	number_queries = int(input("Enter number of queries: "))
	for i in range(number_queries):
		query_type = int(input("Enter query type: "))
		if query_type == 1:
			x = float(input("Enter x: "))
			y = float(input("Enter y: "))
			distance = calculate_rocket_distance(x, y)
			print(distance)
			
			if len(maxHeap) == k:
				heapq.heappushpop(maxHeap, -distance)
			else:
				heapq.heappush(maxHeap, -distance)
			print(maxHeap)
		elif query_type == 2:
			print("Nearest hostel from origin: ", -maxHeap[0])

main()