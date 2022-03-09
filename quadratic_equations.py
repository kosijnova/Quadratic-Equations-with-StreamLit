def donothing():
    return

def sqrtf(a,b,c):
     
    if a<0:
        q = str(a)
    else:
        q = str(a)
        
    if b<0:
        w = str(b)
    else:
        w = '+'+str(b)
        
    if c<0:
        e = str(c)
    else:
        e = '+'+str(c)
    #print('FUNKCJA KWADRATOWA:\n',q+'x²'+w+'x'+e)
    delta = (b**2)-(4*a*c)
    
    if a==0 and b==0 and c==0:
        donothing()
    else:
        st.write('Δ = ',delta)
        
    if delta > 0:
        try:
            x1 = round((-b-(m.sqrt(delta)))/(2*a),2)
            x2 = round((-b+(m.sqrt(delta)))/(2*a),2)
            x = np.arange(x1-3,x2+3,0.5)
            y = a*x**2+b*x+c
            data = pd.DataFrame({'x':x,
                                 'y':y})
        except ZeroDivisionError:
            st.write("ZeroDivisionError: Popraw wartości!")
        except ValueError:
            st.write("ValueError: Popraw wartości!")
        else:
            st.write('\n√Δ = ',round(m.sqrt(delta),2),'\nx1 = ',x1,'\nx2 = ',x2)
            chart = alt.Chart(data).mark_line().encode(
                alt.X('x'),
                alt.Y('y')).properties(title='Parabola')
            chart1 = alt.Chart(pd.DataFrame({'x':[0]})).mark_rule().encode(x='x',color=alt.value("#0a0a0a"))
            chart2 = alt.Chart(pd.DataFrame({'y':[0]})).mark_rule().encode(y='y',color=alt.value("#0a0a0a"))
            st.altair_chart(chart+chart1+chart2)
    elif delta == 0:
        try:
            x0 = round(-b/(2*a),2)
            x = np.arange(x0-3,x0+3,0.5)
            y = a*x**2+b*x+c
            data = pd.DataFrame({'x':x,
                                 'y':y})
        except ZeroDivisionError:
            st.write("ZerDivisionError: Popraw wartości!")
        except ValueError:
            st.write("ValueError: Popraw wartości!")
        else:
            st.write('\nx0 = ',x0)
            chart = alt.Chart(data).mark_line().encode(
                alt.X('x'),
                alt.Y('y')).properties(title='Parabola')
            chart1 = alt.Chart(pd.DataFrame({'x':[0]})).mark_rule().encode(x='x',color=alt.value("#0a0a0a"))
            chart2 = alt.Chart(pd.DataFrame({'y':[0]})).mark_rule().encode(y='y',color=alt.value("#0a0a0a"))
            st.altair_chart(chart+chart1+chart2)
    else:
        st.write('brak miejsc zerowych')
        
    
if __name__=='__main__':
    import numpy as np
    import pandas as pd
    from matplotlib import pyplot as plt
    import math as m
    import streamlit as st
    import altair as alt
    
    st.title('RÓWNANIA KWADRATOWE')
    col1,col2 = st.columns(2) 
    with col1:
        a = st.number_input("Współczynnik kwadratowy: ")
        b = st.number_input("Współczynnik liniowy: ")
        c = st.number_input("Wyraz wolny: ")
    with col2:
        sqrtf(a,b,c)
