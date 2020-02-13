## Software Installation Instructions
We will be using the Conda environment management system, along with Intel's optimized Python distribution for this course. Research-oriented work flows can often involve multiple Python packages, and is not uncommon that a single researcher to work on multiple projects. As a result, managing disparate package versions and combinations becomes a necessity. **Conda** is a widely used tool that helps to manage such different Python package combinations. Using Conda, we will install Intel’s Python distribution, a set of useful Python packages that have been optimized by Intel for use on Intel processors. Intel’s Python distribution is free to use. Due to the significant performance enhancements offered by the Intel Python distribution, it is strongly recommended that you use it when working on Intel systems. The following steps should guide you through the installation process:

1. (You may skip this step if you already have Anaconda installed) Install Miniconda by choosing the appropriate **Python 3.7** installer from this link: https://conda.io/miniconda.html  
Windows, Mac, and Linux installers are provided, and we have tested all three 64-bit versions. Note that if you aren’t sure whether you need 64- or 32-bit functionality, you almost certainly want the 64-bit version. Once you’ve run the installation script, proceed to step 2.

2. Now that you have Conda installed, open up a terminal window (in Windows, select “Anaconda Prompt” from the start menu). Execute the following commands:
    1. ```bash
       conda update conda    # answer "yes"
       ```
    2. ```bash
       conda config --add channels intel
       ```
    3. ```bash
       conda create -n idp intelpython3_full python=3 jupyter    # answer "yes"
       ```   
       *__Note:__ "idp" is a nickname for this Python/package combo. You are free to use anything you wish in lieu of "idp."*
    
3. Once the installation is complete, you should see a message indicating that you can access your python installation by typing conda activate idp. If the installation appears to hang after several minutes, but the last file appears to be 100% downloaded, try hitting “enter.” That seems to wrap things up. The last step is to test your installation. To do so, type the following commands:  
    1. ```bash
       conda activate idp    # source activate idp    
       ```
    2. ```bash 
       python      
       ```
       You will be taken to an interactive Python prompt, and you will see a message indicating:   
       `Python 3.x.y | Intel Corporation |`  
       
       *__Note:__ If you see Python 2.x.y, you have installed the wrong version of python. Rerun the above command and make sure to say "python=3".*
    
    3. ```python
       import numpy
       ```
       Entering this at the Python prompt will import the NumPy module.
    
    4. ```python
       print(numpy.pi)
       ```
       Entering this at the Python prompt should display the value of pi ( 3.14159). If you see this, you’re installation is working!
    
    5. ```python
       exit()
       ```
       This is how we exit the Python interpreter:
    
    6. ```
       conda deactivate
       ```

Note that activation/deactivation is how we switch between different python installations in Conda. When we installed Conda, we also installed Python, but not Intel’s Python. After you have deactivated “idp,” try typing “python” again. You will probably see a different version number and distribution name. Running “activate idp” will point your environment back to the Intel Python (or whatever Python environment is associated with the nickname “idp”).
