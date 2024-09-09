variable "default_region" {
  description = "The default region to deploy resources"
  default     = "eu-central-1"
}

variable "domain_name" {
  description = "The domain name to use for the website"
  default = "aboa.today"
}

variable "subdomain" {
  description = "The subdomain to use for the website"
  default = "live"
}

variable "certificate_arn" {
  description = "The ARN of the certificate to use for the website"
  default = "arn:aws:acm:us-east-1:014605817411:certificate/820ef68f-0a42-4eec-94c5-490a3aa42756"
}