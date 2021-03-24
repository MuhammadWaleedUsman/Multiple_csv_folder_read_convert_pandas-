import pandas as pd
import glob


def tsv_to_csv_batch(input_folder, output_folder):
    try:
        all_files = glob.glob(input_folder + "/*.tsv.gz")
        for filename in all_files:
            df = pd.read_csv(filename, sep='\t', index_col=False)
            print(df.head())
            name = filename.split('.')[0].split('\\')[1]
            output_file = '{0}/{1}.csv'.format(output_folder,name)
            df.to_csv(path_or_buf=output_file, index=False)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    input_path = 'raw'
    output_path = 'csv_folder'
    tsv_to_csv_batch(input_folder=input_path, output_folder=output_path)
