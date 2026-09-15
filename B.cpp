#include <iostream>
#include <vector>

void InsertionSort(std::vector<int> &arr){
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        for (int j = i;  j > 0 && arr[j] < arr[j - 1]; j--) {
            std::swap(arr[j], arr[j - 1]);
        }  
    }
}

int main() {
    std::vector<int> arr;
    int x;
    while (std::cin >> x) {
        arr.push_back(x);
    }

    InsertionSort(arr);
    for (int i = 0; i < arr.size(); i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    
    return 0;
}