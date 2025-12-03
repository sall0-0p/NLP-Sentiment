import pandas as pd
import glob
import os

def unite_csv_files(input_folder='/Opinions/', output_filename='consolidated_opinions.csv'):
    # Pattern to match all csv files in the provided folder
    file_pattern = os.path.join(input_folder, "*.csv")
    all_files = glob.glob(file_pattern)
    
    # List to store individual DataFrames
    df_list = []
    
    # Definition of the desired final column structure
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
    
    # Dictionary to map inconsistent headers to the standard format
    # This handles typos, different cases, and alternative naming conventions found in the source files
    column_mapping = {
        'product_name': 'product_name',
        'Product Name': 'product_name',
        'opinion_id': 'original_id',
        'Opinion ID': 'original_id',
        'id': 'original_id',
        'sentiment': 'sentiment',
        'Sentiment': 'sentiment',
        'sntiment': 'sentiment',   # Fixes typo in opinions_AP.csv
        'statement': 'sentiment',  # Fixes typo in opinions_ND.csv
        'opinion': 'opinion',
        'Opinion': 'opinion',
        'opinion(text)': 'opinion', # Fixes naming in opinions_MP.csv
        'score': 'score',
        'Score': 'score',
        'date': 'date',
        'Date': 'date'
    }

    print(f"Found {len(all_files)} CSV files. Processing...")

    for filename in all_files:
        if filename.endswith(output_filename):
            continue # Skips the output file if it already exists in the folder

        try:
            # reading with engine='python' and sep=None allows pandas to sniff the delimiter (, or ;)
            df = pd.read_csv(filename, sep=None, engine='python')
            
            # Normalizes column names: remove whitespace and map to standard names
            df.columns = df.columns.str.strip()
            df.rename(columns=column_mapping, inplace=True)
            
            # Adds a column to track which file the data came from
            df['source_file'] = os.path.basename(filename)
            
            # Ensures all expected columns exist; fills missing ones with None/NaN
            for col in final_columns:
                if col not in df.columns:
                    df[col] = None
            
            # Reorders columns to match the standard structure and filters out unexpected columns
            df = df[final_columns]
            
            df_list.append(df)
            print(f"Successfully processed: {os.path.basename(filename)}")
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    if not df_list:
        print("No data frames to concatenate.")
        return

    # Concatenates all processed dataframes into one
    unified_df = pd.concat(df_list, ignore_index=True)
    
    # Generates a clean, sequential ID starting from 1
    unified_df['unified_id'] = range(1, len(unified_df) + 1)
    
    # Writes the final result to CSV
    unified_df.to_csv(output_filename, index=False)
    print(f"\nSuccess! Unified data saved to: {output_filename}")
    print(f"Total records: {len(unified_df)}")

if __name__ == "__main__":
    # Assumes files are in the current working directory. 
    # Change the path below if files are in a specific subfolder, e.g., './data'
    unite_csv_files('./Opinions')