#include <iostream>
#include <vector>

void kopii(int N, int x, int y){
	int low = 0;
	int high = std::max(N * x, N * y);
	int ans = high;
	
	while (low <= high){
		int mid = (low + high) /2;
		
		
		if (mid / x + mid / y >= N - 1) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
	}
	std::cout << ans + std::min(x, y) << std::endl;
}




int main (){
	int N, x, y, ans;
	std::cin >> N >> x >> y;
	
	kopii(N, x, y);
	
	return 0;
}
