#include <iostream>
#include <vector>

int main() {
    int N, K;
    std::cin >> N >> K;

    std::vector<int> ver(N);
    for (int i = 0; i < N; i++) {
        std::cin >> ver[i];
    }

    int low = 1;
    int high = 10000000;
    int ans = 0;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        int count = 0;
        for (int i = 0; i < N; i++) {
            count += ver[i] / mid;
        }

        if (count >= K) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    std::cout << ans << std::endl;
    return 0;
}
