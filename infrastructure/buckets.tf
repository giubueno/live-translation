resource "aws_s3_bucket" "subdomain" {
  bucket = replace("${var.subdomain}-${var.domain_name}-eu", ".", "-")

  force_destroy = true
}

# Configure S3 bucket for website hosting
resource "aws_s3_bucket_website_configuration" "website_config" {
  bucket = aws_s3_bucket.subdomain.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}

# create a s3 access point
resource "aws_s3_access_point" "subdomain" {
  bucket = aws_s3_bucket.subdomain.bucket
  name   = aws_s3_bucket.subdomain.bucket
}

resource "aws_s3_bucket_policy" "subdomain" {
  bucket = aws_s3_bucket.subdomain.id

  policy = jsonencode({
    Version = "2012-10-17"
    Id      = "AllowGetObjects"
    Statement = [
      {
        Sid       = "AllowPublic"
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.subdomain.arn}/**"
      }
    ]
  })
}
