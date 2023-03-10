import pandas
import seaborn
import streamlit

from plotly import express

seaborn.set()


@streamlit.cache_data
def load_data():
    data_frame = pandas.read_csv("./data/etapa1_full.csv", sep=";")

    return data_frame


def get_count_plot(data_frame, column):
    value = data_frame.groupby(column)["IS_CHURN"].mean()
    figure = express.bar(value/100, color=value.index, width=500, height=500)
    figure.update_layout(xaxis_title=column, yaxis_title="Churn Rate")

    return figure


def get_pie_chart(data_frame, column):
    value = data_frame[column].value_counts(normalize=True)
    figure = express.pie(values=value.values, names=value.index, height=450, width=450)
    # fig.update_layout(xaxis_title=column, yaxis_title="Percentage")

    return figure


def get_histogram(data_frame, column, set_hue=None):
    figure = express.histogram(data_frame, x=column)

    return figure


def show_plots(data_frame, features):
    data_frame = load_data()
    churn_data = data_frame[data_frame["IS_CHURN"] == 1]
    retained_data = data_frame[data_frame["IS_CHURN"] == 0]
    feature = streamlit.selectbox("**Choose Feature**", tuple(features))

    # ==============================================================
    # Churn radio button
    churn = streamlit.radio("**Show Plot for**: ", ("All", "Churn", "Retained"))

    if churn == "Churn":
        count_plot = get_count_plot(churn_data, feature)
        pie_chart = get_pie_chart(churn_data, feature)
    elif churn == "Retained":
        count_plot = get_count_plot(retained_data, feature)
        pie_chart = get_pie_chart(retained_data, feature)
    else:
        count_plot = get_count_plot(data_frame, feature)
        pie_chart = get_pie_chart(data_frame, feature)

    # End of radio button

    # Plot type radio button
    plot_type = streamlit.radio("**Show Plot as**: ", ("Pie", "Bar"))

    if plot_type == "Bar":
        streamlit.plotly_chart(count_plot)
    else:
        streamlit.plotly_chart(pie_chart)

    # End of radio button
    # ===============================================================
