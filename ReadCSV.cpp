#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <regex>

const std::regex comma(",");

int main()
{
    std::cout << "hi ihihi" << std::endl;
    // Open source file.
    std::ifstream mesh("procssing_times_table.csv");

    // Here we will store the result
    std::vector<std::vector<std::string>> point_coordinates;

    // We want to read all lines of the file
    std::string line{};
    while (mesh && getline(mesh, line)) {
        // Tokenize the line and store result in vector. Use range constructor of std::vector
        std::vector<std::string> row{ std::sregex_token_iterator(line.begin(),line.end(),comma,-1), std::sregex_token_iterator() };
        point_coordinates.push_back(row);
    }
    // Print result. Go through all lines and then copy line elements to std::cout
    std::for_each(point_coordinates.begin(), point_coordinates.end(), [](std::vector<std::string> & vs) {
        std::copy(vs.begin(), vs.end(), std::ostream_iterator<std::string>(std::cout, " ")); std::cout << "\n"; });

    return 0;
}