 # save this as app.py
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':

        gender = request.form['gender']
        marriedr = request.form['marriedr']
        m_identification = request.form['m_identification']
        email_address = request.form['email_address']
        type_of_loan = request.form['type_of_loan']
        employment_years_pr = request.form['employment_years_pr']
        occupation_type = request.form['occupation_type']
        own_car = request.form['own_car']
        own_house = request.form['own_house']
        edu_qualification = request.form['edu_qualification']
        accomodation_type = request.form['accomodation_type']
        apartment_type = request.form['apartment_type']
        living_region_condi = request.form['living_region_condi']
        dstv_recharge = request.form['dstv_recharge']
        nepa_lastday_pay = request.form['nepa_lastday_pay']
        phone_last_pay = request.form['phone_last_pay']


        house_type = request.form['house_type']
        employment_type = request.form['employment_type']





        BVN = float(request.form['BVN'])
        MONTHLY_INCOME_TOTAL = float(request.form['MONTHLY_INCOME_TOTAL'])
        LOAN_AMOUNT = float(request.form['LOAN_AMOUNT'])
        OUTSTANDING_LOAN_BALANCE = float(request.form['OUTSTANDING_LOAN_BALANCE'])
        COUNT_OF_CHILDREN = float(request.form['COUNT_OF_CHILDREN'])
        YEAR_OF_BIRTH = float(request.form['YEAR_OF_BIRTH'])









         #gender
        if (gender == "male"):
             gender_male=1
        else:
             gender_male=0



        # married
        if(marriedr=='single'):
            Married_1 = 1
            Married_2 = 0
            Married_3 = 0


        elif(marriedr == 'married'):
            Married_1 = 0
            Married_2 = 1
            Married_3 = 0

        elif(marriedr=="widowed"):
            Married_1 = 0
            Married_2 = 0
            Married_3 = 1
        else:
            Married_1 = 0
            Married_2 = 0
            Married_3 = 0


        # m_identification
        if(m_identification=='National ID Card'):
            m_identification_1 = 1
            m_identification_2 = 0
            m_identification_3 = 0
            m_identification_4 = 0


        elif(m_identification == 'National Driver’s Licence'):
            m_identification_1 = 0
            m_identification_2 = 1
            m_identification_3 = 0
            m_identification_4 = 0

        elif(m_identification=="Valid INEC Voter’s Card"):
            m_identification_1 = 0
            m_identification_2 = 0
            m_identification_3 = 1
            m_identification_4 = 0

        elif(m_identification=="NIN"):
            m_identification_1 = 0
            m_identification_2 = 0
            m_identification_3 = 0
            m_identification_4 = 1
        else:
            m_identification_1 = 0
            m_identification_2 = 0
            m_identification_3 = 0
            m_identification_4 = 0


        # email_address
        if (email_address == "yes"):
            email_1=1
        else:
            email_1=0


        # type_of_loan
        if(type_of_loan=='personal home loan'):
            type_of_loan_1 = 1
            type_of_loan_2 = 0
            type_of_loan_3 = 0
            type_of_loan_4 = 0

        elif(type_of_loan=="joint mortgage"):
            type_of_loan_1 = 0
            type_of_loan_2 = 1
            type_of_loan_3 = 0
            type_of_loan_4 = 0


        elif(type_of_loan=="salary loan"):
            type_of_loan_1 = 0
            type_of_loan_2 = 0
            type_of_loan_3 = 1
            type_of_loan_4 = 0

        elif(type_of_loan=="secured overdraft"):
            type_of_loan_1 = 0
            type_of_loan_2 = 0
            type_of_loan_3 = 0
            type_of_loan_4 = 1

        else:
            type_of_loan_1 = 0
            type_of_loan_2 = 0
            type_of_loan_3 = 0
            type_of_loan_4 = 0



       #employment_years_pr

        if(employment_years_pr=='two years'):
            employment_years_pr_1 = 1
            employment_years_pr_2 = 0
            employment_years_pr_3 = 0
            employment_years_pr_4 = 0
            employment_years_pr_5 = 0
            employment_years_pr_6 = 0
            employment_years_pr_7 = 0
            employment_years_pr_8 = 0
            employment_years_pr_9 = 0

        elif(employment_years_pr=="three years"):
            employment_years_pr_1 = 0
            employment_years_pr_2 = 1
            employment_years_pr_3 = 0
            employment_years_pr_4 = 0
            employment_years_pr_5 = 0
            employment_years_pr_6 = 0
            employment_years_pr_7 = 0
            employment_years_pr_8 = 0
            employment_years_pr_9 = 0
        elif(employment_years_pr=="less than one year"):
            employment_years_pr_1 = 0
            employment_years_pr_2 = 0
            employment_years_pr_3 = 1
            employment_years_pr_4 = 0
            employment_years_pr_5 = 0
            employment_years_pr_6 = 0
            employment_years_pr_7 = 0
            employment_years_pr_8 = 0
            employment_years_pr_9 = 0
        elif(employment_years_pr=="five years"):
            employment_years_pr_1 = 0
            employment_years_pr_2 = 0
            employment_years_pr_3 = 0
            employment_years_pr_4 = 1
            employment_years_pr_5 = 0
            employment_years_pr_6 = 0
            employment_years_pr_7 = 0
            employment_years_pr_8 = 0
            employment_years_pr_9 = 0
        elif(employment_years_pr=="four years"):
            employment_years_pr_1 = 0
            employment_years_pr_2 = 0
            employment_years_pr_3 = 0
            employment_years_pr_4 = 0
            employment_years_pr_5 = 1
            employment_years_pr_6 = 0
            employment_years_pr_7 = 0
            employment_years_pr_8 = 0
            employment_years_pr_9 = 0
        elif(employment_years_pr=="six years"):
            employment_years_pr_1 = 0
            employment_years_pr_2 = 0
            employment_years_pr_3 = 0
            employment_years_pr_4 = 0
            employment_years_pr_5 = 0
            employment_years_pr_6 = 1
            employment_years_pr_7 = 0
            employment_years_pr_8 = 0
            employment_years_pr_9 = 0
        elif(employment_years_pr=="seven years"):
            employment_years_pr_1 = 0
            employment_years_pr_2 = 0
            employment_years_pr_3 = 0
            employment_years_pr_4 = 0
            employment_years_pr_5 = 0
            employment_years_pr_6 = 0
            employment_years_pr_7 = 1
            employment_years_pr_8 = 0
            employment_years_pr_9 = 0
        elif(employment_years_pr=="eight years"):
            employment_years_pr_1 = 0
            employment_years_pr_2 = 0
            employment_years_pr_3 = 0
            employment_years_pr_4 = 0
            employment_years_pr_5 = 0
            employment_years_pr_6 = 0
            employment_years_pr_7 = 0
            employment_years_pr_8 = 1
            employment_years_pr_9 = 0
        elif(employment_years_pr=="nine years"):
            employment_years_pr_1 = 0
            employment_years_pr_2 = 0
            employment_years_pr_3 = 0
            employment_years_pr_4 = 0
            employment_years_pr_5 = 0
            employment_years_pr_6 = 0
            employment_years_pr_7 = 0
            employment_years_pr_8 = 0
            employment_years_pr_9 = 1

        else:
            employment_years_pr_1 = 0
            employment_years_pr_2 = 0
            employment_years_pr_3 = 0
            employment_years_pr_4 = 0
            employment_years_pr_5 = 0
            employment_years_pr_6 = 0
            employment_years_pr_7 = 0
            employment_years_pr_8 = 0
            employment_years_pr_9 = 0






#occupation_type

        if(occupation_type=='Laborer'):
            occupation_type_1 = 1
            occupation_type_2 = 0
            occupation_type_3 = 0
        elif(occupation_type=="teacher"):
            occupation_type_1 = 0
            occupation_type_2 = 1
            occupation_type_3 = 0
        elif(occupation_type=="Driver"):
            occupation_type_1 = 0
            occupation_type_2 = 0
            occupation_type_3 = 1
        else:
            occupation_type_1 = 0
            occupation_type_2 = 0
            occupation_type_3 = 0




            #own_car

        if (own_car=="yes"):
            own_car_1=1
        else:
            own_car_1=0

            #own_house
        if (own_house=="yes"):
            own_house_1=1
        else:
            own_house_1=0

#edu_qualification

        if(edu_qualification=='Graduate'):
            edu_qualification_1 = 1
            edu_qualification_2 = 0
            edu_qualification_3 = 0
            edu_qualification_4 = 0
            edu_qualification_5 = 0


        elif(edu_qualification == 'Post Graduate'):
            edu_qualification_1 = 0
            edu_qualification_2 = 1
            edu_qualification_3 = 0
            edu_qualification_4 = 0
            edu_qualification_5 = 0


        elif(edu_qualification == 'Professional'):
            edu_qualification_1 = 0
            edu_qualification_2 = 0
            edu_qualification_3 = 1
            edu_qualification_4 = 0
            edu_qualification_5 = 0

        elif(edu_qualification == 'Primary School Leaving Certificate'):
            edu_qualification_1 = 0
            edu_qualification_2 = 0
            edu_qualification_3 = 0
            edu_qualification_4 = 1
            edu_qualification_5 = 0

        elif(edu_qualification == 'Secondary School'):
            edu_qualification_1 = 0
            edu_qualification_2 = 0
            edu_qualification_3 = 0
            edu_qualification_4 = 0
            edu_qualification_5 = 1

        else:
            edu_qualification_1 = 0
            edu_qualification_2 = 0
            edu_qualification_3 = 0
            edu_qualification_4 = 0
            edu_qualification_5 = 0

#accomodation_type
        if(accomodation_type=='Rented'):
            accomodation_type_1 = 1
            accomodation_type_2 = 0
            accomodation_type_3 = 0

        elif(accomodation_type == 'owned'):
            accomodation_type_1 = 0
            accomodation_type_2 = 1
            accomodation_type_3 = 0

        elif(accomodation_type == 'Official Quarters'):
            accomodation_type_1 = 0
            accomodation_type_2 = 0
            accomodation_type_3 = 1
        else:
            accomodation_type_1 = 0
            accomodation_type_2 = 0
            accomodation_type_3 = 0


#apartment_type

        if(apartment_type=='two rooms'):
            apartment_type_1 = 1
            apartment_type_2 = 0
            apartment_type_3 = 0
            apartment_type_4 = 0
            apartment_type_5 = 0

        elif(apartment_type == 'one room'):
            apartment_type_1 = 0
            apartment_type_2 = 1
            apartment_type_3 = 0
            apartment_type_4 = 0
            apartment_type_5 = 0

        elif(apartment_type == 'three rooms'):
            apartment_type_1 = 0
            apartment_type_2 = 0
            apartment_type_3 = 1
            apartment_type_4 = 0
            apartment_type_5 = 0

        elif(apartment_type == 'four rooms'):
            apartment_type_1 = 0
            apartment_type_2 = 0
            apartment_type_3 = 0
            apartment_type_4 = 1
            apartment_type_5 = 0

        elif(apartment_type == 'five rooms'):
            apartment_type_1 = 0
            apartment_type_2 = 0
            apartment_type_3 = 0
            apartment_type_4 = 0
            apartment_type_5 = 1

        else:
            apartment_type_1 = 0
            apartment_type_2 = 0
            apartment_type_3 = 0
            apartment_type_4 = 0
            apartment_type_5 = 0




            #living_region_condi
        if(living_region_condi=='very good'):
            living_region_condi_1 = 1
            living_region_condi_2 = 0
            living_region_condi_3 = 0

        elif(living_region_condi == 'good'):
            living_region_condi_1 = 0
            living_region_condi_2 = 1
            living_region_condi_3 = 0

        elif(living_region_condi == 'very bad'):
            living_region_condi_1 = 0
            living_region_condi_2 = 0
            living_region_condi_3 = 1
        else:
            living_region_condi_1 = 0
            living_region_condi_2 = 0
            living_region_condi_3 = 0

            #dstv_recharge
        if(dstv_recharge=='less than three weeks ago'):
            dstv_recharge_1 = 1
            dstv_recharge_2 = 0
            dstv_recharge_3 = 0
            dstv_recharge_4 = 0
            dstv_recharge_5 = 0



        elif(dstv_recharge == 'two months ago'):
            dstv_recharge_1 = 0
            dstv_recharge_2 = 1
            dstv_recharge_3 = 0
            dstv_recharge_4 = 0
            dstv_recharge_5 = 0

        elif(dstv_recharge == 'three months ago'):
            dstv_recharge_1 = 0
            dstv_recharge_2 = 0
            dstv_recharge_3 = 1
            dstv_recharge_4 = 0
            dstv_recharge_5 = 0

        elif(dstv_recharge == 'less than six months'):
            dstv_recharge_1 = 0
            dstv_recharge_2 = 0
            dstv_recharge_3 = 0
            dstv_recharge_4 = 1
            dstv_recharge_5 = 0

        elif(dstv_recharge == 'a year ago'):
            dstv_recharge_1 = 0
            dstv_recharge_2 = 0
            dstv_recharge_3 = 0
            dstv_recharge_4 = 0
            dstv_recharge_5 = 1

        else:
            dstv_recharge_1 = 0
            dstv_recharge_2 = 0
            dstv_recharge_3 = 0
            dstv_recharge_4 = 0
            dstv_recharge_5 = 0



        #nepa_lastday_pay

        if(nepa_lastday_pay=='a year ago'):
            nepa_lastday_pay_1 = 1
            nepa_lastday_pay_2 = 0
            nepa_lastday_pay_3 = 0
            nepa_lastday_pay_4 = 0
            nepa_lastday_pay_5 = 0

        elif(nepa_lastday_pay == 'less than six months'):
            nepa_lastday_pay_1 = 0
            nepa_lastday_pay_2 = 1
            nepa_lastday_pay_3 = 0
            nepa_lastday_pay_4 = 0
            nepa_lastday_pay_5 = 0

        elif(nepa_lastday_pay == 'less than three weeks ago'):
            nepa_lastday_pay_1 = 0
            nepa_lastday_pay_2 = 0
            nepa_lastday_pay_3 = 1
            nepa_lastday_pay_4 = 0
            nepa_lastday_pay_5 = 0

        elif(nepa_lastday_pay == 'three months ago'):
            nepa_lastday_pay_1 = 0
            nepa_lastday_pay_2 = 0
            nepa_lastday_pay_3 = 0
            nepa_lastday_pay_4 = 1
            nepa_lastday_pay_5 = 0

        elif(nepa_lastday_pay == 'two months ago'):
            nepa_lastday_pay_1 = 0
            nepa_lastday_pay_2 = 0
            nepa_lastday_pay_3 = 0
            nepa_lastday_pay_4 = 0
            nepa_lastday_pay_5 = 1


        else:
            nepa_lastday_pay_1 = 0
            nepa_lastday_pay_2 = 0
            nepa_lastday_pay_3 = 0
            nepa_lastday_pay_4 = 0
            nepa_lastday_pay_5 = 0








    #phone_last_pay

        if(phone_last_pay=='a year ago'):
            phone_last_pay_1 = 1
            phone_last_pay_2 = 0
            phone_last_pay_3 = 0
            phone_last_pay_4 = 0
            phone_last_pay_5 = 0


        elif(phone_last_pay == 'less than six months'):
            phone_last_pay_1 = 0
            phone_last_pay_2 = 1
            phone_last_pay_3 = 0
            phone_last_pay_4 = 0
            phone_last_pay_5 = 0

        elif(phone_last_pay == 'less than three weeks ago'):
            phone_last_pay_1 = 0
            phone_last_pay_2 = 0
            phone_last_pay_3 = 1
            phone_last_pay_4 = 0
            phone_last_pay_5 = 0

        elif(phone_last_pay == 'three months ago'):
            phone_last_pay_1 = 0
            phone_last_pay_2 = 0
            phone_last_pay_3 = 0
            phone_last_pay_4 = 1
            phone_last_pay_5 = 0
        elif(phone_last_pay == 'two months ago'):
            phone_last_pay_1 = 0
            phone_last_pay_2 = 0
            phone_last_pay_3 = 0
            phone_last_pay_4 = 0
            phone_last_pay_5 = 1

        else:
            phone_last_pay_1 = 0
            phone_last_pay_2 = 0
            phone_last_pay_3 = 0
            phone_last_pay_4 = 0
            phone_last_pay_5 = 0



#house_type

        if(house_type=='Detached'):
            house_type_1 = 1
            house_type_2 = 0
            house_type_3 = 0
            house_type_4 = 0
            house_type_5 = 0
            house_type_6 = 0
            house_type_7 = 0
            house_type_8 = 0

        elif(house_type == 'Duplex'):
            house_type_1 = 0
            house_type_2 = 1
            house_type_3 = 0
            house_type_4 = 0
            house_type_5 = 0
            house_type_6 = 0
            house_type_7 = 0
            house_type_8 = 0

        elif(house_type == 'Mansion'):
            house_type_1 = 0
            house_type_2 = 0
            house_type_3 = 1
            house_type_4 = 0
            house_type_5 = 0
            house_type_6 = 0
            house_type_7 = 0
            house_type_8 = 0

        elif(house_type == 'Penthouse'):
            house_type_1 = 0
            house_type_2 = 0
            house_type_3 = 0
            house_type_4 = 1
            house_type_5 = 0
            house_type_6 = 0
            house_type_7 = 0
            house_type_8 = 0

        elif(house_type == 'Semi-detached'):
            house_type_1 = 0
            house_type_2 = 0
            house_type_3 = 0
            house_type_4 = 0
            house_type_5 = 1
            house_type_6 = 0
            house_type_7 = 0
            house_type_8 = 0


        elif(house_type == 'Terraced'):
            house_type_1 = 0
            house_type_2 = 0
            house_type_3 = 0
            house_type_4 = 0
            house_type_5 = 0
            house_type_6 = 1
            house_type_7 = 0
            house_type_8 = 0

        elif(house_type == 'block of flats'):
            house_type_1 = 0
            house_type_2 = 0
            house_type_3 = 0
            house_type_4 = 0
            house_type_5 = 0
            house_type_6 = 0
            house_type_7 = 1
            house_type_8 = 0
        elif(house_type == 'face-me i face-you'):
            house_type_1 = 0
            house_type_2 = 0
            house_type_3 = 0
            house_type_4 = 0
            house_type_5 = 0
            house_type_6 = 0
            house_type_7 = 0
            house_type_8 = 1

        else:
            house_type_1 = 0
            house_type_2 = 0
            house_type_3 = 0
            house_type_4 = 0
            house_type_5 = 0
            house_type_6 = 0
            house_type_7 = 0
            house_type_8 = 0



#employment_type

        if (employment_type == "permanet"):
             employment_type_1=1
        else:
             employment_type_1=0





        BVN = np.log(BVN)
        MONTHLY_INCOME_TOTAL = np.log(MONTHLY_INCOME_TOTAL)
        LOAN_AMOUNT = np.log(LOAN_AMOUNT)
        OUTSTANDING_LOAN_BALANCE = np.log(OUTSTANDING_LOAN_BALANCE)
        COUNT_OF_CHILDREN = np.log(COUNT_OF_CHILDREN)
        YEAR_OF_BIRTH = np.log(YEAR_OF_BIRTH)





        prediction = model.predict([[ gender_male, Married_1, Married_2, Married_3, m_identification_1, m_identification_2,
                               m_identification_3, m_identification_4, email_1, type_of_loan_1, type_of_loan_2,
                               type_of_loan_3, type_of_loan_4, employment_years_pr_1, employment_years_pr_2, employment_years_pr_3,
                               employment_years_pr_4, employment_years_pr_5, employment_years_pr_6, employment_years_pr_7,
                               employment_years_pr_8, employment_years_pr_9, occupation_type_1, occupation_type_2,
                               occupation_type_3, own_car_1, own_house_1, edu_qualification_1, edu_qualification_2,
                               edu_qualification_3, edu_qualification_4, edu_qualification_5, accomodation_type_1,
                               accomodation_type_2, accomodation_type_3, apartment_type_1, apartment_type_2, apartment_type_3,
                               apartment_type_4, apartment_type_5, living_region_condi_1, living_region_condi_2,
                               living_region_condi_3, dstv_recharge_1, dstv_recharge_2, dstv_recharge_3, dstv_recharge_4,
                               dstv_recharge_5, nepa_lastday_pay_1, nepa_lastday_pay_2, nepa_lastday_pay_3, nepa_lastday_pay_4,
                               nepa_lastday_pay_5,  phone_last_pay_1, phone_last_pay_2, phone_last_pay_3,
                               phone_last_pay_4, phone_last_pay_5, house_type_1, house_type_2, house_type_3, house_type_4, house_type_5,
                               house_type_6, house_type_7, house_type_8,  employment_type_1,
                               BVN, MONTHLY_INCOME_TOTAL, LOAN_AMOUNT, OUTSTANDING_LOAN_BALANCE, COUNT_OF_CHILDREN,
                                YEAR_OF_BIRTH]])

        # print(prediction)

        if prediction==1:
            prediction=" <  CONGRATS! your loan will be granted  >"
        else:
            prediction=" <  SORRY! your loan can't be granted   >"




        return render_template("prediction.html", prediction_text="{}".format(prediction))



    else:
        return render_template("prediction.html")



if __name__ == "__main__":
    app.run(debug=True)
