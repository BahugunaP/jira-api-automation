# STEP1 : Generate Jira Access Token 

# STEP2 : Create virtual envoronment 
python -m venv venv
venv\Scripts\activate

# STEP3: Install all required packages 
pip install -r requirements.txt

# STEP 4: Freeze dependencies:
pip freeze > requirements.txt

# Step 5: 