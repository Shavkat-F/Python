import pandas as pd
from ace_tools import display_dataframe_to_user

# Load datasets
qa = pd.read_csv('/mnt/data/tackoverflow_qa.csv')
titanic = pd.read_csv('/mnt/data/titanic.csv')

# Inspect QA dataset structure
print("QA dataset columns:", qa.columns.tolist())
display_dataframe_to_user("First few rows of QA dataset", qa.head())

# Homework 2 filters on QA data
qa['creation_date'] = pd.to_datetime(qa['creation_date'])

# Q1: Created before 2014
hw2_q1 = qa[qa['creation_date'] < '2014-01-01']
display_dataframe_to_user("Q1: Questions created before 2014", hw2_q1)

# Q2: Score > 50
hw2_q2 = qa[qa['score'] > 50]
display_dataframe_to_user("Q2: Questions with score > 50", hw2_q2)

# Q3: Score between 50 and 100
hw2_q3 = qa[(qa['score'] >= 50) & (qa['score'] <= 100)]
display_dataframe_to_user("Q3: Questions with score between 50 and 100", hw2_q3)

# Determine answerer column for Q4–Q8
answer_cols = [col for col in qa.columns if 'answerer' in col.lower()]
answer_col = answer_cols[0] if answer_cols else None

if answer_col:
    # Q4: Answered by Scott Boston
    hw2_q4 = qa[qa[answer_col] == 'Scott Boston']
    display_dataframe_to_user("Q4: Questions answered by Scott Boston", hw2_q4)
    
    # Q5: Answered by a list of 5 users (replace with actual names)
    users_list = ['User1','User2','User3','User4','User5']
    hw2_q5 = qa[qa[answer_col].isin(users_list)]
    display_dataframe_to_user("Q5: Questions answered by specified 5 users", hw2_q5)
    
    # Q6: Created Mar–Oct 2014, answered by Unutbu, score < 5
    hw2_q6 = qa[
        (qa['creation_date'] >= '2014-03-01') &
        (qa['creation_date'] <= '2014-10-31') &
        (qa[answer_col] == 'Unutbu') &
        (qa['score'] < 5)
    ]
    display_dataframe_to_user("Q6: Qs Mar–Oct 2014 by Unutbu with score < 5", hw2_q6)
    
    # Q7: Score 5–10 or view_count > 10000
    view_cols = [col for col in qa.columns if 'view' in col.lower()]
    view_col = view_cols[0] if view_cols else None
    if view_col:
        hw2_q7 = qa[((qa['score'] >= 5) & (qa['score'] <= 10)) | (qa[view_col] > 10000)]
        display_dataframe_to_user("Q7: Score 5–10 or views > 10000", hw2_q7)
    
    # Q8: Not answered by Scott Boston
    hw2_q8 = qa[qa[answer_col] != 'Scott Boston']
    display_dataframe_to_user("Q8: Questions not answered by Scott Boston", hw2_q8)

# Inspect Titanic dataset structure
print("\nTitanic dataset columns:", titanic.columns.tolist())
display_dataframe_to_user("First few rows of Titanic dataset", titanic.head())

# Homework 3 filters on Titanic data

# Q1: Female in Class 1, age 20–30
hw3_q1 = titanic[
    (titanic['Sex'] == 'female') &
    (titanic['Pclass'] == 1) &
    (titanic['Age'].between(20, 30))
]
display_dataframe_to_user("HW3 Q1: Female Pclass 1, Age 20–30", hw3_q1)

# Q2: Fare > $100
hw3_q2 = titanic[titanic['Fare'] > 100]
display_dataframe_to_user("HW3 Q2: Paid fare > $100", hw3_q2)

# Q3: Survived & alone
hw3_q3 = titanic[
    (titanic['Survived'] == 1) &
    (titanic['SibSp'] == 0) &
    (titanic['Parch'] == 0)
]
display_dataframe_to_user("HW3 Q3: Survived and traveling alone", hw3_q3)

# Q4: Embarked 'C' & fare > $50
hw3_q4 = titanic[
    (titanic['Embarked'] == 'C') &
    (titanic['Fare'] > 50)
]
display_dataframe_to_user("HW3 Q4: Embarked from 'C' and paid > $50", hw3_q4)

# Q5: Siblings/spouses and parents/children aboard
hw3_q5 = titanic[
    (titanic['SibSp'] > 0) &
    (titanic['Parch'] > 0)
]
display_dataframe_to_user("HW3 Q5: Had siblings/spouses and parents/children", hw3_q5)

# Q6: Age ≤ 15 & not survived
hw3_q6 = titanic[
    (titanic['Age'] <= 15) &
    (titanic['Survived'] == 0)
]
display_dataframe_to_user("HW3 Q6: Age ≤ 15 who didn't survive", hw3_q6)

# Q7: Known cabin & fare > 200
hw3_q7 = titanic[
    titanic['Cabin'].notna() &
    (titanic['Fare'] > 200)
]
display_dataframe_to_user("HW3 Q7: Known cabin and fare > $200", hw3_q7)

# Q8: Odd-numbered PassengerId
hw3_q8 = titanic[titanic['PassengerId'] % 2 == 1]
display_dataframe_to_user("HW3 Q8: Odd-numbered PassengerId", hw3_q8)

# Q9: Unique ticket numbers
ticket_counts = titanic['Ticket'].value_counts()
unique_tickets = ticket_counts[ticket_counts == 1].index
hw3_q9 = titanic[titanic['Ticket'].isin(unique_tickets)]
display_dataframe_to_user("HW3 Q9: Passengers with unique tickets", hw3_q9)

# Q10: 'Miss' in name, female, Class 1
hw3_q10 = titanic[
    titanic['Name'].str.contains('Miss') &
    (titanic['Sex'] == 'female') &
    (titanic['Pclass'] == 1)
]
display_dataframe_to_user("HW3 Q10: 'Miss' in name, female, Pclass 1", hw3_q10)


import pandas as pd
from ace_tools import display_dataframe_to_user

# Reload QA dataset and adjust column names
qa = pd.read_csv('/mnt/data/tackoverflow_qa.csv')
qa.rename(columns={
    'creationdate': 'creationdate',
    'viewcount': 'viewcount',
    'ans_name': 'answerer'
}, inplace=True)
qa['creationdate'] = pd.to_datetime(qa['creationdate'], errors='coerce')

# Homework 2
# Q1: Created before 2014
hw2_q1 = qa[qa['creationdate'] < '2014-01-01']
display_dataframe_to_user("Q1: Created before 2014", hw2_q1)

# Q2: Score > 50
hw2_q2 = qa[qa['score'] > 50]
display_dataframe_to_user("Q2: Score > 50", hw2_q2)

# Q3: Score between 50 and 100
hw2_q3 = qa[(qa['score'] >= 50) & (qa['score'] <= 100)]
display_dataframe_to_user("Q3: Score between 50 and 100", hw2_q3)

# Q4: Answered by Scott Boston
hw2_q4 = qa[qa['answerer'] == 'Scott Boston']
display_dataframe_to_user("Q4: Answered by Scott Boston", hw2_q4)

# Q5: Answered by specified 5 users (replace with actual names)
users_list = ['User1', 'User2', 'User3', 'User4', 'User5']
hw2_q5 = qa[qa['answerer'].isin(users_list)]
display_dataframe_to_user("Q5: Answered by 5 users", hw2_q5)

# Q6: Created Mar–Oct 2014, answered by Unutbu, score < 5
hw2_q6 = qa[
    (qa['creationdate'] >= '2014-03-01') &
    (qa['creationdate'] <= '2014-10-31') &
    (qa['answerer'] == 'Unutbu') &
    (qa['score'] < 5)
]
display_dataframe_to_user("Q6: Mar–Oct 2014 by Unutbu, score < 5", hw2_q6)

# Q7: Score 5–10 or viewcount > 10000
hw2_q7 = qa[((qa['score'] >= 5) & (qa['score'] <= 10)) | (qa['viewcount'] > 10000)]
display_dataframe_to_user("Q7: Score 5–10 or viewcount > 10000", hw2_q7)

# Q8: Not answered by Scott Boston
hw2_q8 = qa[qa['answerer'] != 'Scott Boston']
display_dataframe_to_user("Q8: Not answered by Scott Boston", hw2_q8)

# Load Titanic dataset
titanic = pd.read_csv('/mnt/data/titanic.csv')

# Homework 3
# Q1: Female in Class 1, Age 20–30
hw3_q1 = titanic[
    (titanic['Sex'] == 'female') &
    (titanic['Pclass'] == 1) &
    (titanic['Age'].between(20, 30))
]
display_dataframe_to_user("HW3 Q1: Female Pclass 1, Age 20–30", hw3_q1)

# Q2: Fare > 100
hw3_q2 = titanic[titanic['Fare'] > 100]
display_dataframe_to_user("HW3 Q2: Fare > $100", hw3_q2)

# Q3: Survived and alone
hw3_q3 = titanic[
    (titanic['Survived'] == 1) &
    (titanic['SibSp'] == 0) &
    (titanic['Parch'] == 0)
]
display_dataframe_to_user("HW3 Q3: Survived & alone", hw3_q3)

# Q4: Embarked 'C' & Fare > 50
hw3_q4 = titanic[
    (titanic['Embarked'] == 'C') &
    (titanic['Fare'] > 50)
]
display_dataframe_to_user("HW3 Q4: Embarked C & Fare > $50", hw3_q4)

# Q5: SibSp > 0 & Parch > 0
hw3_q5 = titanic[
    (titanic['SibSp'] > 0) &
    (titanic['Parch'] > 0)
]
display_dataframe_to_user("HW3 Q5: SibSp & Parch > 0", hw3_q5)

# Q6: Age ≤ 15 & not survived
hw3_q6 = titanic[
    (titanic['Age'] <= 15) &
    (titanic['Survived'] == 0)
]
display_dataframe_to_user("HW3 Q6: Age ≤ 15 not survived", hw3_q6)

# Q7: Known cabin & Fare > 200
hw3_q7 = titanic[
    titanic['Cabin'].notna() &
    (titanic['Fare'] > 200)
]
display_dataframe_to_user("HW3 Q7: Cabin known & Fare > $200", hw3_q7)

# Q8: Odd PassengerId
hw3_q8 = titanic[titanic['PassengerId'] % 2 == 1]
display_dataframe_to_user("HW3 Q8: Odd PassengerId", hw3_q8)

# Q9: Unique ticket numbers
ticket_counts = titanic['Ticket'].value_counts()
unique_tickets = ticket_counts[ticket_counts == 1].index
hw3_q9 = titanic[titanic['Ticket'].isin(unique_tickets)]
display_dataframe_to_user("HW3 Q9: Unique tickets", hw3_q9)

# Q10: 'Miss' in Name, female, Pclass 1
hw3_q10 = titanic[
    titanic['Name'].str.contains('Miss') &
    (titanic['Sex'] == 'female') &
    (titanic['Pclass'] == 1)
]
display_dataframe_to_user("HW3 Q10: 'Miss' & female & Pclass 1", hw3_q10)
