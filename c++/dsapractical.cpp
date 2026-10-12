
// #include <iostream>
// #include <stack>
// #include <string>
// #include <cctype>
// #include <cmath>
// using namespace std;

// int main() {
//     string exp;
//     stack<double> s;
    
//     cout << "Enter a postfix expression: ";
//     cin >> exp;

//     for (int i = 0; i < exp.length(); i++) {
//         char ch = exp[i];

//         if (isalpha(ch)) {
//             double value;
//             cout << "Enter value of " << ch << ": ";
//             cin >> value;
//             s.push(value);
//         }
//         else if (isdigit(ch)) {
//             s.push(ch - '0');
//         }
//         else {
//             double b = s.top();
//             s.pop();

//             double a = s.top();
//             s.pop();

//             switch (ch) {
//                 case '+': s.push(a + b); break;
//                 case '-': s.push(a - b); break;
//                 case '*': s.push(a * b); break;
//                 case '/': s.push(a / b); break;
//                 case '^': s.push(pow(a, b)); break;
//             }
//         }
//     }

//     cout << "Result = " << s.top() << endl;

//     return 0;
// }

// #include <iostream>
// using namespace std;

// struct Node {
//     int data;
//     Node* next;

//     Node(int value) : data(value), next(nullptr) {}
// };

// class Queue {
// private:
//     Node* frontNode;
//     Node* rearNode;

// public:
//     Queue() : frontNode(nullptr), rearNode(nullptr) {}

//     // Free all dynamically allocated nodes when the queue is destroyed
//     ~Queue() {
//         while (frontNode != nullptr) {
//             Node* temp = frontNode;
//             frontNode = frontNode->next;
//             delete temp;
//         }
//     }

//     bool isEmpty() const {
//         return frontNode == nullptr;
//     }

//     void enqueue(int value) {
//         Node* newNode = new Node(value);

//         if (isEmpty()) {
//             frontNode = rearNode = newNode;
//         } else {
//             rearNode->next = newNode;
//             rearNode = newNode;
//         }

//         cout << value << " added to the queue.\n";
//     }

//     void dequeue() {
//         if (isEmpty()) {
//             cout << "Queue is empty. Nothing to remove.\n";
//             return;
//         }

//         Node* temp = frontNode;
//         cout << temp->data << " removed from the queue.\n";
//         frontNode = frontNode->next;

//         if (frontNode == nullptr) {
//             rearNode = nullptr;
//         }

//         delete temp;
//     }

//     void showFront() const {
//         if (isEmpty()) {
//             cout << "Queue is empty.\n";
//         } else {
//             cout << "Front element: " << frontNode->data << '\n';
//         }
//     }

//     void display() const {
//         if (isEmpty()) {
//             cout << "Queue is empty.\n";
//             return;
//         }

//         cout << "Queue (front to rear): ";
//         Node* current = frontNode;

//         while (current != nullptr) {
//             cout << current->data << " ";
//             current = current->next;
//         }

//         cout << '\n';
//     }
// };

// int main() {
//     Queue queue;
//     int choice;
//     int value;

//     do {
//         cout << "\n--- Queue Menu ---\n"
//              << "1. Enqueue\n"
//              << "2. Dequeue\n"
//              << "3. View front element\n"
//              << "4. Display queue\n"
//              << "5. Check if queue is empty\n"
//              << "0. Exit\n"
//              << "Enter your choice: ";

//         if (!(cin >> choice)) {
//             cout << "Invalid input. Exiting.\n";
//             return 1;
//         }

//         switch (choice) {
//             case 1:
//                 cout << "Enter a value: ";
//                 if (!(cin >> value)) {
//                     cout << "Invalid input. Exiting.\n";
//                     return 1;
//                 }
//                 queue.enqueue(value);
//                 break;

//             case 2:
//                 queue.dequeue();
//                 break;

//             case 3:
//                 queue.showFront();
//                 break;

//             case 4:
//                 queue.display();
//                 break;

//             case 5:
//                 cout << (queue.isEmpty() ? "Queue is empty.\n"
//                                          : "Queue is not empty.\n");
//                 break;

//             case 0:
//                 cout << "Exiting program.\n";
//                 break;

//             default:
//                 cout << "Invalid choice. Please try again.\n";
//         }
//     } while (choice != 0);

//     return 0;
// }

// #include <iostream>
// using namespace std;

// struct Node {
//     int data;
//     Node* next;
// };

// Node *front = nullptr, *rear = nullptr;

// void enqueue(int x) {
//     Node* n = new Node{x, nullptr};

//     if (front == nullptr) {
//         front = rear = n;
//         n->next = n;
//     } else {
//         n->next = front;
//         rear->next = n;
//         rear = n;
//     }

//     cout << x << " added\n";
// }

// void dequeue() {
//     if (front == nullptr) {
//         cout << "Queue is empty\n";
//         return;
//     }

//     Node* temp = front;
//     cout << temp->data << " removed\n";

//     if (front == rear)
//         front = rear = nullptr;
//     else {
//         front = front->next;
//         rear->next = front;
//     }

//     delete temp;
// }

// void display() {
//     if (front == nullptr) {
//         cout << "Queue is empty\n";
//         return;
//     }

//     Node* temp = front;
//     do {
//         cout << temp->data << " ";
//         temp = temp->next;
//     } while (temp != front);

//     cout << '\n';
// }

// int main() {
//     int choice, value;

//     do {
//         cout << "\n1. Enqueue\n2. Dequeue\n3. Display\n0. Exit\nChoice: ";
//         cin >> choice;

//         switch (choice) {
//             case 1:
//                 cout << "Enter value: ";
//                 cin >> value;
//                 enqueue(value);
//                 break;
//             case 2:
//                 dequeue();
//                 break;
//             case 3:
//                 display();
//                 break;
//             case 0:
//                 cout << "Exiting\n";
//                 break;
//             default:
//                 cout << "Invalid choice\n";
//         }
//     } while (choice != 0);

//     return 0;
// }

// #include <iostream>
// using namespace std;

// struct Node {
//     int data;
//     Node* next;
// };

// int main() {
//     Node *head = nullptr, *tail = nullptr;
//     int n, value;

//     cout << "How many nodes? ";
//     cin >> n;

//     for (int i = 0; i < n; i++) {
//         cout << "Enter value for node " << i + 1 << ": ";
//         cin >> value;

//         Node* newNode = new Node{value, nullptr};

//         if (head == nullptr)
//             head = tail = newNode;
//         else {
//             tail->next = newNode;
//             tail = newNode;
//         }
//     }

//     cout << "Linked list: ";
//     for (Node* current = head; current != nullptr; current = current->next)
//         cout << current->data << " ";

//     cout << '\n';

//     // Free the allocated memory
//     while (head != nullptr) {
//         Node* temp = head;
//         head = head->next;
//         delete temp;
//     }

//     return 0;
// }

// #include <iostream>
// using namespace std;

// struct Node {
//     int data;
//     Node* next;
// };

// int main() {
//     int n, x, key;
//     cin >> n;

//     Node *head = nullptr, *tail = nullptr, *p;

//     while (n--) {
//         cin >> x;
//         p = new Node{x, nullptr};
//         if (!head) head = p;
//         else tail->next = p;
//         tail = p;
//     }

//     cin >> key;

//     Node *cur = head, *prev = nullptr;
//     while (cur && cur->data != key) {
//         prev = cur;
//         cur = cur->next;
//     }

//     if (cur) {
//         if (prev) prev->next = cur->next;
//         else head = cur->next;
//         delete cur;
//     }

//     for (p = head; p; p = p->next)
//         cout << p->data << " ";

//     return 0;
// }

// #include <iostream>
// using namespace std;

// struct Node {
//     int data;
//     Node* next;
// };

// void traverse(Node* head) {
//     if (head == nullptr) {
//         cout << "The list is empty.\n";
//         return;
//     }

//     Node* current = head;
//     cout << "Linked list: ";

//     while (current != nullptr) {
//         cout << current->data << " -> ";
//         current = current->next;
//     }

//     cout << "NULL\n";
// }

// int main() {
//     Node* head = nullptr;
//     Node* tail = nullptr;
//     int numberOfNodes, value;

//     cout << "Enter the number of nodes: ";
//     cin >> numberOfNodes;

//     if (numberOfNodes < 0) {
//         cout << "Invalid number of nodes.\n";
//         return 1;
//     }

//     for (int i = 1; i <= numberOfNodes; i++) {
//         cout << "Enter data for node " << i << ": ";
//         cin >> value;

//         Node* newNode = new Node{value, nullptr};

//         if (head == nullptr) {
//             head = tail = newNode;
//         } else {
//             tail->next = newNode;
//             tail = newNode;
//         }
//     }

//     traverse(head);

//     // Free the allocated memory
//     while (head != nullptr) {
//         Node* temp = head;
//         head = head->next;
//         delete temp;
//     }

//     return 0;
// }

// #include <iostream>
// using namespace std;

// struct Node {
//     int data;
//     Node* prev;
//     Node* next;
// };

// void insertEnd(Node*& head, Node*& tail, int value) {
//     Node* newNode = new Node{value, tail, nullptr};

//     if (head == nullptr)
//         head = tail = newNode;
//     else {
//         tail->next = newNode;
//         tail = newNode;
//     }
// }

// int main() {
//     Node *head = nullptr, *tail = nullptr;
//     int n, value;

//     cout << "Number of existing nodes: ";
//     cin >> n;

//     for (int i = 0; i < n; i++) {
//         cout << "Enter value: ";
//         cin >> value;
//         insertEnd(head, tail, value);
//     }

//     cout << "Enter value to insert: ";
//     cin >> value;
//     insertEnd(head, tail, value);

//     cout << "Doubly linked list: ";
//     for (Node* current = head; current != nullptr; current = current->next)
//         cout << current->data << " ";

//     cout << '\n';

//     while (head != nullptr) {
//         Node* temp = head;
//         head = head->next;
//         delete temp;
//     }

//     return 0;
// }

// #include <iostream>
// using namespace std;

// struct Node {
//     int data;
//     Node* prev;
//     Node* next;
// };

// int main() {
//     Node *head = nullptr, *tail = nullptr;
//     int n, value;

//     cout << "Number of nodes: ";
//     cin >> n;

//     // Create the list
//     for (int i = 0; i < n; i++) {
//         cout << "Enter value: ";
//         cin >> value;

//         Node* newNode = new Node{value, tail, nullptr};

//         if (head == nullptr)
//             head = newNode;
//         else
//             tail->next = newNode;

//         tail = newNode;
//     }

//     cout << "Value to delete: ";
//     cin >> value;

//     Node* current = head;
//     while (current != nullptr && current->data != value)
//         current = current->next;

//     if (current == nullptr) {
//         cout << "Value not found.\n";
//     } else {
//         if (current->prev != nullptr)
//             current->prev->next = current->next;
//         else
//             head = current->next;

//         if (current->next != nullptr)
//             current->next->prev = current->prev;
//         else
//             tail = current->prev;

//         delete current;
//         cout << "Node deleted.\n";
//     }

//     cout << "List: ";
//     for (current = head; current != nullptr; current = current->next)
//         cout << current->data << " ";

//     cout << '\n';

//     while (head != nullptr) {
//         Node* temp = head;
//         head = head->next;
//         delete temp;
//     }

//     return 0;
// // }

// #include <iostream>
// using namespace std;

// struct Node {
//     int data;
//     Node* prev;
//     Node* next;
// };

// int main() {
//     Node *head = nullptr, *tail = nullptr;
//     int n, value;

//     cout << "Number of nodes: ";
//     cin >> n;

//     // Create the list
//     for (int i = 0; i < n; i++) {
//         cout << "Enter value: ";
//         cin >> value;

//         Node* newNode = new Node{value, tail, nullptr};

//         if (head == nullptr)
//             head = newNode;
//         else
//             tail->next = newNode;

//         tail = newNode;
//     }

//     cout << "Value to delete: ";
//     cin >> value;

//     Node* current = head;
//     while (current != nullptr && current->data != value)
//         current = current->next;

//     if (current == nullptr) {
//         cout << "Value not found.\n";
//     } else {
//         if (current->prev != nullptr)
//             current->prev->next = current->next;
//         else
//             head = current->next;

//         if (current->next != nullptr)
//             current->next->prev = current->prev;
//         else
//             tail = current->prev;

//         delete current;
//         cout << "Node deleted.\n";
//     }

//     cout << "List: ";
//     for (current = head; current != nullptr; current = current->next)
//         cout << current->data << " ";

//     cout << '\n';

//     while (head != nullptr) {
//         Node* temp = head;
//         head = head->next;
//         delete temp;
//     }

//     return 0;
// }








