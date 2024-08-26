help = """
Your analysis has been created!
________________________________________________________________
    _    _  _______   ____ ___ ___  _   _ _____ 
   / \  | |/ / ____| | __ )_ _/ _ \| \ | |  ___|
  / _ \ | ' /|  _|   |  _ \| | | | |  \| | |_   
 / ___ \| . \| |___  | |_) | | |_| | |\  |  _|  
/_/   \_\_|\_\_____| |____/___\___/|_| \_|_|    
________________________________________________________________

If you create a new conda environment for this analysis. Please remember to regularly save
your environment to a file:

mamba create --name {{cookiecutter.repo_name}} python=3.11
mamba activate {{cookiecutter.repo_name}}
mamba env export > environment.yml

You can install the python package in this directory to your local conda environment with:

pip install -e .

You will need to manually add large data files to .gitignore to prevent it from syncing to
version control.

Have fun!
"""
print(help)
