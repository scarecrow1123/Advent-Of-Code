#include <iostream>
#include <string>
#include <sstream>
#include <tuple>
#include <locale>
#include <optional>
#include <fstream>

namespace parser
{
    namespace
    {
        void clearStream(std::stringstream& ss) {
            ss.str("");
            ss.clear();
        }

        int eatNumber(std::string::const_iterator& seek, std::string::const_iterator& end, std::stringstream& ss) {
            int number;
            while (std::isdigit(*seek, std::locale())) {
                ss << *seek;
                ++seek;
            }

            ss >> number;
            clearStream(ss);
            return number;
        }

        char eatAlphabet(std::string::const_iterator& seek, std::string::const_iterator& end, std::stringstream& ss) {
            char letter;
            while (std::isalpha(*seek, std::locale())) {
                ss << *seek;
                ++seek;
            }

            ss >> letter;
            clearStream(ss);
            return letter;
        }

        std::optional<std::string> eatString1(std::string::const_iterator& seek, std::string::const_iterator& end, std::stringstream& ss, char c, int minCount, int maxCount) {
            std::string st;
            int cCount = 0;
            while (std::isalpha(*seek, std::locale())) {
                if (*seek == c) {
                    cCount += 1;
                }
                ss << *seek;
                ++seek;
            }

            if (! (cCount >= minCount && cCount <= maxCount))
                return {};
            else {
                ss >> st;
                clearStream(ss);
                return st;
            }
        }

        std::optional<std::string> eatString2(std::string::const_iterator& seek, std::string::const_iterator& end, std::stringstream& ss, char c, int pos1, int pos2) {
            std::string st;
            while (std::isalpha(*seek, std::locale())) {
                ss << *seek;
                ++seek;
            }

            ss >> st;
            clearStream(ss);

            if (st[pos1-1] == c ^ st[pos2-1] == c)
                return st;
            else
                return {};
        }

        void eatOtherChars(std::string::const_iterator& seek, std::string::const_iterator& end, std::stringstream& ss) {
            while (! (std::isalpha(*seek, std::locale()) or std::isdigit(*seek, std::locale()))) {
                ss << *seek;
                ++seek;
            }
            clearStream(ss);
        }
    }

    bool parseAndCheckPolicy(const std::string& passwordPolicy, bool part1) {
        std::stringstream ss;
        int num1, num2;
        char letter;
        std::optional<std::string> password;

        std::string::const_iterator seek = passwordPolicy.begin();
        std::string::const_iterator end = passwordPolicy.end();

        num1 = eatNumber(seek, end, ss);
        eatOtherChars(seek, end, ss);
        num2 = eatNumber(seek, end, ss);
        eatOtherChars(seek, end, ss);
        letter = eatAlphabet(seek, end, ss);
        eatOtherChars(seek, end, ss);

        if (part1)
            password = eatString1(seek, end, ss, letter, num1, num2);
        else
            password = eatString2(seek, end, ss, letter, num1, num2);

        return password.has_value();
    }
}

int main()
{
    std::ifstream is("../data/day02.txt");
    std::string passwordPolicy;
    int valid1Count = 0, valid2Count = 0;
    while (std::getline(is, passwordPolicy)) {
        bool valid1 = parser::parseAndCheckPolicy(passwordPolicy, true);
        bool valid2 = parser::parseAndCheckPolicy(passwordPolicy, false);
        if (valid1)
            valid1Count += 1;
        if (valid2)
            valid2Count += 1;
    }
    std::cout << "Part 1: " << valid1Count << " Part 2: " << valid2Count << "\n";
    return 0;
}