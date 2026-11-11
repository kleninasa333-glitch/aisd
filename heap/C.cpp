#include <iostream>
#include <string>
using namespace std;

int heap[200005];
int cnt = 0;

void siftUp(int i) {
    while (i > 1 && heap[i] < heap[i / 2]) {
        int t = heap[i];
        heap[i] = heap[i / 2];
        heap[i / 2] = t;
        i = i / 2;
    }
}

void siftDown(int i) {
    while (2 * i <= cnt) {
        int j = 2 * i;
        if (j + 1 <= cnt && heap[j + 1] < heap[j]) {
            j = j + 1;
        }
        if (heap[i] <= heap[j]) {
            break;
        }
        int t = heap[i];
        heap[i] = heap[j];
        heap[j] = t;
        i = j;
    }
}

void add(int x) {
    cnt++;
    heap[cnt] = x;
    siftUp(cnt);
}

int extractMin() {
    int result = heap[1];
    heap[1] = heap[cnt];
    cnt--;
    siftDown(1);
    return result;
}

int main() {
    string cmd;
    while (cin >> cmd) {
        if (cmd == "CLEAR") {
            cnt = 0;
        } else if (cmd == "ADD") {
            int x;
            cin >> x;
            add(x);
        } else {
            if (cnt == 0) {
                cout << "CANNOT" << endl;
            } else {
                cout << extractMin() << endl;
            }
        }
    }
    return 0;
}
