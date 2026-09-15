#include <iostream>
#include <vector>
void BubbleSort(std::vector<int> &arr){
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] < arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}


int main() {
    std::vector<int> arr;
    int x;
    while (std::cin >> x) {
        arr.push_back(x);
    }

    BubbleSort(arr);
    for (int i = 0; i < arr.size(); i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
