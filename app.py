import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# PAGE CONFIG
st.set_page_config(
    page_title="Oil Forecast Dashboard",
    layout="wide"
)

# TITLE
st.title("Global Oil Production Forecasting Dashboard")

st.markdown("""
Machine Learning based forecasting system for
global oil production analysis and future prediction.
""")

# LOAD FORECAST CSV
future_df = pd.read_csv(
    "future_oil_forecast_2026_2031.csv"
)

# METRICS
col1, col2, col3 = st.columns(3)

col1.metric(
    "Forecast Years",
    "2026-2031"
)

col2.metric(
    "Total Forecast Months",
    len(future_df)
)

col3.metric(
    "Model",
    "XGBoost"
)

# TABS
tab1, tab2, tab3, tab4 = st.tabs([
    "Forecast Data",
    "Actual vs Predicted",
    "Feature Importance",
    "Residual Analysis"
])

# TAB 1
with tab1:

    st.subheader("Forecast Dataset")

    st.dataframe(future_df)

    fig, ax = plt.subplots(figsize=(12,6))

    ax.plot(
        future_df['date'],
        future_df['forecasted_production'],
        linewidth=3
    )

    ax.set_title(
        "Forecasted Oil Production (2026-2031)"
    )

    ax.set_xlabel("Date")

    ax.set_ylabel("Production")

    ax.grid(True)

    st.pyplot(fig)

# TAB 2
with tab2:

    st.subheader(
        "Actual vs Predicted Production"
    )

    image1 = Image.open(
        "01_actual_vs_predicted.png"
    )

    st.image(
        image1,
        use_container_width=True
    )

# TAB 3
with tab3:

    st.subheader(
        "Feature Importance"
    )

    image2 = Image.open(
        "02_feature_importance.png"
    )

    st.image(
        image2,
        use_container_width=True
    )

# TAB 4
with tab4:

    st.subheader(
        "Residual Analysis"
    )

    image3 = Image.open(
        "03_residual_analysis.png"
    )

    st.image(
        image3,
        use_container_width=True
    )

# DOWNLOAD BUTTON
csv = future_df.to_csv(index=False)

st.download_button(
    label="Download Forecast CSV",
    data=csv,
    file_name="future_forecast.csv",
    mime="text/csv"
) 