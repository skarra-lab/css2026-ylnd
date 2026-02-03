# -*- coding: utf-8 -*-
"""
Created on Tue Feb 2 28 10:40:23 2026

@author: Yolanda
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="YOLANDA TSENGWA | Chemistry (Energy & Nanomaterials)",
    page_icon="🧪",
    layout="wide"
)

# Sidebar
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Home", "Energy storage & Energy generation", "Biochar-Fuel Cell Research", "Materials synthesis (hydrothermal treatment, chemical activation, impregnation methods)", "4597917@myuwc.ac.za"]
)

# Header
st.title("YOLANDA TSENGWA")
st.subheader("DEVELOPMENT OF LOW-COST HIERARCHICAL BIOCHAR AS A SUPPORT CATALYST FOR DIRECT METHANOL FUEL CELL") 
st.markdown("---")

# Home section
if section == "Home":

        st.markdown(
            "I am a researcher with interests in Biomass-derived carbon materials, "
            " Title: Development of Low-Cost Hierarchical Biochar Derived from Bagasse as Support for PEM Fuel Cells "
            "The Research focuses on the synthesis and modification of biochar derived from agricultural waste to producr a hierarchical, high-surface-area carbon support suitable for"
            "DM fuel cell catalysts. It aims at reducing the reliance on expensive platinum-based material" )

# Research Interests section
elif section == "Biomass-derived carbon materials, Sustainable and green energy technologies":
    st.header("Biomass-derived carbon materials, Sustainable and green energy technologies")
    st.markdown(
        "The Research focuses on the synthesis and modification of biochar derived from agricultural waste to producr a hierarchical, high-surface-area carbon support suitable for" 
        "DM fuel cell catalysts. It aims at reducing the reliance on expensive platinum-based material.")

# Projects section
elif section == "Low-cost electrocatalyst supports for fuel cell applications":
    st.header("Electrochemical characterization and materials performance evaluation")

    st.write(
        "DEVELOPMENT OF LOW-COST HIERARCHICAL BIOCHAR AS A SUPPORT CATALYST FOR DIRECT METHANOL FUEL CEL."
    )

    st.markdown("Energy nanomaterials & Electrovhemistry ."
)
    st.write(
        "The Research focuses on the synthesis and modification of biochar derived from agricultural waste to producr a hierarchical, high-surface-area carbon support suitable for" 
        "DM fuel cell catalysts. It aims at reducing the reliance on expensive platinum-based material ." )

    st.markdown("The Research focuses on the synthesis and modification of biochar derived from agricultural waste to producr a hierarchical, high-surface-area carbon support suitable for")
    "DM fuel cell catalysts. It aims at reducing the reliance on expensive platinum-based material ."

    st.write(
        "Use of Python-based tools for processing and visualizing electrochemical data."
    )

# Skills & Tools section
elif section == "Electrochemical analysis, Materials Synthesis, Structural & Surface Characterization, Data Analysis & Scientific Writing":
    st.header("Electrochemical analysis, Materials Synthesis, Structural & Surface Characterization, Data Analysis & Scientific Writing")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("Chemical, and Thermal Activation of biochar derived from Sweet Sorghum biomass"
                    "Development of  supported bimetallic electrocatalyst"
                    "Characterise the prepared electrocatalyst using characterization techniques such as SEM, FTIR, RAMAN, TGA, XRD, TEM & BET")
    st.markdown("Electrochemical analysis, Materials Synthesis, Structural & Surface Characterization, Data Analysis & Scientific Writing" )


# Contact section
elif section == "4597917@myuwc.ac.za":
    st.header("4597917@myuwc.ac.za")
    st.markdown(
        "📧 **Email**: 4597917@myuwc.ac.za  \n"
        "🔗 **https://github.com/ID-lang/RO-ccsCHPC / https://scholar.google.YOUR GOOGLE SCHOLAR / LinkedIn YOURS*NA*"
    )

    st.info("This Streamlit app is hosted on Streamlit Cloud as a public research profile page.")
