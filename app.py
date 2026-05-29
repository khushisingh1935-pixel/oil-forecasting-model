import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from PIL import Image

# PAGE CONFIG
st.set_page_config(
    page_title="Global Oil Forecast Dashboard",
    layout="wide"
)

# TITLE
st.title("Global Oil Production Forecasting Dashboard")

st.markdown("""
Machine Learning based forecasting system for global oil production analysis and future prediction.
""")

# LOAD DATA
future_df = pd.read_csv(
    "future_oil_forecast_2026_2031.csv"
)

future_df['date'] = pd.to_datetime(
    future_df['date']
)

# METRICS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Forecast Period",
        "2026-2031"
    )

with col2:
    st.metric(
        "Forecast Months",
        len(future_df)
    )

with col3:
    st.metric(
        "Model",
        "XGBoost"
    )

# TABS
tab1, tab2, tab3, tab4 = st.tabs([
    "Forecast",
    "Actual vs Predicted",
    "Feature Importance",
    "Residual Analysis"
])

# TAB 1
with tab1:

    st.subheader(
        "Future Oil Production Forecast"
    )

    fig, ax = plt.subplots(
        figsize=(12, 5)
    )

    ax.plot(
        future_df['date'],
        future_df['forecasted_production'],
        linewidth=3
    )

    ax.set_title(
        "Forecasted Oil Production (2026-2031)"
    )

    ax.set_xlabel("Year")

    ax.set_ylabel("Production")

    ax.grid(True)

    ax.xaxis.set_major_locator(
        mdates.YearLocator()
    )

    ax.xaxis.set_major_formatter(
        mdates.DateFormatter('%Y')
    )

    plt.xticks(rotation=45)

    st.pyplot(fig)

    st.subheader(
        "Forecast Dataset"
    )

    st.dataframe(
        future_df,
        use_container_width=True
    )

# TAB 2
with tab2:

    st.subheader(
        "Actual vs Predicted Production"
    )

    st.image(
        "01_actual_vs_predicted.png",
        use_container_width=True
    )

# TAB 3
with tab3:

    st.subheader(
        "Feature Importance"
    )

    st.image(
        "02_feature_importance.png",
        use_container_width=True
    )

# TAB 4
with tab4:

    st.subheader(
        "Residual Analysis"
    )

    st.image(
        "03_residual_analysis.png",
        use_container_width=True
    )

# DOWNLOAD BUTTON
st.download_button(
    label="Download Forecast CSV",
    data=future_df.to_csv(index=False),
    file_name="future_oil_forecast_2026_2031.csv",
    mime="text/csv"
)