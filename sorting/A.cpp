#include <iostream>
#include <vector>

void SelectionSort(std::vector<int> &arr){
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int maxIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] > arr[maxIndex]) {
                maxIndex = j;
            }
        }
        if (maxIndex != i) {
            std::swap(arr[i], arr[maxIndex]);
        }  
    }
}

int main() {
    std::vector<int> arr;
    int x;
    while (std::cin >> x) {
        arr.push_back(x);
    }

    SelectionSort(arr);
    for (int i = 0; i < arr.size(); i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
