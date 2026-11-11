#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {
    priority_queue<int> q;
    string cmd;
    while (cin >> cmd) {
        if (cmd == "CLEAR") {
            q = priority_queue<int>();
        } else if (cmd == "ADD") {
            int x;
            cin >> x;
            q.push(x);
        } else {
            if (q.empty()) {
                cout << "CANNOT" << endl;
            } else {
                cout << q.top() << endl;
                q.pop();
            }
        }
    }
    return 0;
}
