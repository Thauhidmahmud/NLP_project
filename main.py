
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()
#GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

class BaseModel:
   
    def get_model(self):
        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model=genai.GenerativeModel("gemini-2.5-flash")
            return model
        
        except Exception as e:
            print(e)


class AppFeature(BaseModel):
    def __init__(self):
        self.__database={}
        self.first_menu()

    
    def first_menu(self):
        first_input=int(input("""
        Hi! How would you like to proceed?
                          
            1. Not a Member? Register
            2. Already a Member? Login
            3. Bhai galti se as gaya kia? Exit
            """))
        if first_input==1:
            self.__register()
        elif first_input==2:
            self.__login()
        else:
            exit()


    def second_menu(self):
        second_input=int(input("""
        Hi! How would you like to proceed?
                           
        1. Sentiment Analysis
        2. Language Translation
        3. Language Detection  
        4. Text Summary   
        5. Text Classification  
        6. Keyword Extraction            
        """))

        if second_input==1:
            self.Sentiment_Analysis()
        elif second_input==3:
            self.Language_Detection()
        elif second_input==2:
            self.language_translation()
        elif second_input==4:
            self.Text_summary()
        elif second_input==5:
            self.Text_classification()
        elif second_input==6:
            self.Keyword_Extraction()
        else:
            exit()


    def Sentiment_Analysis(self):
        text=input("Enter your text: ")
        model=self.get_model()
        response=model.generate_content(f"Give me the sentiment of this sentence, the answere is 1 line:{text}")
        result=response.text 
        print(result)  
        self.second_menu()  

    def language_translation(self):
        pro=input("Enter your language: ")
        text = input("Enter your text: ")
        model=self.get_model()
        response=model.generate_content(f"Give me {pro} translation of this sentence:{text}")
        result=response.text 
        print(result)  
        self.second_menu()

    def Language_Detection(self):
        text=input("Enter your text: ")
        model=self.get_model()
        response=model.generate_content(f"Detection the language of this sentence:{text}")
        result=response.text 
        print(result)  
        self.second_menu() 

    def Text_summary(self):
        text=input("Enter your Text: ")
        model=self.get_model()
        response=model.generate_content(f"Provide the summary of this Text:{text}")
        result=response.text 
        print(result)  
        self.second_menu() 

    def Text_classification(self):
        choice =input("Enter your Choice text: ")
        text = input("Enter your text: ")
        model = self.get_model()
        response=model.generate_content(f"give me short 1 line answere {choice} text Classification of this sentence:{text}")
        result=response.text 
        print(result)  
        self.second_menu() 

    def Keyword_Extraction(self):
        text = input("Enter your text: ")
        model = self.get_model()
        response=model.generate_content(f"provide Keyword of this sentence:{text}")
        result=response.text 
        print(result)  
        self.second_menu() 


    def __register(self):
        name=input("Enter your Name: ")
        email=input("Enter your Email: ")
        password=input("Enter your password: ")

        if email not in self.__database:
            self.__database[email]=[name,password]
            print("Registattion Successful. Now you can login.")
            self.first_menu()

        else:
            print("Email already exit.")
            self.first_menu()

    def __login(self):
        email=input("Enter your email: ")
        password=input("Enter your password: ")

        if email in self.__database:
            if self.__database[email][1]==password:
                print("Login Successful!")
                #second menu
                self.second_menu()
            else:
                print("Password Incorrect!")
                self.__login()
        else:
            print("Email not Found.Please Register first.")
            self.first_menu()
    
    


app=AppFeature()







