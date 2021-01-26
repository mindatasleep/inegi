from os import listdir
import pandas as pd


class Main:
    """ Import and preprocess INEGI 2020 census dataset.
    """

    def __init__(self):
        # Dataset directory
        self.dir = "datasets/"


    def run(self):
        """ Output a master census dataset by appending CSVs for each State.
        """
        # Import datasets
        filepaths = [self.dir + f for f in listdir(self.dir) if f.endswith('.csv')]

        # Concatenate into single DataFrame
        df = pd.concat(map(pd.read_csv, filepaths))

        # Derive cvegeo column
        df['CVEGEO'] = df["ENTIDAD"].astype(str).str.zfill(2) + df["MUN"].astype(str).str.zfill(3) + df["LOC"].astype(str).str.zfill(4) + df["AGEB"].astype(str).str.zfill(4)

        # Write DataFrame to CSV
        df.to_csv(".output/inegi_2020_master.csv")



if __name__ == "__main__":

    m = Main()
    m.run()