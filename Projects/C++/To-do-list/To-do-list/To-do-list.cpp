#include <iostream>
#include <vector>
using namespace std;
class to_do_list {
public:
	vector<vector<string>>vec;
	to_do_list() {
	}
	void add_item(string item) {
		vec.push_back({ item,"Uncompleted" });
	}
	void edit_item(int num, string new_item) {
		if (vec.size() >= num) { vec[num - 1][0] = new_item; }
		else { cout << "There is No Item to Edit" << endl; }
	}
	void delete_item(int num) {
		if (vec.size() >= num) {
			for (int i = num; i < vec.size(); i++) { vec[i - 1] = vec[i]; }
			vec[vec.size() - 1].clear();
			vec.resize(vec.size() - 1);
		}
		else { cout << "There is No Item to Delete" << endl; }
	}
	void complete_item(int num) {
		if (vec.size() >= num) { vec[num - 1][1] = "Completed"; }
		else { cout << "\nOut of Range!"; }
	}
	void uncomplete_item(int num) {
		if (vec.size() >= num) { vec[num - 1][1] = "Uncompleted"; }
		else { cout << "\nOut of Range!"; }
	}
	void show_list() {
		if (vec.size() == 0) { cout << "No Item Found" << endl; }
		else {
			cout << endl;
			for (int i = 0; i < vec.size(); i++) {
				cout << i + 1 << ") ";
				cout << vec[i][0];
				if (vec[i][1] == "Completed") { cout << "\t(Completed)" << endl; }
				else { cout << endl; }
			}
		}
	}
};
int main() {
	to_do_list list1 = to_do_list();
	cout << "\nWelcom to Yassin Bassam To-Do List\n";
	try{
		while (true) {
			cout << "\n1 - Add Item\n2 - Show Items\n3 - Edit Item\n4 - Delete Item\n5 - Complete Item\n6 - Uncomplete Item\n7 - Exit\n";
			int i1;
			cout << "\nEnter number from 1 to 6:";
			cin >> i1;
			if (i1 !=1 && i1 != 2 && i1 != 3 && i1 != 4 && i1 != 5 && i1 != 6 && i1 != 7) { throw i1; }
			if (i1 == 1) {
				string i2;
				cout << "Enter The Item:";
				cin >> i2;
				list1.add_item(i2);
			}
			else if (i1 == 2) { list1.show_list(); }
			else if (i1 == 3) {
				list1.show_list();
				int i3;
				cout << "\nEnter number of Item:";
				cin >> i3;
				if (i3>list1.vec.size()) { throw "out of range"; }
				string i4;
				cout << "Enter the New Item:";
				cin >> i4;
				list1.edit_item(i3, i4);
			}
			else if (i1 == 4) {
				list1.show_list();
				int i5;
				cout << "\nEnter number of Item:";
				cin >> i5;
				list1.delete_item(i5);
			}
			else if (i1 == 5) {
				list1.show_list();
				int i6;
				cout << "\nEnter number of Item:";
				cin >> i6;
				list1.complete_item(i6);
			}
			else if (i1 == 6) {
				list1.show_list();
				int i7;
				cout << "\nEnter number of Item:";
				cin >> i7;
				list1.uncomplete_item(i7);
			}
			else if (i1 == 7) { break; }
			else { cout << "\nPlease Enter number from 1 to 6!\n"; }
		}
	}
	catch (int e1) { cout << "\ninvaild number ,Please try again!\n"; }
	catch (const char *e2) { cout << "\nOut of range\n"; }
	catch (...) { cout << "\nUnexpected Error\n"; }
}