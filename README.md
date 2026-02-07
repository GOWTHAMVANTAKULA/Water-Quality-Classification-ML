# Water-Quality-Classification-ML
This project uses machine learning to classify water quality based on physicochemical and biological parameters. District-wise pH analysis and data preprocessing were performed to understand variations and improve data quality. Multiple models were evaluated to predict safe and unsafe water conditions.

**📝 Project Description**
This project focuses on the comprehensive analysis and classification of water quality using exploratory data analysis (EDA) and machine learning techniques. The primary objective is to assess water bodies based on key physicochemical and biological indicators, identify pollution sources and geographic hotspots, and develop a predictive model to classify water quality into use-based categories. The project addresses the critical need for effective water resource management and ensures water suitability for various purposes such as drinking, bathing, irrigation, and industrial use.

**🎯 Project Goals**

* Clean and preprocess raw water quality data for analysis

* Perform detailed exploratory data analysis to uncover pollution patterns

* Analyze district-wise and basin-wise water quality variations

* Classify water bodies into Use Based Classes (A, B, C, E)

* Build and optimize machine learning models for automated classification

* Provide actionable recommendations for water resource management

**Key Preprocessing Steps**

* Dropped irrelevant columns such as Use of Water in Down Stream, Remark, STN Code, Month, State Name

* Cleaned column names and categorical values by removing extra spaces

* Converted non-numeric entries like ND and (BDL) to NaN in numeric columns

* Converted sampling date to datetime format and sampling time to hour format

**Handled missing values:**

* Temperature & pH: District-wise mean imputation

* Other numeric parameters: District-wise median imputation

* Use Based Class: Rule-based classification using DO, BOD, and Total Coliform

* Encoded target variable (Use Based Class) using Label Encoding

* Addressed class imbalance using SMOTE (Synthetic Minority Oversampling Technique)

**📊 Exploratory Data Analysis (EDA) Summary**

1. Water Quality Distribution:

* 82% of samples were classified as Class A (drinking after disinfection)

* 11% belonged to Class E (irrigation/industrial use), indicating localized pollution

2. Pollution Sources:

* Industrial effluents and unclassified activities were major contributors to high BOD and COD

* Bathing, washing, and idol immersion significantly increased Fecal Coliform levels

3. Geographic Hotspots:

* Districts such as Akola, Dhule, Jalgaon, Mumbai, Nashik, Ratnagiri, Solapur, and Thane required severe treatment

* River basins like Mahim Creek, Ulhas, Arnala, and Bassein showed multiple parameter violations

4. pH Imbalances:

* Districts including Akola, Beed, Jalgaon, Jalna, Nagpur, Nanded, and Nashik had pH values outside the safe range (6.5–8.5)

5. Water Clarity vs Safety:

* Clear water samples still showed high fecal coliform and extremely high TDS (>3500 mg/L)

* Visual clarity alone is not a reliable indicator of water safety

6. Inter-parameter Correlations:

* Strong correlation between BOD and COD (organic pollution)

* High correlation among TDS, Conductivity, and Hardness (mineral contamination)

**🤖 Machine Learning Models and Evaluation**
Models Implemented

1. Random Forest Classifier

2. XGBoost Classifier

3. CatBoost Classifier

**Model Optimization**

* Class imbalance handled using SMOTE

* Hyperparameter tuning performed using RandomizedSearchCV

Best Model Performance

**CatBoost Classifier achieved the best results**

* Weighted F1-score: 0.89

* Demonstrated strong balance between precision and recall across all classes

**🔍 Key Findings and Recommendations**

-- Key Findings

* Presence of good-quality water alongside critical pollution hotspots

*Industrial and mixed human activities significantly degrade water quality

* Visual assessment is insufficient for determining water safety

* Machine learning models can reliably automate water quality classification

-- Recommendations

* Implement targeted remediation in districts and river basins requiring severe treatment

* Enforce stricter regulations on industrial effluents

* Increase public awareness about pollution-causing activities

* Establish continuous and comprehensive water quality monitoring systems

* Deploy the CatBoost model for real-time water quality prediction

**🛠️ Tools & Technologies**

1. Python

2. pandas, numpy

3. matplotlib, seaborn

4. scikit-learn, xgboost, catboost

5. imbalanced-learn (SMOTE)

6. Google Colab 
