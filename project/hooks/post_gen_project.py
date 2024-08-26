help = """
Your project has been created!
________________________________________________________________
    _    _  _______   ____ ___ ___  _   _ _____ 
   / \  | |/ / ____| | __ )_ _/ _ \| \ | |  ___|
  / _ \ | ' /|  _|   |  _ \| | | | |  \| | |_   
 / ___ \| . \| |___  | |_) | | |_| | |\  |  _|  
/_/   \_\_|\_\_____| |____/___\___/|_| \_|_|    
________________________________________________________________
You can now create a workspace for each of your analyses using:

cd {{cookiecutter.repo_name}}/analyses
cookiecutter bionf_cookiecutter --directory="analysis"

As soon as an analysis generated a "milestone", 
i.e. figures, tables, or files that will be used in other analyses
save them in the milestones/ directory of the project.

Once you are finished with an analysis, 
add corresponding rules to the snakemake file of the project.

Don't forget to sync this project to GitHub. 


Good Luck!
"""
print(help)
