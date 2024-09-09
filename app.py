import kaggle
import os
import pandas as pd

# setting up kaggle
os.environ['KAGGLE_CONFIG_DIR'] = r'C:\Users\javeria\.kaggle'

# continuously being updated
dataset = 'piterfm/paris-2024-olympic-summer-games'

# download path:
download_path = r'C:\Users\javeria\Downloads\Data Analyst Projects\Olympics Dashboard\Data'

# need to remove previous files to prevent duplicates
for file in os.listdir(download_path):
    file_path = os.path.join(download_path, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)  # get ridda it
            print(f"Deleted {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

# download the dataset using the Kaggle API and unzip the files
kaggle.api.dataset_download_files(dataset, path=download_path, unzip=True)

# list of CSV files to be imported and used
csv_files = [
    'athletes.csv',
    'events.csv',
    'medallists.csv',
    'medals.csv',
    'medals_total.csv',
    'schedules.csv',
    'schedules_preliminary.csv',
    'teams.csv',
    'torch_route.csv',
    'venues.csv'
]

# initialize a dictionary to hold df
dataframes = {}

# iterate through each CSV and load it into the df
for file in csv_files:
    # construct the full path to the CSV file
    file_path = os.path.join(download_path, file)
    
    # load the CSV file into a df
    df = pd.read_csv(file_path)
    
    # add the df to the dictionary using the file name as the key
    table_name = file.split('.')[0]  # remove the .csv extension
    dataframes[table_name] = df
