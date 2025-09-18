# Brute Force, DDoS, and SQL Injection Attack Detection: A Comparative Analysis of Supervised Machine Learning Algorithms on Various Network Attacks

## Project Participants 

| Name           | Username         | Role              |
|----------------|------------------|-------------------|
| Kanchan Naik   | kanchan          | Developer, Writer |
| Spencer Dearman| dearmanspencer   | Developer, Writer |

## Project Description
- Network attacks have become a pervasive threat in today’s digital landscape, significantly impacting the security and availability of online services. Distributed Denial of Service (DDoS) attacks, SQL Injection vulnerabilities, and brute force FTP attacks exemplify the diverse range of threats that organizations face. DDoS attacks overwhelm services by flooding them with traffic from compromised devices, rendering them inaccessible to legitimate users. In 2016, for example, one of the most extensive instances of a DDoS attack was directed against the Domain Name System provider Dyn, employing a botnet composed of tens of millions of IP addresses. Major services, including Quora, Reddit, Amazon, SoundCloud, and the BBC, were entirely unavailable in North America and much of Europe for the duration of this attack, disrupting critical online activities such as e-commerce and voting. Meanwhile, SQL Injection, a critical vulnerability in OpenSSL, allows attackers to extract sensitive information from affected servers, posing significant risks to data security. Brute force FTP attacks exploit weak passwords to gain unauthorized access to servers, further highlighting the importance of robust security measures. In our project, we will compare the effectiveness of various machine learning models—Random Forest Trees, Naive Bayes, Logistic Regression, and a custom Deep Neural Network—in detecting these different types of attacks. By evaluating how well each algorithm performs in detecting DDoS, SQL Injection, and brute force FTP attacks, we will gain insights into their relative strengths and weaknesses. Additionally, we will assess the computational resources required for each model, allowing us to understand their efficiency in real-world applications. Our analysis will utilize three datasets to examine how these models respond to evolving attack patterns over time, ultimately providing a comprehensive overview of their effectiveness in securing network infrastructures against diverse threats.


## Data
- Datasets:
The Canadian Institute for Cybersecurity Intrusion Detection System (CICIDS) datasets, collected by the University of New Brunswick, serve as a comprehensive resource for intrusion detection. These datasets include both benign traffic and a range of contemporary attacks, including DDoS attacks, collected in packet capture (PCAP) files. The datasets provide the presence of all common available protocols, including HTTP, HTTPS, FTP, SSH, and email protocols, ensuring that our machine learning models can learn to recognize different attack patterns across communication channels. To prepare the CICIDS2017, CICIDS2018, and CICIDS2019 datasets, the datasets will be loaded into pandas dataFrames for manipulation and analysis using Matplotlib.

- Packages
  - Model deployment 
    - Scikit Learn (sklearn)
  - Cost metrics
    - Code Carbon (codecarbon)
  - Data visualization
    - Seaborn 
    - Matplotlib 
  
- Models
  - Random Forest Trees (SciKit)
  - Naive Bayes (SciKit)
  - Logistic Regression (SciKit)
  - Deep Neural Network (Custom)

## Deliverables
- **Jupyter Notebook**:
  - **Detection Performance Metrics**:
    - **Receiver Operating Characteristic (ROC) Curve**: Visualize the relationship between the true positive rate and the false positive rate.
    - **F1 Score**: Analyze accuracy with an emphasis on dataset imbalance between benign and malicious traffic.
    - **Accuracy**: Evaluate the proportion of correct predictions.
    - **Precision**: Measure the proportion of positive predictions that are correct.
    - **Confusion Matrix**: Summarize true positive, false positive, false negative, and true negative values to compare predicted vs. actual outcomes.

  - **Deployment Cost Metrics**:
    - **CPU/GPU Consumption**: Use Code Carbon to estimate electricity power consumption (CPU + GPU + RAM) and calculate the carbon intensity based on computation region.

- **Project Report (Sphinx)**:
  - **Data Formatting**:
    - Tables will be included for each dataset, broken down by model, with metrics such as ROC, F1, accuracy, and more.
  
  - **Dataset-Specific Comparisons**:
    - Direct comparisons of each model’s performance across datasets (CICIDS2017, CICIDS2018, CICIDS2019) for brute force, DDoS, and SQL Injection attacks.
    - Analysis of detection accuracy, F1 score, precision, and ROC curves across datasets.
    - Cost analysis comparing CPU/GPU power consumption and regional carbon footprint for each model per dataset.

### Model Performance Comparison by Model Type and Attack Type

#### Logistic Regression
| Dataset       | Attack Type       | ROC Curve | F1 Score | Accuracy | Precision | Confusion Matrix |
|---------------|-------------------|-----------|----------|----------|-----------|-------------------|
| CICIDS2017    | Brute Force       | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2017    | DDoS              | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2017    | SQL Injection     | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2018    | Brute Force       | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2018    | DDoS              | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2018    | SQL Injection     | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2019    | Brute Force       | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2019    | DDoS              | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2019    | SQL Injection     | ✓         | ✓        | ✓        | ✓         | ✓                 |

#### Random Forest
| Dataset       | Attack Type       | ROC Curve | F1 Score | Accuracy | Precision | Confusion Matrix |
|---------------|-------------------|-----------|----------|----------|-----------|-------------------|
| CICIDS2017    | Brute Force       | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2017    | DDoS              | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2017    | SQL Injection     | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2018    | Brute Force       | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2018    | DDoS              | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2018    | SQL Injection     | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2019    | Brute Force       | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2019    | DDoS              | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2019    | SQL Injection     | ✓         | ✓        | ✓        | ✓         | ✓                 |

#### Naive Bayes
| Dataset       | Attack Type       | ROC Curve | F1 Score | Accuracy | Precision | Confusion Matrix |
|---------------|-------------------|-----------|----------|----------|-----------|-------------------|
| CICIDS2017    | Brute Force       | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2017    | DDoS              | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2017    | SQL Injection     | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2018    | Brute Force       | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2018    | DDoS              | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2018    | SQL Injection     | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2019    | Brute Force       | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2019    | DDoS              | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2019    | SQL Injection     | ✓         | ✓        | ✓        | ✓         | ✓                 |

#### Deep Neural Network
| Dataset       | Attack Type       | ROC Curve | F1 Score | Accuracy | Precision | Confusion Matrix |
|---------------|-------------------|-----------|----------|----------|-----------|-------------------|
| CICIDS2017    | Brute Force       | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2017    | DDoS              | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2017    | SQL Injection     | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2018    | Brute Force       | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2018    | DDoS              | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2018    | SQL Injection     | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2019    | Brute Force       | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2019    | DDoS              | ✓         | ✓        | ✓        | ✓         | ✓                 |
| CICIDS2019    | SQL Injection     | ✓         | ✓        | ✓        | ✓         | ✓                 |

### Cost and Carbon Footprint Comparison by Model Type and Attack Type

#### Logistic Regression
| Dataset       | Attack Type       | CPU/GPU Power Consumption | Carbon Intensity |
|---------------|-------------------|---------------------------|-------------------|
| CICIDS2017    | Brute Force       | ✓                         | ✓                 |
| CICIDS2017    | DDoS              | ✓                         | ✓                 |
| CICIDS2017    | SQL Injection     | ✓                         | ✓                 |
| CICIDS2018    | Brute Force       | ✓                         | ✓                 |
| CICIDS2018    | DDoS              | ✓                         | ✓                 |
| CICIDS2018    | SQL Injection     | ✓                         | ✓                 |
| CICIDS2019    | Brute Force       | ✓                         | ✓                 |
| CICIDS2019    | DDoS              | ✓                         | ✓                 |
| CICIDS2019    | SQL Injection     | ✓                         | ✓                 |

#### Random Forest
| Dataset       | Attack Type       | CPU/GPU Power Consumption | Carbon Intensity |
|---------------|-------------------|---------------------------|-------------------|
| CICIDS2017    | Brute Force       | ✓                         | ✓                 |
| CICIDS2017    | DDoS              | ✓                         | ✓                 |
| CICIDS2017    | SQL Injection     | ✓                         | ✓                 |
| CICIDS2018    | Brute Force       | ✓                         | ✓                 |
| CICIDS2018    | DDoS              | ✓                         | ✓                 |
| CICIDS2018    | SQL Injection     | ✓                         | ✓                 |
| CICIDS2019    | Brute Force       | ✓                         | ✓                 |
| CICIDS2019    | DDoS              | ✓                         | ✓                 |
| CICIDS2019    | SQL Injection     | ✓                         | ✓                 |

#### Naive Bayes
| Dataset       | Attack Type       | CPU/GPU Power Consumption | Carbon Intensity |
|---------------|-------------------|---------------------------|-------------------|
| CICIDS2017    | Brute Force       | ✓                         | ✓                 |
| CICIDS2017    | DDoS              | ✓                         | ✓                 |
| CICIDS2017    | SQL Injection     | ✓                         | ✓                 |
| CICIDS2018    | Brute Force       | ✓                         | ✓                 |
| CICIDS2018    | DDoS              | ✓                         | ✓                 |
| CICIDS2018    | SQL Injection     | ✓                         | ✓                 |
| CICIDS2019    | Brute Force       | ✓                         | ✓                 |
| CICIDS2019    | DDoS              | ✓                         | ✓                 |
| CICIDS2019    | SQL Injection     | ✓                         | ✓                 |

#### Deep Neural Network
| Dataset       | Attack Type       | CPU/GPU Power Consumption | Carbon Intensity |
|---------------|-------------------|---------------------------|-------------------|
| CICIDS2017    | Brute Force       | ✓                         | ✓                 |
| CICIDS2017    | DDoS              | ✓                         | ✓                 |
| CICIDS2017    | SQL Injection     | ✓                         | ✓                 |
| CICIDS2018    | Brute Force       | ✓                         | ✓                 |
| CICIDS2018    | DDoS              | ✓                         | ✓                 |
| CICIDS2018    | SQL Injection     | ✓                         | ✓                 |
| CICIDS2019    | Brute Force       | ✓                         | ✓                 |
| CICIDS2019    | DDoS              | ✓                         | ✓                 |
| CICIDS2019    | SQL Injection     | ✓                         | ✓                 |

