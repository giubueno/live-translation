# Create ACM certificate
resource "aws_acm_certificate" "api_cert" {
  domain_name       = "api.${var.domain_name}"
  validation_method = "DNS"

    tags = {
        Name = "api.${var.domain_name}"
    }

  lifecycle {
    create_before_destroy = true
  }
}

# Create Route53 record for ACM certificate validation
resource "aws_route53_record" "api_cert_validation" {
  for_each = {
    for dvo in aws_acm_certificate.api_cert.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  }

  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  ttl             = 300
  type            = each.value.type
  zone_id         = aws_route53_zone.root.zone_id
}
