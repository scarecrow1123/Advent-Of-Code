#include <iostream>
#include <fstream>
#include <vector>

int part1(const std::vector<int>& numbers) {
    for (int i = 0; i < numbers.size(); ++i) {
        for (int j = 0; j < numbers.size(); ++j) {
            if (i == j)
                continue;
            if (numbers[i] + numbers[j] == 2020) {
                // std::cout <<  << " ---- " << numbers[i] << " | " << numbers[j] << "\n";
                return numbers[i] * numbers[j];
            }
        }
    }
}

int part2(const std::vector<int>& numbers) {
    for (int i = 0; i < numbers.size(); ++i) {
        for (int j = 0; j < numbers.size(); ++j) {
            for (int k = 0; k < numbers.size(); ++k) {
                if (i == j or j == k or i == k)
                    continue;
                if (numbers[i] + numbers[j] +numbers[k] == 2020) {
                    // std::cout <<  << " ---- " << numbers[i] << " | " << numbers[j] << " | " << numbers[k] << "\n";
                    return numbers[i] * numbers[j] * numbers[k];
                }
            }
        }
    }
}

int main()
{
    std::ifstream is("../data/day01.txt");
    std::vector<int> numbers;
    int num;
    while (is >> num) {
        numbers.push_back(num);
    }
    
    std::cout << part1(numbers) << "\n" << part2(numbers) << "\n";

    return 0;
}