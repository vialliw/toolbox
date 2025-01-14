<img src="https://raw.githubusercontent.com/vialliw/Hyperion_Data_Science_Bootcamp/main/image/python_library.jfif" alt="vialliw toolbox" width="280" height="280">

*The path to a meaningful life is paved with repeated acts of kindness.*


<details>
<summary><b>[duplicate-file-checker.py] Duplicate file searcher script</b></summary>
  
*This script recursively searches through directories and identifies duplicate files by comparing their SHA256 hashes.*

1. [duplicate-file-checker.py](https://github.com/vialliw/toolbox/blob/main/duplicate-file-checker.py)
2. This script provides several key features:
   1. Recursively scans all subdirectories
   2. Uses SHA256 for reliable file comparison
   3. Handles large files efficiently by reading in chunks
   4. Resolves symbolic links to avoid duplicates
   5. Provides human-readable file sizes
   6. Handles errors gracefully (permission issues, missing files)
   7. Tracks processed files to avoid redundant calculations
   8. Groups duplicate files by their hash values
   9. Shows summary statistics of duplicate files found
3. To use the script:
   1. Save it to a file (e.g., find_duplicates.py)
   2. Run it: python find_duplicates.py
   3. Enter the directory path when prompted

</details>


<details>
<summary><b>[vw_toolbox.py] Miscellaneous handy python functions</b></summary>
  
*I am tired of repeatedly adding error handling for frequent tasks, so I write these codes to make my life easier.*
  
1. [vw_toolbox.py](https://github.com/vialliw/toolbox/blob/main/vw_toolbox.py)
2. ask_user_input_int(msg: str, error_handling: bool = True) -> int **Note** *(Ask user input integer with error handling)*
3. ask_user_input_num(msg: str, error_handling: bool = True) -> float **Note** *(Ask user input float with error handling)*
4. convert_list_to_a_string(contents_to_print: list[str], delimiter: str = " ") -> str **Note** *(Convert list of values into delimiter separated string)*
5. print_in_one_line(contents_to_print: list[str], delimiter: str = " ") -> None **Note** *(Print list of values with delimiter separated string)*
</details>


<details>
<summary><b>[TestVWToolbox.py] Unit test script for vw_toolbox</b></summary>

*This is the unit test script for vw_toolbox.py.*
  
1. [TestVWToolbox.py](https://github.com/vialliw/toolbox/blob/main/TestVWToolbox.py)
2. Usage: In command prompt, type "python .\TestVWToolbox.py".

</details>

<details>
<summary><b>[install_python_package.bat] Windows batch script to install user specified python package</b></summary>

*This installation script will check if the package has been installed in your system first.*

1. [install_python_package.bat](https://github.com/vialliw/toolbox/blob/main/install_python_package.bat)
2. Usage: In command prompt, type "install_python_package.bat <package>".
3. Example: type "install_python_package.bat pandas"

</details>

