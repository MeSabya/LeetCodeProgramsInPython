## You are given an array of N integers. You have to determine the maximum difference between two indices i and j, such that i < j and Array[i] < Array[j].

```
Let’s understand it using an example.
Example 1:
Input: [4, 2, 8, 9, 11, 4, 3, 1]
Output: 5

Explanation: Indices 1 and 6 satisfy the constraints as 1 < 6 and Array[1] < Array[6], (2 < 3).

Example 2:
Input: [4, 3, 2, 1]
Output: -1

Explanation: There are no pair of indices that fullfill the given constraints.
```

👉 Brute Force approach Time complexity o(n2)

```cpp
#include <bits/stdc++.h> // the all in one header file :)
using namespace std;

// method to calculate the maximum difference between the indices
// using brute force approace

int maximum_difference(const vector<int> &input)
{
	// declare a variable to hold our result
	int max_diff = 0;

	// size of the input array
	int n = input.size();

	// use two loop to process each pair of values that
	// satisfy the constraints
	for (int i = 0; i < n - 1; i++)
	{

		// start the second inner loop from the end
		for (int j = n - 1; j > i; j--)
		{
			// compare if ith value is less than jth and j-i is maximum
			// then update the max_diff
			if (input[i] < input[j])
			{
				max_diff = max(max_diff, j - i);
			}
		}
	}

	// return the result
	return max_diff;
}

// Driver program
int main()
{
	// input array
	vector<int> input{4, 2, 8, 9, 11, 4, 3, 1};

	cout << "The maximum difference between two indices are " << maximum_difference(input) << endl;

	return 0;
}
```

👉 ***Efficient Approach***

Our intuition says if there is a smallest element at a lower index (i), then there will be many numbers which will be greater than the smallest element and those will be at higher index (j and i < j). 

So we need to find the smallest element which is at lower index. 

**Step1**: For that we need to maintain a map<int, vector<int>> , where key is element and values are indices to handle duplicates.
  
```
For example in cpp we can use:
map<int, vector<int> hashtable;

which is mapping an integer to a list/vector of integers, where this vector will hold indices for duplicate values.
Input: [4, 2, 2, 5]
Hash table:
[4, {0}]
[2, {1, 2}]
[5, {3}]
```

**Step2**: To find the smallest element , we need to sort the input array. 

```cpp
  #include <bits/stdc++.h> // the all in one header file :)
using namespace std;

// method to calculate the maximum difference between the indices
// using brute force approace

int maximum_difference(vector<int> &input)
{
	// create a hash table to store the indices of each element
	map<int, vector<int>> hashTable;

	// map the elements with their indices or list of indices in case of duplicates
	for (int i = 0; i < input.size(); i++)
	{
		hashTable[input[i]].push_back(i);
		// the list of indices for each value will be sorted
		// it will help us to get the earliest position and the last position
		// of an element
	}

	// now sort the array
	sort(input.begin(), input.end());

	int lowest_index_so_far = input.size();

	// variable to hold the result
	int max_diff = -1;

	for (int i = 0; i < input.size(); i++)
	{

		// update the lowest index seen so far based on the current element
		lowest_index_so_far = min(lowest_index_so_far, hashTable[input[i]][0]);
		// :) this monstrosity hashTable[input[i]][0] is nothing but the first
		// position of the input[i]

		// Now take the current elements last position
		int ith_last_position = hashTable[input[i]][hashTable[input[i]].size() - 1];
		// the part hashTable[input[i]] gives us the list of indices
		// th second part gives us the last index value

		// Now update the max_diff, if ith_last_position - lowest position seen so far
		// is the maximum differece
		max_diff = max(max_diff, ith_last_position - lowest_index_so_far);
	}

	return max_diff;
}

// Driver progrom
int main()
{
	vector<int> input{4, 2, 8, 9, 11, 4, 3, 1};
	cout << "The maximum difference between any two indices are " << maximum_difference(input) << endl;

	return 0;
}
```







