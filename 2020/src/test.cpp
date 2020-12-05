#include <iostream>
#include <string>
#include <sstream>

int main()
{
    std::string s("1234"), t("4567");
    std::stringstream ss;
    int u;
    
    ss << s;
    ss >> u;

    std::cout << u << "\n";

    ss.str("");
    ss.clear();

    ss << t;
    ss >> u;

    std::cout << u << "\n";
}
