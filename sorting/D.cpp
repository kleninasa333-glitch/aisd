#include <iostream>
#include <vector>

void BubbleSort(std::vector<int> &arr) {
	int n = arr.size();
	int N = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                N += 1;                
            }
        }
    }
    std::cout << N << std::endl;
}

int main() {
	int n;
    std::cin >> n;
    std::vector <int> arr(n);
    
    for (int i = 0;i < n; i++){
    	std::cin >> arr[i];
	}

    BubbleSort(arr);

    return 0;
}
