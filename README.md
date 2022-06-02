# Count amino acid substitutions 

Simple program that counts amino acid changes in each position against reference sequnce.

## Description

- Create a list of amino acid substitutions from multiple  - sequences in single fasta file.
- Seaqunces needs to bee alligned before.
- Results are saved in a csv file

## Getting Started

### Dependencies

* BioPython

### Executing program

* Run python script 
* Results are saved in rez.csv  

```
python parse.py example.fasta
```

NOT IMPLEMENTED: Pass referece sequence seperately.  

```
python parse.py example.fasta reference.fasta
```  

### Jupyter notebooks  

Download mutation data from lapis.cov-spectrum.org [here](./count_mutations.ipynb)  
Count mutation from allignment [here](./parse.ipynb)  

## Help

To see help run command without any parameters
```
python parse.py
```

## Authors


Name: Edgars Liepa

Twitter: [@liepa_edgars](https://twitter.com/liepa_edgars)

email: edgars.liepa@biomed.lu.lv

## TODO

- [ ] add that you can specify reference optinally in other file
- [ ] make jupyer notebook for analysis example
- [ ] Crete system tests 

## Version History

* 0.1
    * Initial Release 

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

## Bonus: The README Checklist

A helpful checklist to gauge how your README is coming along:

- [ ] One-liner explaining the purpose of the module
- [ ] Necessary background context & links
- [ ] Potentially unfamiliar terms link to informative sources
- [ ] Clear, *runnable* example of usage
- [ ] Installation instructions
- [ ] Extensive API documentation
- [ ] Performs [cognitive funneling](https://github.com/noffle/art-of-readme#cognitive-funneling)
- [ ] Caveats and limitations mentioned up-front
- [ ] Doesn't rely on images to relay critical information
- [ ] License
