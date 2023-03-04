import streamlit

streamlit.title("Data Avengers | No matter how your day starts, find time to make it gr8!")
streamlit.image("./images/customer-churn.png", caption="Let the Butter Churn, Not Your Customers!",
                use_column_width=True)

dataset = "View the data set here: [Dataset](https://drive.google.com/drive/folders/1i6MS6Q-11BQlKyc5s_VReyGauCOMKOzY)"

streamlit.write("**You Can Also:** ")
streamlit.markdown(dataset, unsafe_allow_html=True)

# =====================Conclusion=======================

streamlit.markdown("## Conclusion")

# Create a bullet list
streamlit.write("##### Based on user demographics:")
streamlit.write("- Gender has no effect on Churn Rate .")
streamlit.write("- Seniors are more probable to churn with a churn rate of 0.42 while 0.23 for non seniors.")
streamlit.write("- Customers that don't have partners are more likely to churn with a rate of 0.33.")
streamlit.write("- Customers that don't have dependents are more likely to churn with a rate of 0.32.")

streamlit.write("##### Based on Customr Account info:")
streamlit.write("- Customers With Month to Month contract are more likely to churn with a churn rate of 0.42.")
streamlit.write("- Customers that prefer Paperless Billing are more likely to churn 0.33.")
streamlit.write("- Customers that pay with Electronic Check have a high churn rate 0.44")
streamlit.write("- The longer the customer stay with the corporation the less the churn rate (low: 0.41).")
streamlit.write("- The higher the charges the higher the churn rate (high: 0.34).")

streamlit.write("##### In term of Services:")
streamlit.write("- Customers using Fiber Optic Have a high churn rate (0.42).")
streamlit.write("- Customers Using the rest of the services have low churn rates compared to customers who don't.")