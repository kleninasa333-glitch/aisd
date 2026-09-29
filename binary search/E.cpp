#include <iostream>
#include <vector>

void dist_kor(std::vector<int> &st, int N, int K){
	int low = 1;
	int high = st[N - 1] - st[0];
	int dist = 0;
	
	while (low <= high){
		int mid = low + (high - low)/2;
		
		int count = 1;
		int last_pos = st[0];
		for (int i = 1; i < N; i++) {
			if (st[i] - last_pos >= mid){
				count++;
				last_pos = st[i];
			}
		}
		if (count >= K){
			dist = mid;
			low = mid + 1;
		} else {
			high = mid - 1;
		}
	}
	std::cout << dist << std::endl;
}


int main (){
	int N;
	int K;
	std::cin >> N >> K;
	std::vector<int> st(N);
	for (int i = 0; i < N; i++){
		std::cin >> st[i];
	}
	
	dist_kor(st, N, K);
	
	return 0;
}
