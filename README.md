# 🤰 MamaCare - Maternal Health Risk Prediction System

## Overview
MamaCare is an AI-powered maternal health risk prediction system that helps healthcare providers assess and classify maternal health risks into three categories: **Low Risk**, **Mid Risk**, and **High Risk**. The system uses machine learning to analyze clinical parameters and provide real-time risk assessments.

## 🔴 Problem Statement
Maternal mortality remains a critical challenge in healthcare systems worldwide. Early identification of high-risk pregnancies can significantly improve outcomes through timely interventions. MamaCare addresses this by providing:

- Automated risk assessment based on clinical parameters
- Real-time predictions for immediate decision support
- Scalable deployment through cloud infrastructure
- Easy integration with existing healthcare systems



[![AWS](https://img.shields.io/badge/AWS-Cloud%20Native-orange)](https://aws.amazon.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Development-yellow)](https://github.com/user/MamaCare-AI)

> An intelligent, compassionate AI agent designed to revolutionize maternal healthcare by providing continuous, personalized support throughout pregnancy, delivery, and postpartum periods.

## Overview

MamaCare-AI bridges critical gaps in maternal care access, particularly in underserved communities, while enhancing healthcare provider efficiency through 24/7 AI-powered support.

## Core Capabilities

### 24/7 Virtual Health Assistant
- **Always-Available Support**: Instant access to maternal health guidance
- **Multi-Language Communication**: Culturally sensitive interactions in local languages
- **Multi-Channel Access**: Smartphones, SMS, web platforms, and voice calls

### Personalized Pregnancy Journey Management
- **Dynamic Health Profiles**: Individual medical history and risk factor tracking
- **Customized Nutrition Guidance**: Evidence-based dietary recommendations
- **Automated Care Reminders**: Intelligent scheduling for appointments and medications
- **Milestone Tracking**: Week-by-week pregnancy guidance with personalized insights

### Advanced Risk Detection & Early Warning System
- **Symptom Pattern Analysis**: ML algorithms for concerning symptom combinations
- **Critical Alert Triggers**: Immediate flagging of high-risk conditions:
  - Severe bleeding or unusual discharge
  - Persistent severe headaches or vision changes (preeclampsia indicators)
  - Reduced fetal movement patterns
  - Signs of gestational diabetes or hypertension
  - Mental health concerns including postpartum depression risks
- **Progressive Risk Scoring**: Continuous maternal risk assessment

### Healthcare Network Integration
- **Seamless Provider Connectivity**: Real-time integration with local healthcare facilities
- **Emergency Escalation Protocols**: Automatic routing of urgent cases
- **Telemedicine Bridge**: Virtual consultations when physical visits aren't possible
- **Resource Mapping**: Dynamic database of nearby healthcare facilities and services

## Technical Architecture

### AWS-Powered AI Engine
| Service | Purpose |
|---------|---------|
| **Amazon Bedrock AgentCore** | Multi-step clinical reasoning and care planning engine |
| **Amazon SageMaker** | ML models for high-risk pregnancy symptom classification |
| **Amazon Bedrock (Claude/Titan)** | Multi-language conversational health Q&A |
| **Amazon Q** | Contextual retrieval of WHO guidelines and local health ministry documentation |
| **AWS Transform** | Structured conversation workflows for care coordination |

### Data & Storage Infrastructure
| Service | Purpose |
|---------|---------|
| **Amazon S3** | Anonymized health interaction logs with HIPAA compliance |
| **Amazon DynamoDB** | Real-time user profiles and pregnancy tracking data |
| **AWS HealthLake** | FHIR-compliant health data management and EHR integration |
| **Amazon KMS** | PHI data encryption and security |

### Integration & Accessibility
| Service | Purpose |
|---------|---------|
| **Amazon API Gateway + Lambda** | SMS/WhatsApp integration for low-connectivity areas |
| **Amazon EventBridge** | Automated care reminders and appointment scheduling |
| **External API Integration** | Emergency hotlines and clinic locator services |
| **Amazon Comprehend Medical** | Clinical entity extraction from user inputs |

### Compliance & Security
| Service | Purpose |
|---------|---------|
| **AWS Config + CloudTrail** | HIPAA audit trails and compliance monitoring |
| **VPC Endpoints** | Secure inter-service communication |
| **IAM Roles** | Least privilege access controls |
| **Amazon CloudWatch** | Critical health alert monitoring |

## Impact & Benefits

### For Expectant Mothers
- Reduced anxiety through reliable, instant health information access
- Improved pregnancy outcomes through consistent monitoring and guidance
- Enhanced healthcare engagement and appointment compliance
- Early detection and prevention of complications

### For Healthcare Systems
- Reduced burden on healthcare facilities through efficient triage
- Improved maternal mortality and morbidity statistics
- Enhanced resource allocation and emergency response
- Data-driven insights for public health planning

### For Communities
- Increased maternal health literacy and awareness
- Strengthened healthcare access in remote or underserved areas
- Cultural preservation through localized, respectful care approaches
- Community health worker support and training enhancement

## Implementation Strategy

### Deployment Phases
1. **Pilot Testing**: Initial rollout in select healthcare facilities
2. **Community Integration**: Expansion to community health worker networks
3. **Regional Scaling**: Broader geographic coverage with local adaptations
4. **National Integration**: Full healthcare system incorporation

### Quality Assurance
- Continuous clinical validation and safety monitoring
- Regular updates based on latest maternal health research
- Healthcare provider oversight and intervention protocols
- Outcome tracking and performance optimization

## Getting Started

### Prerequisites
- AWS Account with appropriate permissions
- AWS CLI configured
- Node.js 18+ or Python 3.9+

### Quick Start
```bash
# Clone the repository
git clone https://github.com/user/MediAssist-AI.git
cd MediAssist-AI

# Install dependencies
npm install

# Configure AWS credentials
aws configure

# Deploy infrastructure
npm run deploy
```

## API Documentation

### Health Assessment Endpoint
```http
POST /api/v1/health-assessment
Content-Type: application/json

{
  "userId": "string",
  "symptoms": ["string"],
  "gestationalWeek": "number",
  "riskFactors": ["string"]
}
```

### Emergency Alert Endpoint
```http
POST /api/v1/emergency-alert
Content-Type: application/json

{
  "userId": "string",
  "alertType": "string",
  "severity": "high|medium|low",
  "location": "string"
}
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- Email: support@mediassist-ai.com
- Discord: [Join our community](https://discord.gg/mamacare-ai)
- Documentation: [docs.mediassist-ai.com](https://docs.mamacareai.com)

## Acknowledgments

- World Health Organization (WHO) for maternal health guidelines
- Healthcare providers and community health workers for their invaluable feedback
- Open source community for foundational technologies

---

**MamacareAI** - Transforming maternal healthcare through compassionate AI technology for safer pregnancies and healthier outcomes worldwide.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/GRACENGARI/mamacare.git
cd mamacare

###installing the dependencies
pip install -r requirements.txt
📊 Dataset
The system uses the maternal_health.csv dataset containing clinical parameters for maternal health assessment.
🤖 Model Details

Algorithm: Random Forest Classifier,Logistics Regression,Knearest Neighbours,Gradient Radient Boosting Classifier

Techniques:

Feature Engineering
Hyperparameter Tuning
Cross-Validation


Evaluation Metrics:

Accuracy
Confusion Matrix
Feature Importance
