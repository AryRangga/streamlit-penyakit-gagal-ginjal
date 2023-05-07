import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('penyakit_gagal_ginjal.sav', 'rb'))

st.title('Prediksi Penyakit Gagal Ginjal')

col1, col2, col3 = st.columns(3)
with col1:blood_pressure = st.number_input('Input Tekanan Darah')
with col2:sg = st.number_input('Input Berat Badan')
with col3:albumin = st.number_input('Input Albumin (Protein Pada Darah)')
with col1:sugar = st.number_input('Input Gula')
with col2:red_blood_cell = st.number_input('Input Sel darah merah')
with col3:blood_urea = st.number_input('Input Blood Urea (zat sisa protein dan asam amino)')
with col1:serum_creatinine = st.number_input('Input Kreatinin serum')
with col2:sodium = st.number_input('Input Sodium')
with col3:pottasium = st.number_input('Input Pottasium')
with col1:hemoglobin = st.number_input('Input Hemoglobin')
with col2:white_blood_cell = st.number_input('Input Sel Darah Putih')
with col3:red_blood_cell_count = st.number_input('Input Jumlah Sel Darah Merah')
with col1:hypertension = st.number_input('Input Hipertensi')    
    
predict = ''

if st.button('Prediksi Penyakit Gagal Ginjal'):
    predict = model.predict([[blood_pressure,sg,albumin,sugar,red_blood_cell,blood_urea,serum_creatinine,sodium,pottasium,hemoglobin,white_blood_cell,red_blood_cell_count,hypertension]])
    
    if(predict[0]==0):
        predict = 'Seorang Tidak Mengidap Gagal Ginjal'
    else :
        predict = 'Seorang Mengidap Gagal Ginjal'
st.success(predict)
