# AutoViz
AutoViz (Automatic Visualization) is a Python library designed to simplify data visualization and exploratory data analysis (EDA). It uses a single line of code to automatically generate visualizations for datasets of any size. 
## Getting Started:
  1. Perform a pip installation
  2. In command line: pip install autoviz or go to https://pypi.org/project/autoviz/
  3. Import the library
       from autoviz import Autoviz_Class
  4. If using a notbook, charts can be displayed with in the notebook (inline)
       %matplotlib inline
  5. Create an instance of AutoViz
       AV = AutoViz_Class()
  6. Fill in Parameters
## Parameters
**filename:** File path to your CSV, TXT, or JSON file.  
**sep:** Separator to define the delimiter in the data file  
**depVar:** Dependent variable  
**dfte:** Use a data frame instead of a file.  
**header:** Define the row with the headings.  
**verbose:** Controls the amount of detail of analysis progress (0-2).  
**lowess:** Use LOWESS smoothing in plots.  
**chart_format:** Select the file format of the plots (svg, png, jpg, bokeh, server, or html).  
**max_rows_analyzed:** Set limits for the number of rows to be analyzed.  
**max_cols_analyzed:** Set limits for the number columns to be analyzed.  
**save_plot_dir:** Specify a directory to save the plots to a file instead of displaying them within the notebook.
## FixDQ Function
AutoViz includes the FixDQ class, that helps address data quality issues.
  1. Handle Missing Data: Fill or drop missing values
  2. Remove Duplicates: Detects and removes duplicate rows
  3. Correct Column Data Types: Ensures each column has the correct type based on its content
  4. Other Quality Issues: Flags and handles low-information or problematic columns.
## Reference
  1. https://pypi.org/project/autoviz/
  2. https://github.com/AutoViML/AutoViz
  3. Seshadri, Ram (2020). GitHub - AutoViML/AutoViz: Automatically Visualize any dataset, any size with a single line of code.
