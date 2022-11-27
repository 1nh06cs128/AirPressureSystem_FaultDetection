# neurolab-mongo-python

![image](https://user-images.githubusercontent.com/57321948/196933065-4b16c235-f3b9-4391-9cfe-4affcec87c35.png)

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### Step 3 - check if Git is installed and is on what Version

```bash
git --version
```

### Step 4 - Downnload Data Set

```bash
wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv
```

### Terminal Command History

```bash
abc@4788b49e1e4f:~/workspace$ history
    1  git --version
    2  pip install --upgrade pip
    3  python --version
    4  wget
    5  wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv
    6  pip install -r requirements.txt
    7  python data_dump.py 

       # check if git pointing to different repo
    8  git remote -v

       # move repo to point to our orgin
    9  git remote remove origin
    10  git remote -v
    11  git log
  
        # git remote add variableName (usually origin) <your repo loc>
    12  git remote add origin https://github.com/1nh06cs128/ AirPressureSystem_FaultDetection.git
    
        #git push variableName BranchName
    13  git pull origin main

        #git push variableName BranchName
    14  git push origin main

    15  git log
        # Point to latest Commit ID
    16  git reset --soft 6afd
    
    17  git add -m "This is my initial commit"
    18  git push -f origin main
    19  git add .
    20  git status
    
        #-> Error to updated config
    21  git commit -m "This is my 1st Commit"
    22  git config --global user.email "sb.1nh06cs128@gmail.com"
    23  git config --global user.name "1nh06cs128"
    24  git commit -m "This is my 1st Commit"
    25  git push origin main


    git commit -m "README.md file updated in neuron lab"
    git log

```

