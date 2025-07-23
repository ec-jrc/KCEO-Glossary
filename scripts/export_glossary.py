# exporting all definitions for each level, i.e. all first definitions go in one file, all second definitions and so on
import glob
import pandas as pd 
import os

os.makedirs("exports/parquet/", exist_ok=True)
os.makedirs("exports/xlsx/", exist_ok=True)

for definition_no in list(range(1,6)):

    all_files = []
    for file in glob.glob("docs/terms/*.md"):

    # which definition to extract? up to 5 different definitions in uncertainty
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        #---
        try: 
            title = content.split("title: ")[1].strip().split("\n")[0].strip() # there is always a title and it#s always on top of the file, no other checks needed
        except:
            print(file)
        #---
        tags = ""
        header = content.split("---")[1]
        try: 
            tags = header.split("tags:")[1].strip().split("---")[0].strip()
        except IndexError: # if there are no tags
            pass
        #---
        synonyms = ""
        relevant_passage = content.split("## 1 Definition")[0]
        try: 
            synonyms = relevant_passage.split(f"**Synonyms**:")[1].strip().split("## 1 Definition")[0].strip()
        except IndexError: # if there are no synonyms
            pass
        #---
        try:
            relevant_content = content.split(f"## {definition_no} Definition")[1].strip().split("___")[0].strip()
        except IndexError:
            continue
        #---
        definition = relevant_content.split("### Notes")[0].strip()
        #---
        try:
            notes = relevant_content.split("### Notes")[1].strip().split("### Examples")[0].strip()
        except:
            print(file)
        #---
        examples = relevant_content.split("### Examples")[1].strip().split("### Sources")[0].strip()
        #---
        sources = relevant_content.split("### Sources")[1].strip().split("___")[0].strip()
        #---

        all_cols = [title,tags,synonyms,definition,notes,examples,sources]
        all_files.append(all_cols)

    df = pd.DataFrame(all_files, columns=["term","tags","synonyms","definition","notes","examples","sources"])

    df.to_parquet(f"exports/parquet/terms_definition_{definition_no}.parquet",index=False)
    df.to_excel(f"exports/xlsx/terms_definition_{definition_no}.xlsx",index=False)
    # not exporting to csv or other legacy formats due to problems with complicated strings and cell seperators!
    all_files = []
