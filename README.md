# Davis Putnam without CNF
Automated Theorem Proving based on the [Davis-Putnam](https://en.wikipedia.org/wiki/Davis%E2%80%93Putnam_algorithm?oldformat=true) algorithm

* Shane Aston
* Dr. Bram van Heuveln
* Intermediate Logic, RPI, Spring 2016

---
## How to Use

### From Website
Routes:

 * `/`
    - Add New Argument
        - Input fields for the Title of the argument, any number of Premises, and a Conclusion
        - Click the `Add Premise` button to add an additional premise to the argument
        - Title and Conclusion fields are required
    - Existing Arguments
        - List of all of the previously submitted arguments
        - Selecting any of these will bring you to the respective `/argument/` page

 * `/argument/<argument name>`
    - Argument (Premises and Conclusion)
    - Satisfiability and Argument Validity
    - Resulting Davis-Putnam Tree

 * `/about`
    - `README.md` rendered as an About page

### From Command Line
 * Navigate to the `davisputnam/` directory
 * Run `python main.py <input file> <output file directory>`
    - `<input file>` is a relative path to the input file to run on (see File Format)
    - `<output file directory>` is a relative path to the directory that the resulting tree images will be stored in. The images will be stored as `.png` files with the same name as the given input file
 * Ascii-art tree will be displayed in the terminal, along with the satisfiability and validity of the argument
 * A `.png` of the resulting tree will be placed in the `<output file directory>`

### Test Suite
 * Navigate to the `davisputnam/` directory
 * Run `make test`

---
## File Format
* Each line contains an individual statement
* The last line is considered to be the Conclusion
* Literals: Uppercase Letters `A`, `B`, `C`, ...
* Supported Logical Connectors
    - Negation `~`
    - Disjunction `v`
    - Conjunction `^`
    - Implication `->`
    - Biconditional `<->`
* Example: Modus Ponens

```

P->Q

P

Q

```

---
## Resources
* [Notes on Resolution and Davis-Putnam](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&cad=rja&uact=8&ved=0ahUKEwi5lbb6s9_LAhVBOSYKHZreCEMQFggtMAM&url=http%3A%2F%2Fwww.rpi.edu%2F~heuveb%2Fteaching%2FLogic%2FInterLogic%2FNotes%2FATP.ppt&usg=AFQjCNHkslzpLK4PeenEpD5x523sslbEKQ&sig2=Le_yfNjm-IHvXzjF1wHLcw)
* <https://github.com/astonshane/DavisPutnam>
    - Language: _Python_
    - Implementation of the Davis-Putnam Algorithm using the CNF statement set
    - Computability and Logic - Spring 2015
* <https://github.com/astonshane/DavisPutnamGo>
    - Language: _Go_
    - Implementation of the Davis-Putnam Algorithm using the CNF statement set
    - RCOS - Fall 2015
* <https://github.com/astonshane/DavisPutnamNoCNF> (_This Project_)
    - Language: _Python_
    - Implementation of the Davis-Putnam Algorithm modified to operate on the statements themselves instead of the CNF statement set
    - Intermediate Logic - Spring 2016
