#include <iostream>
#include <vector>

void CountSort(std::vector<int>& A) {
    int count[101] = {0};
    
    for (int i = 0; i < (int)A.size(); i++) {
        count[A[i]]++;
    }
    
    int idx = 0;
    for (int val = 0; val <= 100; val++) {
        for (int k = 0; k < count[val]; k++) {
            A[idx++] = val;
        }
    }
}

int main() {
    std::vector<int> A;
    int x;
    while (std::cin >> x) {
        A.push_back(x);
    }
    
    CountSort(A);
    
    for (int i = 0; i < (int)A.size(); i++) {
        std::cout << A[i] << " ";
    }
    
    return 0;
}
