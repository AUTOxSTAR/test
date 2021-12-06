import streamlit as st

def BMI(w,h):
    return w/(h*h)

#w = float(input('請輸入體重(KG)?'))
w = st.number_input('請輸入體重(KG)？')
h = st.number_input('請輸入身高(M)？')
st.button('請輸入確認')

bmi = BMI(w, h)
#print('BMI為', bmi)
st.write('BMI為')
if (bmi < 18):
    print('體重過輕')
elif (bmi < 24):
    print('體重正常')
elif (bmi < 27):
    print('體重過重')
else:
    print('體重肥胖')
