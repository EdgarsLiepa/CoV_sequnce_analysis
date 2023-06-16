#  Analysis of the nucleocapsid and spike proteins of SARS-Cov-2

This repository consists of python scripts and notebooks used to select best imunogenetic epitopes of the nucleocapsid and spike proteins of SARS-Cov-2 by combining solvent accessebility, predicted peptides and mutation data.

Created for scientific project at **Latvian biomedical and reaserch center** .  

## Description

!! IMPORTANT !!

**Curently this repository is under development and might not have all needed files and examples.**

- Download SARS-Cov-2 variant mutation data
- Load and process predicted epitope data tables for B-cell, T-cell data (MHC-I and MHC-II) and structural data.
- Add to B-cell and T-cel data tables structural and mutation data.
- Create epitope lists in excel files for variants of concern with structural and mutation statistics.
- SARS-Cov-2 sequnce allignment and mmino acid substitution statistics from GISAID data. (Currently partially impllemented)

## Main analysis files  

Combine mutation data, predicted SARS-Cov-2 variant epitops and structuraldata  [count_mutations.ipynb](./count_mutations.ipynb)  

Transform brewery 5.0 result structurald data files to JSON structures [parseStruct.ipynb](./parseStruct.ipynb)  
  
Count mutation from allignment [parse.ipynb](./parse.ipynb)  

## Getting Started

For detailed descriptions of used piepeline look at [count_mutations.ipynb](./count_mutations.ipynb)  

[count_mutations.ipynb](./count_mutations.ipynb) rely on JSON files created with [parseStruct.ipynb](./parseStruct.ipynb)  
  
[parse.ipynb](./parse.ipynb) currently is not used in epitope analysis pipeline, but was left on this project if there is need to make mutation frequency data from full SARS-Cov-2 S and N protein sequnce data. 

### Dependencies

* Plotly 

* Pandas

* BioPython 

* All CSV files are expected to have delimination symbol ";"  

* Scripts were created and tested on python 3.10.4 64 bit version

* Hugging faces Transformer api for ESM AI model.

### Directory structure 

spikeProt and NProt directories contain data files used in analyasis and epitope result tables.  

- **Linear Epitopes** - folder with scripts for linear epitope 3D protein structure generation using ESM machine learning model and visualization. 

In "data" foleder B-cell, MHC-I, MHC-II hold csv input files with predicted B and T cell epitope data. 
Epitope data were predicted using tools from IEDB: 
- **B-cell** http://tools.iedb.org/bcell/
- **MHC-I** http://tools.iedb.org/mhci/
- **MHC-II** http://tools.iedb.org/mhcii/




```
project
│   README.md
│   count_muation.ipynb
|   parse.ipynb
|   parse.py
|   parseStruct.ipynb
│
└───sProt
│   │   S_epitope_alpha.xlsx
│   │   S_epitope_beta.xlsx
│   │   ...
|   |
│   └───data
│       └───B-cell
|           |   alpha.csv
|           |   beta.csv
|           |   ...
|
│       └───MHC-I
|           |   alpha.csv
|           |   beta.csv
|           |   ...
│       └───MHC-II
|           |   alpha.csv
|           |   beta.csv
|           |   ...
|       └───reference_sequences
|           |   alpha_S.fasta
|           |   beta_S.fasta
|           |   ...
|       └───struct   
│   
└───nProt
│   │   S_epitope_alpha.xlsx
│   │   S_epitope_beta.xlsx
│   │   ...
|   |
│   └───data
|       └───B-cell
|           | ...
|       └───MHC-I
|       └─── ...
|
|___Linear epitopes
    |___longLinkers
    |
    |___shortLinkers
    |
    |   generate-3D-struct-combinations.ipynb
    |   show_best_models.ipynb


```

### Executing python program

* Run python script 
* Results are saved in rez.csv  

```
python parse.py example.fasta
```

NOT IMPLEMENTED: Pass referece sequence seperately.  

```
python parse.py example.fasta reference.fasta
```  

### Help

To see help run command without any parameters
```
python parse.py
```

## Authors

Name: Edgars Liepa  

email: edgars.liepa@biomed.lu.lv  

LinkedIn: [Edgars Liepa](https://www.linkedin.com/in/edgars-liepa-b85083129/)

Twitter: [@liepa_edgars](https://twitter.com/liepa_edgars)


## Version History

* 0.1
    * Initial Release 

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## TODO

- [ ] add that you can specify reference optinally in other file
- [ ] Crete tests 

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

## Bonus: The README Checklist

A helpful checklist to gauge how your README is coming along:

- [X] One-liner explaining the purpose of the module
- [X] Necessary background context & links
- [ ] Potentially unfamiliar terms link to informative sources
- [ ] Clear, *runnable* example of usage
- [ ] Installation instructions
- [ ] Extensive API documentation
- [ ] Performs [cognitive funneling](https://github.com/noffle/art-of-readme#cognitive-funneling)
- [ ] Caveats and limitations mentioned up-front
- [x] Doesn't rely on images to relay critical information
- [ ] License
