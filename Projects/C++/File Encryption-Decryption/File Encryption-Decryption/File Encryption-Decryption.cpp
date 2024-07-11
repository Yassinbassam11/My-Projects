#include <iostream>
#include <cmath>
using namespace std;
char letter_encryption(char c,int key) {
	while (key <= 0) { key += 26; }
		if (c >= 'A' && c <= 'Z') { return char('A' + (c - 'A' + key) % 26); }
		else if (c >= 'a' && c <= 'z') { return char('a' + (c - 'a' + key) % 26); }
		else { cout << "\nError\n"; }
}
char letter_decryption(char c, int key) {
	int new_key = 26 - key;
	return letter_encryption(c, new_key);
}
char number_encryption(char c,int key){
	while (key <= 0) { key += 10; }
	if (c >= '0' && c <= '9') { return char('0' + (c - '0' + key) % 10); }
	else { cout << "\nError\n"; }
}
char number_decryption(char c, int key) {
	int new_key = 10 - key;
	return number_encryption(c, new_key);
}

string encryption(string s,int key) {
	string result;
	for (char c : s) {
		if (int(c) >= 65 && int(c) <= 90) {
			result += letter_encryption(c,key);
		}
		else if (int(c) >= 97 && int(c) <= 122) {
			result += letter_encryption(c, key);
		}
		else if (int(c) >= 48 && int(c) <= 57) {
			result += number_encryption(c, key);
		}
		else { result += c; }
	}
	return result;
}
string decryption(string s,int key) {
	string result;
	for (char c : s) {
		if (int(c) >= 65 && int(c) <= 90) {
			result += letter_decryption(c, key);
		}
		else if (int(c) >= 97 && int(c) <= 122) {
			result += letter_decryption(c, key);
		}
		else if (int(c) >= 48 && int(c) <= 57) {
			result += number_decryption(c, key);
		}
		else { result += c; }
	}
	return result;
}
int main() {
	cout << "\nWelcome to Yassin bassam Encryption-Decryption program:\n";
	while (true) {
		cout << "\n1) Encryption\n2) Decryption\n3) Exit\n";
		int i1;
		cout << "\nEnter number from 1 to 3:";
		cin >> i1;
		if (i1 == 1) {
			string i2;
			cout << "Enter the text that you want to Encode:";
			cin >> i2;
			int i3;
			cout << "Enter the key number:";
			cin >> i3;
			cout << "\nEncryption Text:";
			cout << encryption(i2, i3) << endl;
		}
		else if (i1 == 2) {
			string i2;
			cout << "Enter the text that you want to Decode:";
			cin >> i2;
			int i3;
			cout << "Enter the key number:";
			cin >> i3;
			cout << "\nDecryption Text:";
			cout << decryption(i2, i3) << endl;
		}
		else if (i1 == 3) { cout << "\nBye!\n"; break; }
		else { cout << "\nPlease Enter number from 1 to 3!\n"; }
	}
}