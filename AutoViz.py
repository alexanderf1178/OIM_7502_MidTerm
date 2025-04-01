"""Name: Alex Fichtner
Library: AutoViz
URL: https://pypi.org/project/autoviz/
Description: AutoViz is a Python library designed to simplify data visualization and exploratory data analysis (EDA). It uses a single line of code to automatically generate visualizations for datasets of any size. It supports CSV, TXT, and JSON files. AutoViz creates various plots, such as scatter plots, distribution plots, heatmaps, etc. that can be exported in different formats."""

from autoviz import AutoViz_Class # Import the AutoViz class
AV = AutoViz_Class() # Create an instance of the AutoViz class
filename = "C:/Users/alexa/Documents/PythonProject/Wage.csv" # Define file you want analyze
dft = AV.AutoViz( # Call the Autoviz function
    filename,
    sep=",", # Separator used in dataset
    depVar="", # Dependent variable
    dfte=None, #Pandas data frame
    header=0, # Define the row for column headers
    verbose=2, # Level of verbosity
    lowess=False, # LOWESS smoothing
    chart_format="html", # Chart file formats
    max_rows_analyzed=150000, # Max number of rows
    max_cols_analyzed=30, # Max number of columns
    save_plot_dir="C:/Users/alexa/Documents/PythonProject" # Where to save the charts
)