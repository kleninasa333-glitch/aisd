#include <iostream>
#include <algorithm>

int main() {
    long long w, h, n;
    std::cin >> w >> h >> n;

    long long low = 1;
    long long high = n * std::max(w, h);
    long long ans = high;

    while (low <= high) {
        long long mid = low + (high - low) / 2;

        if ((mid / w) * (mid / h) >= n) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    std::cout << ans << std::endl;
    return 0;
}
