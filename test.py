import pandas as pd

def import_excel_to_dataframe(file_path):
    excel_data = pd.read_excel(file_path, sheet_name=None)
    dataframes = {}
    
    for sheet_name, sheet_data in excel_data.items():
        dataframes[sheet_name] = sheet_data
    
    user_input = input("Which sheet do you want to display? ")
    if user_input in dataframes:
        return dataframes[user_input]
    else:
        print("Invalid sheet name")
        columns = list(dataframes[user_input].columns)
        print("Available columns:", columns)
        
        selected_columns = input("Enter the columns you want to display (comma-separated): ").split(",")
        selected_columns = [col.strip() for col in selected_columns]
        
        filtered_df = dataframes[user_input][selected_columns]
        
        filter_input = input("Enter a filter (optional): ")
        if filter_input:
            filtered_df = filtered_df.query(filter_input)
        
        return filtered_df
        print("Filtered DataFrame:")
        print(filtered_df.head())
        example_filter = "column_name == 'example_value'"
        print("Example filter:", example_filter)
        filter_input = input("Enter a filter (optional): ")
        if filter_input:
            filtered_df = filtered_df.query(filter_input)
        
        return filtered_df
    
#q: schreibe eine main funktion, die die funktion import_excel_to_dataframe mit dem file_path "data.xlsx" aufruft und das ergebnis in einer variable speichert. gebe die variable aus.
def main():
    result = import_excel_to_dataframe("data.xlsx")
    print(result)
    