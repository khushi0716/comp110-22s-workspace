
# Main function
def main():
    severity = input("Enter pneumonia severity:")
    age = int(input("Enter patient age:"))
    pregnancy = input("Is the patient pregnant? Enter yes or no:")
    med_plan_age(age, severity, pregnancy)
   

# Calculates the dosage of medicine based off of the pneumonia severity.
def med_plan_severity(severity: str):
    if (severity == "mild"):
        print("Dosage for antibiotic should be 250 mg every 8 hours for 3-5 days.")
        print("Antiviral medication should be taken 2 times a day for 1 week")
    elif (severity == "moderate"):
        print("Dosage for antibiotic should be 500 mg every 8 hours for 5-10 days.")
        print("Antiviral medication should be taken 2 times a day for a 1-2 weeks")
    else:
        print("Consider patient hosipitalization")
        print("Dosage for antibiotic should be 800 mg every 8 hours for 5-10 days.")
        print("Antiviral medication should be taken 3 times a day for a 2-3 week")


# Prints out the side effects of the drugs.
def amoxicillin():
    print("    Side effects of Amoxicillin: abdominal cramps, back pain, blistering or peeling skin, bloating, bloody urine, blooody nose, chest pain")


def ampicillin():
    print("    Side effects of Ampicillin: nausea, diarrhea, vomiting, abdominal pain, headache")


def cephalosporin():
    print("    Side effects of Cephalosporin: diarrhea, nausea, vomiting, abdominal pain, heartburn, gas, change in taste, headache")


def azithromycin():
    print("    Side effects of Azithromycin: nausea, diarrhea, vomiting, abdominal pain, headache")


def tetracycline():
    print("    Side effects of Tetracycline: nausea, vomiting, diarrhea, itching of the rectum or vagina, swollen tongue, sore throat")


def ribavirin():
    print("    Side effects of Ribavirin: cough, upset stomach, vomiting, diarrhea, constipation, heartburn, loss of appetite, weight loss")


def acyclovir():
    print("    Side effects of Acyclovir: nausea, diarrhea, headache, vomiting, dizziness, drowsiness, kidney problems")


def interferon_alpha():
    print("    Side effects of Interferon Alpha: injection side reactions, headache, fatigue, diarrhea, loss of appetite, back pain, dizziness, nausea, vomiting")


# Lists potention treatments and their side effects based off of the patient's age.
def med_plan_age(age: int, severity: str, pregnancy):

    if (age < 18):
        print("Possible antibiotic treatments for bacterial pneumonia:\n Amoxicillin \n Ampicillin \n Cephalosporin")
        amoxicillin()
        ampicillin()
        cephalosporin()
        print("Possible treatments for viral pneumonia: \n Ribavirin \n Acyclovir")
        ribavirin()
        acyclovir()
        med_plan_severity(severity)
    elif (age >= 18) and (age < 65):
        if (pregnancy == "no"):
            print("Possible antibiotic treatments for bacterial pneumonia:\n Azithromycin \n Tetracycline")
            azithromycin()
            tetracycline()
            print("Possible treatments for viral pneumonia:\n Ribavirin \n Interferon Alpha \n Acyclovir")
            ribavirin()
            interferon_alpha()
            acyclovir()
            med_plan_severity(severity)
        else:
            print("Possible antibiotic treatments for bacterial pneumonia:\n Azithromycin")
            azithromycin()
            print("Possible treatments for viral pneumonia: \n Interferon Alpha")
            interferon_alpha()
            med_plan_severity(severity)
    else:
        print("Possible antibiotic treatments for bacterial pneumonia:\n Charithromycin \n Tetracycline")
        cephalosporin()
        tetracycline()
        print("Possible treatments for viral pneumonia: \n Ribavirin")
        ribavirin()
        med_plan_severity(severity)


main()