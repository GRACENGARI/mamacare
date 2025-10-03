# Maternal Health Risk Analytics Dashboard

This QuickSight dashboard provides comprehensive insights into maternal health risk factors and patient monitoring.

## Dashboard Features

### Executive Summary Page
- **Total Patients KPI**: Shows total number of patients in the dataset
- **High Risk Patients KPI**: Count of patients classified as high risk
- **Risk Level Distribution**: Pie chart showing percentage breakdown of risk levels
- **Average Vital Signs**: Bar chart comparing vital signs across risk levels

### Risk Analysis Page
- **Blood Pressure Scatter Plot**: Shows relationship between systolic/diastolic BP colored by risk level
- **Age Distribution Box Plot**: Age ranges for each risk category
- **Heart Rate Histogram**: Distribution of heart rates across all patients
- **Risk Factors Summary Table**: Detailed statistics by risk level

## Quick Deployment

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure AWS Credentials**:
   ```bash
   aws configure
   ```

3. **Run Deployment Script**:
   ```bash
   python deploy-dashboard.py
   ```

4. **Follow Prompts**:
   - Enter your AWS Account ID
   - Choose AWS region (default: us-east-1)
   - Provide S3 bucket name for data storage
   - Enter QuickSight username (default: admin)

## Manual Setup (Alternative)

If you prefer manual setup:

### 1. Upload Data to S3
```bash
aws s3 cp "maternal health.csv" s3://your-bucket/maternal-health-data/
```

### 2. Create QuickSight Data Source
- Go to QuickSight console
- Create new data source → S3
- Point to your uploaded CSV file

### 3. Import Dashboard Definition
- Use the `dashboard-definition.json` file
- Import as new analysis/dashboard

## Dashboard Insights

### Key Metrics Tracked
- **Age**: Patient age distribution and correlation with risk
- **Blood Pressure**: Systolic and diastolic measurements
- **Blood Sugar (BS)**: Glucose levels
- **Body Temperature**: Temperature readings
- **Heart Rate**: Cardiac monitoring
- **Risk Level**: Classification (low, mid, high risk)

### Calculated Fields
- **Age Groups**: 20-25, 26-30, 31-35, 36+
- **BP Category**: Normal, Elevated, Hypertensive
- **Temperature Status**: Normal, Fever, Hypothermia
- **Risk Score**: Composite risk calculation

### Interactive Features
- **Age Range Filter**: Slider to filter by age range
- **Risk Level Filter**: Multi-select for risk categories
- **Cross-filtering**: Click on charts to filter other visuals
- **Drill-down**: Detailed patient data on demand

## Data Schema

| Column | Type | Description |
|--------|------|-------------|
| Age | Integer | Patient age in years |
| SystolicBP | Integer | Systolic blood pressure (mmHg) |
| DiastolicBP | Integer | Diastolic blood pressure (mmHg) |
| BS | Decimal | Blood sugar level (mmol/L) |
| BodyTemp | Decimal | Body temperature (°F) |
| HeartRate | Integer | Heart rate (bpm) |
| RiskLevel | String | Risk classification (low/mid/high risk) |

## Usage Tips

1. **Risk Assessment**: Use the scatter plot to identify patients with concerning BP combinations
2. **Age Analysis**: Box plots help identify age-related risk patterns
3. **Vital Signs Monitoring**: Bar charts show average vital signs by risk category
4. **Population Health**: Pie chart provides overall risk distribution overview

## Troubleshooting

### Common Issues
- **Permission Errors**: Ensure QuickSight has S3 access permissions
- **Data Source Connection**: Verify S3 bucket and file path are correct
- **Dashboard Loading**: Check that all calculated fields are properly defined

### Support
- Check AWS QuickSight documentation for detailed configuration
- Verify IAM permissions for QuickSight service
- Ensure CSV file format matches expected schema

## Cost Considerations

- **QuickSight Pricing**: Based on user licenses and SPICE capacity
- **S3 Storage**: Minimal cost for CSV file storage
- **Data Refresh**: Consider refresh frequency for cost optimization

## Security

- **Data Privacy**: Ensure PHI compliance if using real patient data
- **Access Control**: Configure appropriate QuickSight user permissions
- **Encryption**: Enable S3 and QuickSight encryption as needed