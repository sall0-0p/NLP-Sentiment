import pandas as pd
import glob
import os

def unite_csv_files(input_folder='.', output_filename='consolidated_opinions.csv'):
    # Finds all CSV files in the specified directory
    file_pattern = os.path.join(input_folder, "*.csv")
    all_files = glob.glob(file_pattern)
    
    df_list = []
    
    # Defines the standard column order for the output file
    final_columns = [
        'unified_id', 
        'original_id', 
        'product_name', 
        'sentiment', 
        'opinion', 
        'score', 
        'date', 
        'source_file'
    ]
    
    # Maps various column names found in source files to a standard format
    column_mapping = {
        'product_name': 'product_name',
        'Product Name': 'product_name',
        'opinion_id': 'original_id',
        'Opinion ID': 'original_id',
        'id': 'original_id',
        'sentiment': 'sentiment',
        'Sentiment': 'sentiment',
        'sntiment': 'sentiment',   # Handles typo found in source data
        'statement': 'sentiment',  # Handles typo found in source data
        'opinion': 'opinion',
        'Opinion': 'opinion',
        'opinion(text)': 'opinion', # Handles variation in source data
        'score': 'score',
        'Score': 'score',
        'date': 'date',
        'Date': 'date'
    }

    print(f"Found {len(all_files)} CSV files. Processing...")

    for filename in all_files:
        # Prevents processing the output file if it already exists
        if filename.endswith(output_filename):
            continue 

        try:
            # Reads the file, automatically detecting the separator (comma or semicolon)
            df = pd.read_csv(filename, sep=None, engine='python')
            
            # Standardizes column names
            df.columns = df.columns.str.strip()
            df.rename(columns=column_mapping, inplace=True)
            
            # Tracks the source filename for reference
            df['source_file'] = os.path.basename(filename)
            
            # Ensures the 'opinion' column exists, then removes line breaks
            if 'opinion' in df.columns:
                # Replaces newlines with spaces and strips leading/trailing whitespace
                df['opinion'] = df['opinion'].astype(str).str.replace(r'[\r\n]+', ' ', regex=True).str.strip()
            
            # Adds missing columns with empty values to ensure consistent structure
            for col in final_columns:
                if col not in df.columns:
                    df[col] = None
            
            # Filters and reorders columns to match the final structure
            df = df[final_columns]
            
            df_list.append(df)
            print(f"Successfully processed: {os.path.basename(filename)}")
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    if not df_list:
        print("No data frames to concatenate.")
        return

    # Combines all dataframes into a single dataframe
    unified_df = pd.concat(df_list, ignore_index=True)
    
    # Creates a new sequential ID to resolve overlapping original IDs
    unified_df['unified_id'] = range(1, len(unified_df) + 1)
    
    # Exports the consolidated data to a CSV file
    unified_df.to_csv(output_filename, index=False)
    print(f"\nSuccess! Unified data saved to: {output_filename}")
    print(f"Total records: {len(unified_df)}")

if __name__ == "__main__":
    # execute the function on the current directory
    unite_csv_files('./Opinions')