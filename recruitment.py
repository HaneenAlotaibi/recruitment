# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills():
     skills=['Python','C++','Javascript','Juggling','Running','Eating']
     return skills
     
# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    print('Skills:')
    count=1
    for skill in skills:
        print(f"{count}. {skill}")
        count=1+count

# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    show_skills(skills)
    user_skills=[]
    for num_skills in range(0,2):  
      user_skills_choose=int(input("Choose a skill from above by entering its number: "))
      user_skills.append(skills[(user_skills_choose)-1])
    return user_skills
# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv={}
    user_name=input("What's your name? ")
    cv['name']=user_name
    user_age=int(input("How old are you? "))
    cv['age']=user_age
    user_experience=int(input("How many years of experience do you have? "))
    cv['experience']=user_experience
    cv['skills']=get_user_skills(skills)
    return cv
# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    #print("in check_acceptance")
    if 25< cv['age'] <40 : 
     #print(cv['age'])
     if cv['experience'] >3 :
       #print(cv['experience'])
       for skill in cv['skills'] :
        #print(skill)
        #print(desired_skill+"de")
        if desired_skill == skill:
          #print("true")
          return True    
    return False

def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions:")
    skills=get_skills()
    desired_skill='Javascript'
    cv=get_user_cv
    #show_skills( get_skills())
    #print(get_user_skills(get_skills()))
    #rint(get_user_cv(get_skills()))
    #print(check_acceptance(get_user_cv(skills),desired_skill))
    if check_acceptance(get_user_cv(skills),desired_skill) ==True:
     print(f"You have been accepted ")
    else:
       print(f"You have been rejected ") 
if __name__ == "__main__":
    main()
