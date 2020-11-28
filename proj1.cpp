// Andrea M. Stojanovski

#include <iostream>
//#include "proj1.h"
#include <fstream>
#include <string>
#include <map> // instead of dictionary

using namespace std;

int main (int argc, char *argv[]) {
    char line[256];
    if (argc != 2) {
        cerr << "Missing file name.";
        cerr << "Usage: prog <filename>";
        exit(1);
    }

    // mapping instructions
    map<string, string> instr_map { // key value types are both string
        {"add", "0000000000000000"}, 
        {"sub", "0000000000000001"},
        {"and", "0000000000000010"},
        {"or", "0000000000000011"},
        {"slt", "0000000000000100"},
        {"jr", "0000000000001000"},
        {"slti", "0010000000000000"},
        {"lw", "1000000000000000"},
        {"sw", "1010000000000000"},
        {"jeq", "1100000000000000"},
        {"addi", "1110000000000000"},
        {"j", "0100000000000000"},
        {"jal", "0110000000000000"},
        {"movi", "1110000000000000"},
        {"nop", "0000000000000000"}, 
        {"halt", "0100000000000000"}
    }; // end instr_map

    // location of lables
    map<string, int> label_map {
        // initialize as empty add as labels are found
    }; // end label_map
/*
    // print format
    string printer (address, bin_instr) {
        cout << "ram[" << address << "] = 16'b" << bin_instr << ";" << endl;
    } // end printer
*/
    // opening the file
    ifstream in(argv[1]);\
    if(!in) {
        cout << "Cannot open input file.\n";
        return 1;
    } // end if
    char str[255];
    while(in) {
        in.getline(str, 255);  // delim defaults to '\n'
        if(in) {
            int line_count;
            string temp_string;
            for(int i = 0; 0 != str[i]; i++) {
                char cur_char = str[i];
                while (cur_char != '#') { // this will remove anything after a comment
                    if (cur_char == ' ') {
                        // do nothing
                    } else if (cur_char == ':') { // these are labels
                        label_map.insert(temp_string, line_count);
                        temp_string += cur_char;
                    } else { // everything else will be added (, $ and chars)
                        temp_string += cur_char; // add commas
                    } // end if else
                } // end while
            } // end for

            while (temp_string.length() != 0) {
                line_count++;
            } // end while counter check
        } // end if(in)




    for(auto item: label_map) { // prints out each element
                    // Key                  Value
        cout << item.first << " : " << item.second << "\n";
        break;
    } // end for



    }
    in.close();


    return 0;
} // end main
