{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ffa2d212",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "%load_ext autoreload\n",
    "%autoreload 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e40b176c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# data_processing.py\n",
    "import pandas as pd\n",
    "%load_ext autoreload\n",
    "%autoreload 2\n",
    "\n",
    "def clean_column_names(data):\n",
    "    data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')\n",
    "    return data\n",
    "\n",
    "def clean_invalid_values(data):\n",
    "    data['gender'] = data['gender'].str.lower().replace({'femal': 'female', 'm': 'male'})\n",
    "    return data\n",
    "\n",
    "def format_data_types(data):\n",
    "    data['age'] = data['age'].astype(int)\n",
    "    data['date_of_birth'] = pd.to_datetime(data['date_of_birth'])\n",
    "    return data\n",
    "\n",
    "def handle_null_values(data):\n",
    "    data.dropna(inplace=True)  # Drops rows with null values\n",
    "    return data\n",
    "\n",
    "def remove_duplicates(data):\n",
    "    data.drop_duplicates(inplace=True)\n",
    "    return data\n",
    "\n",
    "def convert_numeric_to_int(data):\n",
    "    numeric_columns = data.select_dtypes(include='number').columns\n",
    "    data[numeric_columns] = data[numeric_columns].applymap(int)\n",
    "    return data\n",
    "\n",
    "def save_to_csv(data, filename):\n",
    "    data.to_csv(filename, index=False)\n",
    "\n",
    "def main():\n",
    "    # Load the data\n",
    "    data = pd.read_csv('data.csv')\n",
    "\n",
    "    # Exercise 1: Cleaning Column Names\n",
    "    data = clean_column_names(data)\n",
    "\n",
    "    # Exercise 2: Cleaning Invalid Values\n",
    "    data = clean_invalid_values(data)\n",
    "\n",
    "    # Exercise 3: Formatting Data Types\n",
    "    data = format_data_types(data)\n",
    "\n",
    "    # Exercise 4: Handling Null Values\n",
    "    data = handle_null_values(data)\n",
    "\n",
    "    # Exercise 5: Removing Duplicates\n",
    "    data = remove_duplicates(data)\n",
    "\n",
    "    # Exercise 6: Convert Numeric Variables to Integers\n",
    "    data = convert_numeric_to_int(data)\n",
    "\n",
    "    # Save the cleaned dataset to a new CSV file\n",
    "    save_to_csv(data, 'cleaned_data.csv')\n",
    "\n",
    "    # Print the cleaned and formatted data\n",
    "    print(data.head())\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "conda_env",
   "language": "python",
   "name": "conda_env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
