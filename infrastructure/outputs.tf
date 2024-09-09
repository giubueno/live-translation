output "name_servers" {
  value       = aws_route53_zone.root.name_servers
  description = "The name servers to configure in your domain registrar"
}

# Output the CloudFront distribution domain name
output "cloudfront_domain_name" {
  value = aws_cloudfront_distribution.s3_distribution.domain_name
}

output "api-ecr-repository-name" {
  value = aws_ecr_repository.api.name
}
