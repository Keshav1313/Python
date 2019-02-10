import logging
import os
import pandas
import textract
import lib


list_of_files = {}
for (r "C:\\company_resume_files") as f in  #directory pathname anything we can pass
os.walk("f"):
    for filename in f:
        if filename.endswith('.txt'):
            list_of_files[f] = os.sep.join([f])
            file = open(f, 'r')
            file.read()
            file.close()
print (list_of_files)

def main():
@@ -33,16 +38,32 @@ def extract():
    # TODO Docstring
    logging.info('Begin extract')

    # TODO Create list of candidate files
    # Reference variables
    candidate_file_agg = list()

    # Create list of candidate files
    for root, subdirs, files in os.walk(lib.get_conf('Company_resume_directory')):

    # TODO Subset candidate files to supported extensions
        folder_files = map(lambda x: os.path.join(root, x), files)
        candidate_file_agg.extend(folder_files)

    # TODO Attempt to extract text from files
    # Convert list to a pandas DataFrame
    observations = pandas.DataFrame(data=candidate_file_agg, columns=['file_path'])
    logging.info('Found {} candidate files'.format(len(observations.index)))

    # TODO Archive schema and return
    # Subset candidate files to supported extensions
    observations['extension'] = observations['file_path'].apply(lambda x: os.path.splitext(x)[1])
    observations = observations[observations['extension'].isin(lib.AVAILABLE_EXTENSIONS)]
    logging.info('Subset candidate files to extensions w/ available parsers. {} files remain'.
                 format(len(observations.index)))

    # Attempt to extract text from files
    observations['text'] = observations['file_path'].apply(textract.process)

    # Archive schema and return
    lib.archive_dataset_schemas('extract', locals(), globals())
    logging.info('End extract')
    pass
    return observations

def transform():
    pass

#The resume get parsed with each template now we find only text for our requirement.
while list_of_files== True:
    with open('list_of_files','rb') as wrd:
    with open('output.txt','a') as wf:
        page=wrd.read()
        link_exits=True   #it will check the link with comparison value.
        while link_exist:
            pos=page.find("Name","Skill","Experience")
            if pos == -1:
                link_exist = False
            else:
                first_quote=page.find("*/",pos)
                second_quote=page.find('\n',first_quote+1) #as am not able to get correct logic for name only so trying to print till line ends.

                demand_from_resume=page[first_quote+1:second_quote]
                wf.write(demand_from_resume + '\n')
                page=page[second_quote:]
