/*
	Simple affine cipher by Sarah Sahibzada. Will only accept linear equations mod 26 (will make the parsing more elaborate later).
	Developed for use in MATH470 at Texas A&M University.
*/
#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>
#include <sstream>
#define ALPHABET_SIZE 26
#define CAPS_OFFSET 65
#define LOWERCASE_OFFSET 97

using namespace std;


//super elementary tokenizer
vector<string> tokenize_encryption_equation(string parseable) {	
	vector<string> token_vector;
	string::iterator iter = parseable.begin();
	string current_line;
	stringstream str;
	current_line = "";
	str << *iter;

while (iter != parseable.end()) {
	//cout << *iter << endl;
	current_line = "";
	if (isalpha(*iter) || *iter == '=' || *iter ==  '+') {
		current_line += *iter;
		token_vector.push_back(current_line);
		++iter;
		}
	else if (isdigit(*iter)) {
		while (isdigit(*iter)) {
			current_line += *iter;
			++iter;
			}
		token_vector.push_back(current_line);
	}
	else {
		++iter;
	}
}

	return token_vector;
}

//since this is going to be used by at least one other student in MATH470, 
//bool verify_linear_equation()
//not done yet

vector<string> generate_decryption_equation(string parseable)
{
	vector<string> encryption_equation = tokenize_encryption_equation(parseable);

}

string encrypt(string parseable, vector<string> equation) {
	string encrypted = "";
	string::iterator iter = parseable.begin();
	int multiplier = stoi(equation[2]);
	int shift = stoi(equation[equation.size() - 1]);
	while (iter != parseable.end()) {
		
		if (isspace(*iter)) {
			//cout << "here" << endl;
			++iter;
			encrypted += ' ';
		}
		else {
			//cout << "there" << endl;
			if (isupper(*iter)) {
				int offset_letter = *iter - CAPS_OFFSET;
				int encrypted_letter = (((multiplier * offset_letter) + shift) % ALPHABET_SIZE) + CAPS_OFFSET;
				encrypted += (char)encrypted_letter;
			}
			else if (islower(*iter)) {
				int offset_letter = *iter - LOWERCASE_OFFSET;
				int encrypted_letter = (((multiplier * offset_letter) + shift) % ALPHABET_SIZE) + LOWERCASE_OFFSET;
				encrypted += (char)encrypted_letter;
			}
			else {
				encrypted += *iter;
			}
			/*else if (isdigit(*iter)) {
				encrypted += (int)(((multiplier * (*iter)) + shift) % 9 );
				cout << encrypted << endl;
			}*/
			++iter;
		}
	}
	return encrypted;
}



int main()
{
	string equation;
	string to_encrypt;
	string final;
	string response;
	bool continue_program = true;
	vector<string> tokenized_equation;
	cout << "********AFFINE CIPHER ENCRYPTION********" << endl;
	while (continue_program) {
	cout << "Please enter an encryption function in the form y = ax + b. (Mod 26 is implicit in the definition of an affine cipher; do NOT enter it)" << endl;
	getline(cin, equation);
	tokenized_equation = tokenize_encryption_equation(equation);
	cout << "Please enter a message to encrypt." << endl;
	getline(cin, to_encrypt);
	cout << "Your encrypted message is below:" << endl;
	final = encrypt(to_encrypt, tokenized_equation);
	cout << final << endl;
	cout << "Run again? (yes or no)";
	getline(cin, response);
	for (int i = 0; i < response.size(); ++i) {
		response[i] = tolower(response[i]);
	}
	if (response != "yes") 
		continue_program = false;
	//else main();

}
	cout << "Simple linear affine encryption program by Sarah Sahibzada. Thank you for using and have a lovely day!! (:" << endl;
	return 0;
	}

