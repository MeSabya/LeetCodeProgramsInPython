## Count Ways to Score in a Game

Suppose there is a game where a player can score either 
1, 2 or 4 points in each turn. Given a total score, n , find all the possible ways in which you can score these  points.



```cpp
#include <iostream>
#include <vector>

long ScoringOptionsRec(int n, std::vector<long>& memo) {
	// We can not get a negative score, we return 0 for negative values
	if(n < 0) return 0;
	
	// Check if a solution already exists in the vector
	if (memo[n] != -1) return memo[n];

	// Else, we recursively calculate the solution for the 
	// given value and store it in our solution vector
	return memo[n] = ScoringOptionsRec(n - 1, memo) + 
					 ScoringOptionsRec(n - 2, memo) +
				   	 ScoringOptionsRec(n - 4, memo);
}



// Scoring options are 1, 2, and 4
long ScoringOptions(int n) {
	// Initializing our solution vector
	std::vector<long> memo(n + 1, {-1});

	// Set up the base case, 1 way to score 0
	memo[0] = 1;

	// Pass our vector to the helper function
	return ScoringOptionsRec(n, memo);
}

// Helper function to print a vector
std::string PrintVec(std::vector < int > dims) {
  std::string res = "";
  for (auto i: dims) {
    res = res + std::to_string(i) + ", ";
  }
  res.pop_back();
  res.pop_back();
  return res;
}

// Driver code
int main() {
  std::vector<int> totalScores = {3, 5, 10, 25, 0};

  // You can uncomment the line below and check how this top-down solution executes without a time-out 
  // totalScores.push_back({50});

  for (int i = 0; i < totalScores.size(); i++) {
    std::cout << i + 1 << ".\tn: " << totalScores[i] << "\n\n\tNumber of ways to reach the score: " << ScoringOptions(totalScores[i]) << std::endl;
    std::cout << std::string(100, '-') << std::endl;
  }
}
```
