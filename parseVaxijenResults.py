import re
import pandas as pd

if __name__=="__main__":
    with open('vaxijen_results.txt', 'r') as f: #change name file with yours xxx.txt
        file = f.read()
        file = re.sub(r'[\s]*', '', file)
        file = re.sub(r'[\n]*', '', file)

        #lookup for the sample text to know the format
        result = re.findall(r'YourSequence\:\>([A-Z]+)OverallPredictionfortheProtectiveAntigen[=]([-]?[0-9]*[.][0-9]*)\(Probable([A-Z]+[-]?[A-Z]*)\)', file)
        print(result)

        df = pd.DataFrame(result, columns=['sequence','score','conclusion'])
        print(df)
        df.to_csv('vaxijen_results.csv',index=False) #change name file with yours xxx.csv