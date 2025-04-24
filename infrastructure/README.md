# Infrastructure Documentation

This directory contains the Terraform configuration for deploying the Live Translation application infrastructure on AWS. Below is a detailed explanation of all AWS resources and services created.

## AWS Resources Overview

### Networking
- **VPC** (`aws_vpc.main`)
  - CIDR Block: 10.0.0.0/16
  - Contains all other resources
  - Configured with public subnets for internet access

- **Internet Gateway** (`aws_internet_gateway.main`)
  - Attached to the VPC
  - Enables internet connectivity for public subnets

- **Route Tables** (`aws_route_table.main`)
  - Routes all internet-bound traffic (0.0.0.0/0) through the Internet Gateway
  - Associated with all subnets

- **Subnets** (`aws_subnet.main`)
  - 2 public subnets across different availability zones
  - Auto-assigns public IP addresses
  - Used for ECS tasks and ElastiCache

- **Security Groups** (`aws_security_group.main`)
  - Allows inbound HTTP (80) and HTTPS (443) traffic
  - Allows all outbound traffic
  - Special rule for Redis (6379) within VPC

### Compute & Container Services
- **ECS Cluster** (`aws_ecs_cluster.main`)
  - Name: live-translation-cluster
  - Runs the API service using Fargate

- **ECS Task Definition** (`aws_ecs_task_definition.api`)
  - Family: live-translation-api
  - CPU: 256
  - Memory: 512MB
  - Network mode: awsvpc
  - Container port: 80

- **ECS Service** (`aws_ecs_service.api`)
  - Name: live-translation-api
  - Desired count: 1
  - Launch type: FARGATE
  - Connected to Application Load Balancer

- **ECR Repository** (`aws_ecr_repository.api`)
  - Name: live-translation-api
  - Stores Docker images for the API service

### Load Balancing
- **Application Load Balancer** (`aws_lb.api`)
  - Type: application
  - Public-facing
  - Listens on ports 80 (HTTP) and 443 (HTTPS)
  - SSL/TLS termination

- **Target Group** (`aws_lb_target_group.api`)
  - Protocol: HTTP
  - Port: 80
  - Health check path: "/"
  - Target type: IP (for Fargate)

### Caching
- **ElastiCache Serverless** (`aws_elasticache_serverless_cache.api`)
  - Engine: Redis
  - Name: api
  - Data storage: 1GB
  - ECPU per second: 2000
  - Deployed in VPC
  - Accessible only from within VPC

### Storage
- **S3 Bucket** (`aws_s3_bucket.subdomain`)
  - Name format: {subdomain}-{domain_name}-eu
  - Configured for website hosting
  - Contains frontend application files

### CDN
- **CloudFront Distribution** (`aws_cloudfront_distribution.s3_distribution`)
  - Origin: S3 bucket
  - Supports IPv6
  - Default root object: index.html
  - SSL/TLS enabled
  - Custom domain support

### DNS
- **Route53 Zone** (`aws_route53_zone.root`)
  - Manages DNS records for the domain
  - Creates records for:
    - Root domain (A record to CloudFront)
    - API subdomain (A record to ALB)

### Certificates
- **ACM Certificate** (`aws_acm_certificate.api_cert`)
  - Domain: api.{domain_name}
  - DNS validation
  - Used for HTTPS on ALB and CloudFront

### IAM
- **ECS Task Execution Role** (`aws_iam_role.ecs_task_execution_role`)
  - Allows ECS to pull images from ECR
  - Allows writing logs to CloudWatch
  - Attached to ECS tasks

## Required Environment Variables

```bash
# AWS Credentials (Required)
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=eu-central-1

# Domain Configuration (Optional - has defaults)
TF_VAR_domain_name=aboa.today
TF_VAR_subdomain=live
TF_VAR_certificate_arn=your_certificate_arn
```

## Deployment Process

1. Initialize Terraform:
   ```bash
   terraform init
   ```

2. Plan the deployment:
   ```bash
   terraform plan
   ```

3. Apply the configuration:
   ```bash
   terraform apply
   ```

4. After deployment, note the outputs:
   - Name servers for DNS configuration
   - CloudFront distribution domain
   - ECR repository name
   - ElastiCache endpoint

## Security Considerations

- All sensitive data is stored within the VPC
- Public access is restricted to necessary services only
- SSL/TLS encryption for all public endpoints
- Security groups follow principle of least privilege
- ElastiCache is only accessible from within the VPC

## Cost Considerations

- Fargate pricing based on CPU and memory usage
- ElastiCache serverless pricing based on data storage and ECPU usage
- CloudFront pricing based on data transfer and requests
- S3 pricing based on storage and requests
- Consider using AWS Free Tier where applicable 